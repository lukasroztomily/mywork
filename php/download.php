<?php session_start(); 
if (isset($_SESSION["loggedin"]))
   {
    if((time() - $_SESSION['last_time']) > 1800)
    {
        header("location:logout.php"); 
        
    }
    } 
    
    $_SESSION['last_time'] = time();
    
    ?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/cerulean/bootstrap.min.css">
  <title>Download files</title>
      <style type="text/css">
        body{ font: 14px sans-serif; text-align: left; }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarColor01">
    <ul class="navbar-nav mr-auto">
    
      <li class="nav-item">
          <a href="welcome1.php"> <button type="button" class="btn btn-secondary disabled">Hlavní strana</button></a>
      </li>

  
    </ul>
    
 
      <a href="logout.php"> <button class="btn btn-danger my-2 my-sm-0" type="button">Odhlásit se</button></a> 
   
  </div>
</nav>
    <p><br/></p>
<div class="btn-group" role="group" aria-label="Basic example">
<p><br/></p>
    <div class = "container">
<table class = "table table-bordered">
 <div class="btn-group" role="group" aria-label="Basic example">
     
</div>   
<thead>
<tr>
<th>Nazev</th>
<th>Stahnout</th>
</tr>
</thead>
<tbody>
<?php 
//ob_start();
// Check if the user is logged in, if not then redirect him to login page

include "db.inc.php";
$username=$_SESSION["username"];
 $sql = "select * from FILES where USERS = '$username'
            AND FILENAME <> ''" ;
 $stmt= mysqli_query ($conn, $sql);
while($row = mysqli_fetch_array($stmt)){
if(empty($stmt)){
    $stmt = false; }
// ob_clean();
    // flush();
?>
 <tr>
 <td> <?php echo $row [ 'FILENAME' ] ?> </td>
<td class = "class center"> <a href="download1.php?id=<?php echo $row['ID'] ?>">Download</a></td>
</tr>
<?php
}
?>
</table>
</div>
<script src= "js/jquery.min.js"> </script>
<script src= "js/bootstrap.min.js"> </script>
</body>
</html>
