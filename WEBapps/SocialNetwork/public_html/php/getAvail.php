<?php
$username=$_GET["username"];
$dbc=mysqli_connect('localhost','root','1','mem_info') or die('Connection Lost !');
            $query="SELECT fname FROM info where username='$username'--";
            
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
