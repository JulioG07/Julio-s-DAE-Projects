<?php
header('Content-Type: application/json');
$conn = new mysqli("localhost", "root", "root", "expenseTracker");
if ($conn->connect_error) {
    echo json_encode(["error" => "DB connection failed"]);
    exit;
}

$sql = "
SELECT 
    u.user_id, u.first_name, u.last_name,
    s.amount AS salary, s.date_recorded,
    g.goal_amount, g.date_set,
    e.amount AS expenses, e.date_spent,
    gp.progress_percent, gp.onTrack
FROM users u
LEFT JOIN salaries s ON u.user_id = s.user_id
LEFT JOIN savings_goals g ON u.user_id = g.user_id
LEFT JOIN expenses e ON u.user_id = e.user_id
LEFT JOIN goal_progress gp ON u.user_id = gp.user_id
ORDER BY u.user_id DESC
";
$result = $conn->query($sql);

$data = [];
while ($row = $result->fetch_assoc()) {
    $data[] = $row;
}
echo json_encode($data);
$conn->close();
?>