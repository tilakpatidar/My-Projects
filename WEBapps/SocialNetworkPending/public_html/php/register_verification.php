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
      
        <script type="text/javascript" src="/js/jQuery.js"></script>
        <script type="text/javascript" src="/js/hoverText.js"></script>
         <link type="text/css" href="/css/register.css" rel="stylesheet"/>
        <script type="text/javascript">
           
            
        </script>
    </head>
    
    
    <body>
      <?php
      require_once('db_info.php');
      $fname=$_POST['fname'];
    $lname=$_POST['lname'];
    $sex=$_POST['sex'];
    $dob=$_POST['dob'];
    $email=$_POST['email'];
    
    $sec_q=$_POST['sec_q'];
    $sec_q2=$_POST['sec_q2'];
    $sec_a=$_POST['sec_a'];
    $pswd=$_POST['pswd1'];
    $pswd= file_get_contents("http://localhost/cgi-bin/enc.py?pswd=$pswd");
    $username=$_POST['username'];
    $mob1=$_POST['mob'];
    $alt_name=$_POST['alt_name'];
   $ques="";
      if(empty($sec_q))
      {
          $ques=$sec_q2;
      }
      elseif(empty($sec_q2))
      {
          $ques=$sec_q;
      }
    
     
    
     
    
    $code=rand(10000,99999);
    //now updating our database
                                
                                 $dbc=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Something went wrong !');
                                /* check connection */
                                if (mysqli_connect_errno()) {
                                    printf("Connect failed: %s\n", mysqli_connect_error());
                                    exit();
                                }

                                /* disable autocommit */
                                mysqli_autocommit($dbc, FALSE);

                                mysqli_query($dbc, "START TRANSACTION;--");
                                mysqli_query($dbc, "INSERT INTO mem_email_verification(code,email) VALUES('$code','$email');--");
                                mysqli_query($dbc, "INSERT INTO mem_info(username,fname,lname,sex,dob,mob1,alt_name,email,pswd,sec_q,sec_a) VALUES('$username','$fname','$lname','$sex','$dob','$mob1','$alt_name','$email','$pswd','$ques','$sec_a');--");
                                mysqli_query($dbc,"COMMIT;--");
                                /* commit insert */
                                mysqli_commit($dbc);
                                mysqli_close($dbc);
                
               
                
                
               
                                         
    $to=$email;
    $subject="Email verification for amogosnet";
    
    
    $message="Your verification code is ".$code.".You can also activate your account by clicking th link below."."'<a  target='_blank' href='localhost/php/register_verification2.php?email='.$email.'&code='.$code'>Click this Link</a>";
    
    mail($to, $subject, $message,'From:'.'tilakpatidar@gmail.com');
    echo 'A verification email has been sent to your registered email address i.e <strong> '.$email.' </strong>';
    
    ?>  
        <form name="verify" id="verify" method="POST" action="/php/register_verification1.php">
            <input type="submit" id="submit" value="Click to verify code recieved"/>
            
        </form>
    </body>
</html>
