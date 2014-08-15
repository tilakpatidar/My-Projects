<?php
// In PHP versions earlier than 4.1.0, $HTTP_POST_FILES should be used instead
// of $_FILES.

$uploaddir = '/var/www/AmigosNet/public_html/Files/';
$uploadfile = $uploaddir .$_GET['username']. basename($_FILES['type']);

echo '<pre>';
if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
    echo "1";//success
} else {
    echo "0";
}

echo 'Here is some more debugging info:';
print_r($_FILES);

print "</pre>";

?>
