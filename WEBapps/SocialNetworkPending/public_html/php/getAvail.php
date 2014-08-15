<?php
require_once('db_info.php');
$username=$_GET["username"];
$dbc=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Connection Lost !');
            $query="SELECT fname FROM mem_info where username='$username'--";
            
            $result=mysqli_query($dbc,$query) or die('Connection Lost');
            $row=  mysqli_fetch_array($result);
            if(empty($row['fname']))
            {
                $response="Available";
            }
            else
            {
                $response="Not Available";
            }
            echo ''.$response;
?>
