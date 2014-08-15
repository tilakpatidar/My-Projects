<?php
require_once('db_info.php');
 
if (isset($_GET['term'])){
	$return_arr = array();
 
	try {
	    $conn = new PDO("mysql:host=".DB_HOST.";port=3306;dbname=".DB_NAME, DB_USER, DB_PASSWORD);
	    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	    
	    $stmt = $conn->prepare('SELECT DISTINCT profile_pic,CONCAT(fname,CONCAT(CONCAT(" ",lname))),vertical,username FROM info WHERE fname LIKE :term OR lname LIKE :term OR regno LIKE :term OR username LIKE :term OR vertical LIKE :term LIMIT 5');
	    $stmt->execute(array('term' => '%'.$_GET['term'].'%'));
	    
	    while($row = $stmt->fetch()) {
	        $return_arr[] ='<!'.$row['username'].'><div style="float:left;padding-top:10px;padding-bottom:10px;">'.'<img src="/images/'.$row['profile_pic'].'" class="image" width=60 height=55></img></div><label><div style="float:right"><div style="float:top;font-size:larger;padding-top:10px;padding-bottom:10px;  font-style:normal; font-weight:lighter;margin-left:20px;">'.$row['CONCAT(fname,CONCAT(CONCAT(" ",lname)))'].'</div><div style="font-size:small;  font-style:normal; font-weight:lighter;margin-left:20px;float:bottom;">Vertical : '.$row['vertical'].'</label></div></div>';
	    }
            $return_arr[]="<center><div style='color:#0044cc;text-decoration:underline;font-size:small;'>Search using filters</div></center>";
	} catch(PDOException $e) {
	    echo 'ERROR: ' . $e->getMessage();
	}
 
 
    /* Toss back results as json encoded array. */
    echo json_encode($return_arr);
}
 
?>
