<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>www.amigosNet.com</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width">
    </head>
    <?php
    require_once('db_info.php');
    $fname=$_POST['fname'];
    $lname=$_POST['lname'];
    $sex=$_POST['sex'];
    $dob=$_POST['dob'];
    $email=$_POST['email'];
    $sec_q1=$_POST['sec_q1'];
    $sec_q2=$_POST['sec_q2'];
    $sec_a=$_POST['sec_a'];
    $pswd=$_POST['pswd1'];
    if(empty($sec_q1))
    {
        $sec_q=$sec_q2;
    }
    else if(empty($sec_q2))
    {
        $sec_q=$sec_q1;
    }
    $code=rand(10000,99999);
    $to=$email;
    $subject="Email verification for amogosnet";
    
    $header = "From:abc@somedomain.com \r\n";
    $header = "Cc:afgh@somedomain.com \r\n";
    $header .= "MIME-Version: 1.0\r\n";
    $message="Your verification code is ".$code;
    
    mail($to, $subject, $message,$header);
    echo 'A verification email has been sent to your registered email address i.e <br><center><strong>Blah</strong></center>';
    ?>
    
    <body>
        
    </body>
</html>
