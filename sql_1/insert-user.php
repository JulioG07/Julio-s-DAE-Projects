<?php
header('Content-Type: application/json');
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Only accept POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(["error" => "Only POST requests are allowed"]);
    exit;
}

// Get raw input and decode
$rawInput = file_get_contents("php://input");
$data = json_decode($rawInput, true);

// Validate input
if (
    !isset($data['uid']) || empty($data['uid']) ||
    !isset($data['firstName']) || empty($data['firstName']) ||
    !isset($data['lastName']) || empty($data['lastName']) ||
    !isset($data['email']) || empty($data['email'])
) {
    http_response_code(400);
    echo json_encode(["error" => "Invalid or missing data", "received" => $rawInput]);
    exit;
}

// Database connection
$conn = new mysqli("localhost", "root", "root", "expenseTracker");

if ($conn->connect_error) {
    http_response_code(500);
    echo json_encode(["error" => "Database connection failed"]);
    exit;
}

// Prepare and insert
$stmt = $conn->prepare("INSERT INTO users (firebase_uid, first_name, last_name, email) VALUES (?, ?, ?, ?)");
$stmt->bind_param("ssss", $data['uid'], $data['firstName'], $data['lastName'], $data['email']);

if ($stmt->execute()) {
    echo json_encode(["status" => "success"]);
} else {
    http_response_code(400);
    echo json_encode(["status" => "failed", "message" => $stmt->error]);
}

$stmt->close();
$conn->close();
?>
