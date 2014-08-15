<html>
    <head><title></title></head>
    <body>
        <?php
        require_once('db_info.php');
        
// In PHP versions earlier than 4.1.0, $HTTP_POST_FILES should be used instead
// of $_FILES.

$uploaddir = '/var/www/AmigosNet/public_html/Files/';
$uploadfile = $uploaddir . basename($_FILES['img']['name']);


if (move_uploaded_file($_FILES['img']['tmp_name'], $uploadfile )) {
    echo '1';
  /*  $username=$_POST['username'];
        $alt_name=$_POST['alt_name'];
        $interested_in=$_POST['interestedin'];
        $mob2=$_POST['mob2'];
        $mob3=$_POST['mob3'];
        $website=$_POST['website'];
        $place_ob=$_POST['place_ob'];
        $place_cc=$_POST['place_cc'];
        $place_ht=$_POST['place_ht'];
        $about_you=$_POST['about_you'];
        $lang=$_POST['lang'];
        $religion=$_POST['religion'];
        $email=$_POST['email'];
     $dbc=mysqli_connect('localhost','root','1','member') or die('Something went wrong !');
                                    if (mysqli_connect_errno()) {
                                    printf("Connect failed: %s\n", mysqli_connect_error());
                                    exit();
                                }
                                mysqli_autocommit($dbc, FALSE);
                                mysqli_query($dbc, "START TRANSACTION;--");
                                mysqli_query($dbc, "UPDATE mem_info SET verified='2',alt_name='$alt_name',interested_in='$interested_in',mob2='$mob2',mob3='$mob3',website='$website',place_ob='$place_ob',place_cc='$place_cc',place_ht='$place_ht',about_you='$about_you',lang='$lang',religion='$religion' WHERE username='$username'--");
                                mysqli_query($dbc, "DELETE FROM mem_email_verification WHERE email='$email';--");
                                mysqli_query($dbc,"COMMIT;--");
                                mysqli_commit($dbc);
                                mysqli_close($dbc);
    
    */
}
 else {
    echo '0';
}


?>

    </body>
</html>