<?php

 
if (isset($_GET['term'])){
	$return_arr = array();
 
	
	   
	    
	    
	    $return_arr[] ='<!fname><div style="font-size:small;font-weight:200;"><label>First Name :</label></div>';
            $return_arr[] ='<!lname><div style="font-size:small;font-weight:200;"><label>Last Name :</label></div>';
	    $return_arr[] ='<!sex><div style="font-size:small;font-weight:200;"><label>Sex :</label></div>';
            $return_arr[] ='<!email><div style="font-size:small;font-weight:200;"><label>Email Address :</label></div>';
            $return_arr[] ='<!vertical><div style="font-size:small;font-weight:200;"><label>Vertical :</label></div>';
            $return_arr[] ='<!category><div style="font-size:small;font-weight:200;"><label>Category :</label></div>';
            $return_arr[] ='<!year><div style="font-size:small;font-weight:200;"><label>Year :</label></div>';
            //$return_arr[]="<center><div style='color:#0044cc;text-decoration:underline;font-size:small;'>Search using filters</div></center>";
	
 
 
    /* Toss back results as json encoded array. */
    echo json_encode($return_arr);
}
 
?>
