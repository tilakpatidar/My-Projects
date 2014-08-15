<?php
require_once('db_info.php');
 
if (isset($_GET['term'])){
	$return_arr = array();
 
	try {
	    $conn = new PDO("mysql:host=".DB_HOST.";port=3306;dbname=".DB_NAME, DB_USER, DB_PASSWORD);
	    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	    
	    $stmt = $conn->prepare('SELECT DISTINCT(lang) FROM lang WHERE lang LIKE :term LIMIT 10');
	    $stmt->execute(array('term' => '%'.$_GET['term'].'%'));
	    
	    while($row = $stmt->fetch()) {
	        $return_arr[] =  $row['lang'];
	    }
 
	} catch(PDOException $e) {
	    echo 'ERROR: ' . $e->getMessage();
	}
 
 
    /* Toss back results as json encoded array. */
    echo json_encode($return_arr);
}
 
?>
