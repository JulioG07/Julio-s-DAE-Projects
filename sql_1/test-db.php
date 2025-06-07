<?php
$conn = new mysqli('localhost', 'root', 'root', 'expenseTracker');
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
echo 'Connected successfully!';
?>