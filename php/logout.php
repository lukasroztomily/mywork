<?php
ob_start();
// Initialize the session
require_once "db.inc.php";
session_start();
 $idd = session_id();  
 mysqli_query($conn, "update LOGIN_TRACK set logout_time=current_timestamp where id_session = '$idd' ");	
// Unset all of the session variables
$_SESSION = array();

// Destroy the session.
session_destroy();

 
// Redirect to login page
header("location: login2.php");
exit;
ob_end_flush();
?>
