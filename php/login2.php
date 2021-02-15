<?php
ob_start();

session_start();

if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
    header("location: welcome1.php");
    //$_SESSION['last_time'] = time();
    exit;
}
// Include config file
require_once "db.inc.php";

$username = $password = "";
$username_err = $password_err = "";
 

if($_SERVER["REQUEST_METHOD"] == "POST"){
 
    
    if(empty(trim($_POST["username"]))){
        $username_err = "Zadejte jmeno.";
    } else{
        $username = trim($_POST["username"]);
    }  
    
    if(empty(trim($_POST["password"]))){
        $password_err = "Zadejte vaše heslo.";
    } else{
        $password = trim($_POST["password"]);
    }
    
    if(empty($username_err) && empty($password_err)){
        
        $sql = "SELECT DISTINCT id, username, password FROM users WHERE username =  ? ";
        
        if($stmt = mysqli_prepare($conn, $sql)){
            
            mysqli_stmt_bind_param($stmt, "s", $param_username);
            
            
            $param_username = $username;
            
            
            if(mysqli_stmt_execute($stmt)){
                
                mysqli_stmt_store_result($stmt);
                
                
                if(mysqli_stmt_num_rows($stmt) == 1) {                    
                    
                     $username = $_POST [ 'username' ];
                    
                    mysqli_stmt_bind_result($stmt, $id, $username, $hashed_password);
                    if(mysqli_stmt_fetch($stmt)){
                        if(password_verify($password, $hashed_password)){
                            
                         //   $newid = session_create_id('my-');
                            session_regenerate_id();
                            //session_start();
     			    

                            
                            $_SESSION["loggedin"] = true;
                            
                            $_SESSION['id']=$num['id'];
                             $idd = session_id();  
                             $_SESSION['last_time'] = time();
                             $_SESSION['username']=$username;                          
					mysqli_query($conn, "INSERT INTO login_track(id_session, username) VALUES('$idd','$username')");

                            
                            header("location: welcome1.php");
                } else{
                            
                            $password_err = "Bylo zadané špatné heslo";
                        }
                    }
                } else{
                    
                    $username_err = "Účet neexistuje.";
                }
            } else{
                echo "Něco se pokazilo. Zkuste to ještě jednou";
            }
        }   
       
        
        mysqli_stmt_close($stmt);
    }
    
    mysqli_close($conn);
}
ob_end_flush();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Přihlášení</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
    <style type="text/css">
        body{ font: 14px sans-serif; }
        .wrapper{ width: 350px; padding: 20px; }
    </style>
</head>
<body>
    <div class="wrapper">
        <h2>Přihlášení</h2>
        <p>Vypln své jméno a heslo</p>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
            <div class="form-group <?php echo (!empty($username_err)) ? 'has-error' : ''; ?>">
                <label>Username</label>
                <input type="text" name="username" class="form-control" value="<?php echo $username; ?>">
                <span class="help-block"><?php echo $username_err; ?></span>
            </div>    
            <div class="form-group <?php echo (!empty($password_err)) ? 'has-error' : ''; ?>">
                <label>Password</label>
                <input type="password" name="password" class="form-control">
                <span class="help-block"><?php echo $password_err; ?></span>
            </div>
            <div class="form-group">
                <input type="submit" class="btn btn-primary" value="Přihlásit">
            </div>
            <p>Nemáš účet? <a href="register.php">Zde se můžeš zaregistrovat</a>.</p>
        </form>
    </div>    
</body>
</html>
