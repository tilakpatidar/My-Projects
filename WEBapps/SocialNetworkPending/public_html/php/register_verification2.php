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
        <meta http-equiv="refresh" content="10; URL=/login.php"><!Redirecting>
        <script type="text/javascript" src="/js/jQuery.js"></script>
        <script type="text/javascript" src="/js/hoverText.js"></script>
         <link type="text/css" href="/css/register.css" rel="stylesheet"/>
        <script type="text/javascript">
           
        </script>
    </head>
    
    
    <body>
     <?php
     require_once('db_info.php');
     function transact($email){
                 $dbc=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Something went wrong !');
                                    if (mysqli_connect_errno()) {
                                    printf("Connect failed: %s\n", mysqli_connect_error());
                                    exit();
                                }
                                mysqli_autocommit($dbc, FALSE);
                                mysqli_query($dbc, "START TRANSACTION;--");
                                mysqli_query($dbc, "UPDATE mem_email_verification SET status='1' WHERE email='$email'--");
                                mysqli_query($dbc, "UPDATE mem_info SET verified='1' WHERE email='$email';--");
                                mysqli_query($dbc,"COMMIT;--");
                                mysqli_commit($dbc);
                                mysqli_close($dbc);
     }
     $email=$_POST['email'];
     $code=$_POST['code'];
        $dbc=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Something went wrong !');

        $query="SELECT code from mem_email_verification where status='0' AND email='$email'--";
        $result=mysqli_query($dbc,$query) or die('Error in result');
        $row=  mysqli_fetch_array($result);
        mysqli_close($dbc);
            if(empty($row['code']))
            {
                echo 'No pending requests found for '.$email;
            }
            else {
                $rcode=$row['code'];
                if($rcode==$code )
                {
                    
                    transact($email);
                    //Redirecting
                    echo 'Code Matched.<br/> Redirecting to login page in 10seconds . . . .';
                   
                }
                else
                {
                    echo 'Invalid Code Entered';
                }

           }

     ?>
       
    </body>
</html>
