<?php
header('Content-Type: application/json');
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Connect to database
$conn = new mysqli("localhost", "root", "root", "expenseTracker");
if ($conn->connect_error) {
    echo json_encode(["message" => "Database connection failed: " . $conn->connect_error]);
    exit;
}

// Get and sanitize input
$first_name = $conn->real_escape_string($_POST['first_name'] ?? '');
$last_name = $conn->real_escape_string($_POST['last_name'] ?? '');
$salary = floatval($_POST['salary'] ?? 0);
$savings_goal = floatval($_POST['savings_goal'] ?? 0);
$expenses = floatval($_POST['expenses'] ?? 0);

// Basic validation
if (!$first_name || !$last_name || !$salary || !$savings_goal || !$expenses) {
    echo json_encode(["message" => "Missing required fields."]);
    exit;
}

// 1. Insert user or get existing user_id
$user_id = null;
$user_check = $conn->query("SELECT user_id FROM users WHERE first_name='$first_name' AND last_name='$last_name' LIMIT 1");
if ($user_check && $user_check->num_rows > 0) {
    $row = $user_check->fetch_assoc();
    $user_id = $row['user_id'];
} else {
    if (!$conn->query("INSERT INTO users (first_name, last_name) VALUES ('$first_name', '$last_name')")) {
        echo json_encode(["message" => "User insert failed: " . $conn->error]);
        exit;
    }
    $user_id = $conn->insert_id;
}

// 2. Insert salary
if (!$conn->query("INSERT INTO salaries (user_id, amount, date_recorded) VALUES ($user_id, $salary, CURDATE())")) {
    echo json_encode(["message" => "Salary insert failed: " . $conn->error]);
    exit;
}
$salary_id = $conn->insert_id;

// 3. Insert savings goal
if (!$conn->query("INSERT INTO savings_goals (user_id, goal_amount, date_set) VALUES ($user_id, $savings_goal, CURDATE())")) {
    echo json_encode(["message" => "Savings goal insert failed: " . $conn->error]);
    exit;
}
$savings_id = $conn->insert_id;

// 4. Insert expenses
if (!$conn->query("INSERT INTO expenses (user_id, amount, date_spent) VALUES ($user_id, $expenses, CURDATE())")) {
    echo json_encode(["message" => "Expenses insert failed: " . $conn->error]);
    exit;
}
$expense_id = $conn->insert_id;

// 5. Calculate progress and onTrack
$progress = ($savings_goal > 0) ? (($salary - $expenses) / $savings_goal) * 100 : 0;
$onTrack = ($progress >= 100) ? 1 : 0;

// 6. Insert into goal_progress
if (!$conn->query("INSERT INTO goal_progress (user_id, salary_id, savings_id, expense_id, progress_percent, onTrack) VALUES ($user_id, $salary_id, $savings_id, $expense_id, $progress, $onTrack)")) {
    echo json_encode(["message" => "Goal progress insert failed: " . $conn->error]);
    exit;
}

// 7. Return message
echo json_encode([
    "message" => "Data submitted! You are " . round($progress, 2) . "% towards your goal. " . ($onTrack ? "On track!" : "Not on track."),
    "progress" => round($progress, 2)
]);
$conn->close();
?>