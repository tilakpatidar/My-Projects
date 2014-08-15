<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
<?php

require_once('db_info.php');
$pswd=$_GET['id'];
$uname=$_GET['uname'];
function validateEmail($sEmail) {
                $pattern="/^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/";
                   $filter = preg_match($pattern,$sEmail);
                   
                    if ($filter==1) {

                        return 1;
                    }
                    else if($filter==0) {

                        return 0;
                    }
            }
         if(is_numeric($uname))
                    {
                        //user entered mob
                        echo 'Mob';

                    $dbc=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Connection Lost !');
                    $query="SELECT fname FROM mem_info where mob1='$uname'--";

                    $result=mysqli_query($dbc,$query) or die('Connection Lost');
                    $row=  mysqli_fetch_array($result);

                    mysqli_close($dbc);

                       if(empty($row['fname']))
                            {


                            $reason='Invalid mobile number !';
                            header("Location:login_attempt.php?reason=$reason");
                            }
                            else
                            {
                                        $dbc1=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Connection Lost !');
                                        $query1="SELECT fname,verified,username,pswd FROM mem_info where mob1='$uname' AND pswd='$pswd';--";
                                        $result1=mysqli_query($dbc1,$query1) or die('Connection Lost');
                                        $row1=  mysqli_fetch_array($result1);
                                        mysqli_close($dbc1);
                                        if(empty($row1['fname']))
                                        {

                                                $reason='Invalid password!';
                                                header("Location:login_attempt.php?reason=$reason");
                                        }
                                        else
                                        {
                                            
                                            $_SESSION['username'] = $row1['username'];
                                            
                                            setcookie('username', $row1['username'], time() + (60 * 60 * 24 * 30),'/');  // expires in 30 days
                                            $_SESSION['pswd'] = $row1['pswd'];
                                            setcookie('pswd', $row1['pswd'], time() + (60 * 60 * 24 * 30),'/');  // expires in 30 days
                                           
                                            
                                            
                                            
                                            
                                                echo 'success ';
                                                    if ($row1['verified']==0)
                                                        {
                                                            echo 'Unverified';   
                                                        }
                                                        else if($row1['verified']==1)
                                                        {
                                                             echo 'Verified'; 
                                                             $username=$row1['username'];
                                                             
                                                             header("Location:/php/profile_edit.php?username=$username");

                                                             echo 'Verified but profile not completed';
                                                        }
                                                        else if($row1['verified']==2)
                                                        {

                                                             //redirect to home page
                                                        }

                                        }
                            }

                    }
                    else if(validateEmail($uname)==1)
                    {
                        //user entered email
                        echo 'email';

                          $dbc=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Connection Lost !');
                    $query="SELECT fname FROM mem_info where email='$uname'--";

                    $result=mysqli_query($dbc,$query) or die('Connection Lost');
                    $row=  mysqli_fetch_array($result);

                    mysqli_close($dbc);

                       if(empty($row['fname']))
                            {


                            $reason='Invalid email address !';
                            header("Location:login_attempt.php?reason=$reason");
                            }
                            else
                            {
                                
                                        $dbc1=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Connection Lost !');
                                        $query1="SELECT fname,verified,username,pswd FROM mem_info where email='$uname' AND pswd='$pswd';--";
                                        $result1=mysqli_query($dbc1,$query1) or die('Connection Lost');
                                        $row1=  mysqli_fetch_array($result1);
                                        mysqli_close($dbc1);
                                        if(empty($row1['fname']))
                                        {
                                                echo 'Invalid password!';
                                        }
                                        else
                                        {
                                            $_SESSION['username'] = $row1['username'];
                                            setcookie('username', $row1['username'], time() + (60 * 60 * 24 * 30),'/');  // expires in 30 days
                                            $_SESSION['pswd'] = $row1['pswd'];
                                            setcookie('pswd', $row1['pswd'], time() + (60 * 60 * 24 * 30),'/');  // expires in 30 days
                                            
                                            
                                                echo 'success ';
                                                    if ($row1['verified']==0)
                                                        {
                                                            echo 'Unverified';   
                                                        }
                                                        else if($row1['verified']==1)
                                                        {
                                                             echo 'Verified'; 
                                                             $username=$row1["username"];
                                                             header("Location:/php/profile_edit.php?username=$username");
                                                             echo 'Verified but profile not completed'; 
                                                        }
                                                        else if($row1['verified']==2)
                                                        {

                                                             //redirect to home page
                                                        }

                                        }
                            }

                    }
                    else {
                        //user entered username


                    $dbc=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Connection Lost !');
                    $query="SELECT fname FROM mem_info where username='$uname'--";

                    $result=mysqli_query($dbc,$query) or die('Connection Lost');
                    $row=  mysqli_fetch_array($result);

                    mysqli_close($dbc);

                       if(empty($row['fname']))
                            {


                            $reason='Invalid username !';
                            header("Location:login_attempt.php?reason=$reason");
                            }
                            else
                            {
                                
                                        $dbc1=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Connection Lost !');
                                        $query1="SELECT fname,verified,username,pswd FROM mem_info where username='$uname' AND pswd='$pswd';--";
                                        $result1=mysqli_query($dbc1,$query1) or die('Connection Lost');
                                        $row1=  mysqli_fetch_array($result1);
                                        mysqli_close($dbc1);
                                        if(empty($row1['fname']))
                                        {

                                              //  $reason='Invalid password !';
                                             //   header("Location:login_attempt.php?reason=$reason");
                                        }
                                        else
                                        {
                                            
                                            $_SESSION['username'] = $row1['username'];
                                            setcookie('username', $row1['username'], time() + (60 * 60 * 24 * 30),'/');  // expires in 30 days
                                            $_SESSION['pswd'] = $row1['pswd'];
                                            setcookie('pswd', $row1['pswd'], time() + (60 * 60 * 24 * 30),'/');  // expires in 30 days
                                                echo 'success ';
                                                        if ($row1['verified']==0)
                                                                {
                                                                    echo 'Unverified';   
                                                                }
                                                                else if($row1['verified']==1)
                                                                {
                                                                     echo 'Verified'; 
                                                                     header("Location:/php/profile_edit.php?username=$uname");
                                                                     echo 'Verified but profile not completed'; 
                                                                }
                                                                else if($row1['verified']==2)
                                                                {
                                                                     //redirect to home page
                                                                }

                                        }
                            }

                    }
        ?>        
    </body>
</html>

