<?php session_start(); ?>
<?php
ob_start();
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: login2.php");
    exit;
}
require_once "db.inc.php";
if (isset($_GET['id'])) {
    $id = $_GET['id'];
error_reporting(E_ALL);
$username=$_SESSION["username"];
    // fetch file to download from database
$sql = "SELECT * FROM FILES WHERE ID=$id";
   $result = mysqli_query($conn, $sql);

    $file = mysqli_fetch_assoc($result);
    $filepath = 'upload_users/' . $username . "/" . $file[ 'FILENAME' ];

if (file_exists($filepath)) {
        header("Content-Description: File Transfer");
        header("Content-Type: application/octet-stream");
        header("Content-Disposition: attachment; filename=" . basename($filepath));
        header("Expires: 0");
        header("Cache-Control: must-revalidate");
        header("Pragma: public");
        header("Content-Length: " . filesize('upload_users/' . $username . "/" . $file['FILENAME']));
        ob_clean();
        flush();
        readfile($filepath);
        exit;
    }
}
?>
