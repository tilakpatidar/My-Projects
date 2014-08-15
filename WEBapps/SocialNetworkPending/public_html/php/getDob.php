
<?php
$username=$_GET['username'];
$dbc=  mysqli_connect('localhost','root','1','member')or die('Unable to connect to db');
$query="SELECT dob FROM mem_info WHERE username='$username';--";
$result=  mysqli_query($dbc,$query) or die('Connection Lost');
        
        while ($row=  mysqli_fetch_array($result))
        {
          echo "".$row['dob'];  
        }
?>
