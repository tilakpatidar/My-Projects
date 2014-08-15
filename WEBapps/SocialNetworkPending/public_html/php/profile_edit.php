<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>TODO supply a title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width">
        <script type="text/javascript" src="/js/jQuery.js"></script>
       <script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="http://code.jquery.com/ui/1.10.1/jquery-ui.min.js"></script>
  <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.1/themes/base/minified/jquery-ui.min.css" type="text/css" /> 
        <link href="/bootstrap-3.1.1-dist/css/bootstrap.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.min.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.min.css" rel="stylesheet" media="screen">
         <link type="text/css" href="/css/profile_edit.css" rel="stylesheet"/>
         <script type="text/javascript">
              var countries;//global connected with getCountries and copyCountries
              var uname;
              var files;
             
           
		function capitalizeMe(val){
                return val.charAt(0).toUpperCase()+val.substr(1).toLowerCase();
            }					
		 
		
             $(document).ready(function(){
                
                 $("#body").show();
             $("#warning").hide();
                 
                 function getUsername(){
                     return uname;
                 }
               
                 uname="<?php $username=$_GET['username'];echo $username; ?>";
                 $("#username").val(uname);
                 <?php
                    require_once('db_info.php');
                    $dbc=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME) or die('Connection Lost !');
                    $query="SELECT fname, lname, sex, dob, mob1, alt_name, email FROM mem_info where username='$username';--";

                    $result=mysqli_query($dbc,$query) or die('Connection Lost');
                    $row=  mysqli_fetch_array($result);
                    $fname=$row['fname'];
                    $lname=$row['lname'];
                    $sex=$row['sex'];
                    $dob=$row['dob'];
                    $mob1=$row['mob1'];
                    $alt_name=$row['alt_name'];
                    $email=$row['email'];
                    mysqli_close($dbc);
                    
                    
                    
                 ?>
                         
                         $("#fname").val("<?php echo ''.$fname;?>");
                         $("#lname").val("<?php echo ''.$lname;?>");
                         $("#sex").val("<?php echo ''.$sex;?>");
                         $("#dob").val("<?php echo ''.$dob;?>");
                         $("#mob1").val("<?php echo ''.$mob1;?>");
                         $("#alt_name").val("<?php echo ''.$alt_name;?>");
                         $("#email").val("<?php echo ''.$email;?>");
               
             });
                
             
             
             
             
             function imgSubmit(){
                    if($("#select_img").val()!=="")
                    {
                       
                            
                            $("#warning").attr("class","alert alert-success");
                            document.getElementById("warning").innerHTML="<strong>Well Done! Your profile picture was successfully uploaded !</strong>";
                              $("#warning").show();
                              $("#warning").hide(8000);
                              $("#warning").attr("class","alert alert-warning");
                              
                          
                    $("#select_img").attr("disabled","");
                    $("#clear").attr("disabled","");  
                    $("#upload").attr("disabled",""); 
                    }
    
    
                }
            function BytesToKiloBytes(size)
            {
                    return Math.round(size/1024);
                        }
            function fileSelectHandler() {

                    // get selected file
                    var oFile = $('#select_img')[0].files[0];



                    // check for image type (jpg and png are allowed)
                    var rFilter = /^(image\/jpeg|image\/png)$/i;
                    if (! rFilter.test(oFile.type)) {
                        alert('Please select a valid image file (jpg and png are allowed)');
                        imgClear();
                        return 0;
                    }
                    // check for file size
                    if (oFile.size > 550 * 1024) {//not greater than 550 KB
                        //size in bytes

                        var yourSize=BytesToKiloBytes(oFile.size);
                        alert('Your file size is '+yourSize+'kB.\n Please select a file smaller than 250 kB !');
                        imgClear();
                        return 0;
                    }
                    return 1;
            }

            function imgClear(){
                        $("#img").attr("src","/images/user.png");
                        $("#img").attr("width","160");
                        $("#select_img").val("");

            }
            
            function containsNum(jqcomp){
                        var l=$(jqcomp).val().length;
                        var a=0;
                        var count=0;
                        while(a<l)
                        {

                            var t=$(jqcomp).val().charAt(a);
                            if(!isNaN(t))
                            {
                                count++;

                            }
                            a++;
                        }
                        if((count!==l)&&(count>0))
                        {
                            return 1;
                        }
                        else
                        {
                            return 0;
                        }



                    }
            
    function checkSpecialChar(str){
    var filter=/^\s*[a-zA-Z0-9,\s]+\s*$/;
    if (filter.test(str))
    {
        //nsp
        return 0;
    }
    else
    {
        //sp
        return 1;
    }
}
    
    
            function readURL(input) {
    
            if(fileSelectHandler()===1){
            
            if (input.files && input.files[0]) {
                        var reader = new FileReader();

                        reader.onload = function (e) {
                            $('#img')
                                .attr('src', e.target.result)
                                .width(120)
                                .height(160);
                        };
                          
                        reader.readAsDataURL(input.files[0]);
                        
                    
            }
            
            
           }
            
        }
        $(document).ready(function(){
                 //autocomplete
			$("#lang").autocomplete({
                            
				source: "getLang.php",
				minLength: 1
                                
			});
           });
           $(document).ready(function(){
                 //autocomplete
			$("#place_ob").autocomplete({
                            
				source: "getCountry.php",
				minLength: 1
                                
			});
           });
             $(document).ready(function(){
                 //autocomplete
			$("#place_cc").autocomplete({
                            
				source: "getCountry.php",
				minLength: 1
                                
			});
           });
            $(document).ready(function(){
                 //autocomplete
			$("#place_ht").autocomplete({
                            
				source: "getCountry.php",
				minLength: 1
                                
			});
           });
           $(document).ready(function(){
               $("#alt_name").focusout(function(){
                    $("#alt_name").val( $("#alt_name").val().trim().toLowerCase());
               });
                   
           });
                        $(function() {
                $('#profile').on('reset', function() {

                   location.reload();

                });
           });
           
 //alt_name focus out
$(document).ready(function(){
    $("#alt_name").focusout(function(){
        $("#alt_name").val($("#alt_name").val().trim());
         if($("#alt_name").val().length>90)
        {
            $("#warning").show();
            document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> Profile name must be of maximum 90 characters.";
            $("#alt_name").val("");
        }
        else
        {
            $("#warning").hide();
             document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> Profile name must be of maximum 90 characters.";
        }
    });
});

//mob3 focusout
$(document).ready(function(){                    
    $("#mob3").focusout(function(){
        $("#mob3").val($("#mob3").val().trim());
        if((isNaN($("#mob3").val()))||($("#mob3").val().length!==12))
        {
          
           $("#warning").show().hide(3250);
           document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> Invalid mobile number.";
           
           $("#mob3").val('');
        }
        else{
            
             $("#warning").hide();
             document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> Invalid mobile number.";
              
        }
    });
});

//mob2 focusout
$(document).ready(function(){                    
    $("#mob2").focusout(function(){
        $("#mob2").val($("#mob2").val().trim());
        if((isNaN($("#mob2").val()))||($("#mob2").val().length!==12))
        {
          
           $("#warning").show().hide(3250);
           document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> Invalid mobile number.";
           
           $("#mob2").val('');
        }
        else{
            
             $("#warning").hide();
             document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> Invalid mobile number.";
              
        }
    });
});
//pl_ob focus out
$(document).ready(function(){
$("#place_ob").focusout(function(){
    $("#place_ob").val(capitalizeMe($("#place_ob").val().trim()));
    if((checkSpecialChar("#place_cc")===1))
    {
        $("#warning").show().hide(3250);
        document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> No special characters allowed here.";
        
    }
    else
    {
        $("#warning").hide();
    }
});
});
//place_cc focus out
$(document).ready(function(){
$("#place_cc").focusout(function(){
    $("#place_cc").val(capitalizeMe($("#place_cc").val().trim()));
    if((checkSpecialChar("#place_cc")===1))
    {
        $("#warning").show().hide(3250);
        document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> No special characters allowed here.";
        
    }
    else
    {
        $("#warning").hide();
    }
});
});


function containsNum(jqcomp){
    var l=$(jqcomp).val().length;
    var a=0;
    var count=0;
    while(a<l)
    {
      
        var t=$(jqcomp).val().charAt(a);
        if(!isNaN(t))
        {
            count++;
            
        }
        a++;
    }
    if((count!==l)&&(count>0))
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
    
    
}

//place_ht focus out
$(document).ready(function(){
$("#place_ht").focusout(function(){
    $("#place_ht").val(capitalizeMe($("#place_ht").val().trim()));
    if((checkSpecialChar("#place_ht")===1))
    {
        $("#warning").show().hide(3250);
        $("#place_ht").val("");
        document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> No special characters allowed here.";
        
    }
    else
    {
        $("#warning").hide();
    }
});
});


//lang focus out
$(document).ready(function(){
$("#lang").focusout(function(){
    $("#lang").val(capitalizeMe($("#lang").val().trim()));
    if((checkSpecialChar("#lang")===1))
    {
        $("#warning").show().hide(3250);
        $("#lang").val("");
        document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> No special characters allowed here.";
        
    }
    else
    {
        $("#warning").hide();
    }
});
});


//website focus out
$(document).ready(function(){
$("#website").focusout(function(){
    $("#website").val($("#website").val().trim().toLowerCase());
    
    if(($("#website").val().length)>48)
    {
        
        $("#warning").show().hide(3250);
        document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> Website name must not be greater than 48 characters.";
    }
    else
    {
        $("#warning").hide();
        
    }
});
});

//about_you focus out
$(document).ready(function(){
$("#about_you").focusout(function(){
    if(($("#about_you").val().length)>500)
    {
        
         $("#warning").show().hide(3250);
        document.getElementById("warning").innerHTML="<strong>Oh Snap !</strong> Maximum 500 characters are supported.";
    }
    else
    {
        
        $("#warning").hide();
    }
});
});
         </script>  
        <script type="text/javascript"  src="/js/hoverText.js"></script>
        
    </head>
    <body id="body">
        
        <div id="top">
                
            </div>
        
        <form name="profile" method="POST" enctype="multipart/form-data" action="update_profile.php" id="profile">
            <div class="row">
            <div id="left" class="col-md-10">
                <div class="alert alert-danger" id="warning"><strong>Oh Snap !</strong> This website works on JavaScript ! Please enable it !</div> 
            <label id="big_head">Complete your Profile</label>
            
            <br/>
            <br/>
            
            <label class="head">Profile Information</label>
           
            <br/>
            <br/>
            <div class="form-inline">
                
            <label id="lusername" class="flabels">Username</label>
            <input class="fields form-control  " type="text" autocomplete="off" disabled="" id="username" placeholder="Enter your User Name" name="username"/>
            
            
            
            <label id="lalt_name" class="flabels">Profile Name</label>
            <input class="fields form-control" id="alt_name" name="alt_name" placeholder="Enter your Profile Name" type="text" autocomplete="off">
            <br/><br/>
            
            </div>
            
            <div class="form-inline">
            
            <label id="lmob1" class="flabels">Registered Mobile Number</label>
            <input class="fields form-control" id="mob1" name="mob1" type="text" placeholder="Enter your mobile number" autocomplete="off" disabled="">
            
            
            <label id="lemail" class="flabels">Registered email address</label>
            <input class="fields form-control" id="email" name="email" type="text" placeholder="Enter your email addres" autocomplete="off" disabled="">
            
            
        
            </div>
            <br/>
            <br/>
            <label class="head">Basic Information</label><br/>
            <br/>
            <br/>
            <div class="form-inline">
            <label id="lfname" class="flabels">First Name</label>
            <input class="fields form-control" placeholder="Enter your First Name" type="text" autocomplete="off" disabled="" name="fname" id="fname">
            
            <label id="llname" class="flabels">Last Name</label>
            <input class="fields form-control" type="text" placeholder="Enter your Last Name" autocomplete="off" disabled="" name="lname" id="lname">
            <br/><br/>
            </div>
            
            <div class="form-inline">
            <label id="lsex" class="flabels">Sex</label>
            <input class="fields form-control" type="text" autocomplete="off" disabled="" name="sex" id="sex">
            
            <label id="ldob" class="flabels" >Date of Birth</label>
            <input class="fields form-control" placeholder="Enter your dob" type="text" autocomplete="off" disabled="" name="dob" id="dob">
            <br/><br/>  
            
            </div>
            
            <div class="form-inline">
            <label id="linterestedin" class="flabels">Interested In</label>
           
            <select name="interestedin" class="form-control"> 
                <option selected="" value="Not Interested">Not Interested</option>
                <option value="Men">Men</option>
                <option value="Women">Women</option>
                <option value="Both">Both</option>
            </select>
            
            </div>
            
            <br/>
            <br/>
            <label class="head">Contact Information</label>
            <br/>
            <br/>
            
            
            <div class="form-inline">
            <label id="lmob2" class="flabels">Mobile number 1</label>
            <input class="fields form-control" id="mob2" name="mob2" placeholder="Enter your mobile number" type="text" autocomplete="off">
            
            <label id="lmob3" class="flabels">Mobile number 2</label>
            <input class="fields form-control" id="mob3" name="mob3" placeholder="Enter your mobile number" type="text" autocomplete="off">
            <br/><br/>
            </div>
            
            <div class="form-inline">
            <label id="lwebsite" class="flabels">Website/Blog you administer</label>
            <input class="fields form-control" id="website" name="website" placeholder="Enter your website's or blog's url" type="text" autocomplete="on">
            </div>
            <br/><br/>
            
            <br/>
            
            <label class="head">Additional Information</label>
            <br/>
            <br/>
            
            
            <label id="lplace_ob" class="flabels">Place of Birth</label><br/>
            <div class="form-inline">
            
                <input type="text" name="place_ob" placeholder="Place of Birth"  class="fields form-control" autocomplete="off"   id="place_ob" />
            </div>
            <br/>
            <br/>
            
            
            <label id="lplace_cc" class="flabels">Current City</label><br/><br/>
            <div class="form-inline">
            
                <input type="text" name="place_cc"  class="fields form-control select" placeholder="Current City"   id="place_cc" />
           
            <br/>
            </div>
           
            
            <br/><br/>
            <label id="lplace_ht" class="flabels">Home Town</label><br/><br/>
            <input type="text" autocomplete="off" placeholder="Home Town" name="place_ht" class="fields form-control select"   id="place_ht" />
            <br/><br/>
           
            <label id="labout_you" class="flabels">About You</label><br/>
            <textarea placeholder="About You" name="about_you" maxlength="500" rows="5" cols="60" id="about_you">
                

            </textarea>
            
            
            <br/>
            <br/>
            
            <label id="llang" class="flabels">Languages you speak</label>
            <br/><br/>
            
            <input type="text" name="lang" id="lang" placeholder="Languages you speak" class="fields form-control" autocomplete="off" /><br/><br/>
            
            <label id="lreligion" class="flabels">Religion you follow</label>
            <select name="religion" id="religion" class="fields form-control">
                <option value="Christianity">Christianity</option>
                <option value="Islam">Islam</option>
                <option value="Secular">Secular</option>
                <option value="Nonreligious">Nonreligious</option>
                <option value="Agnostic">Agnostic</option>
                <option value="Atheist">Atheist</option>
                <option value="Hinduism">Hinduism</option>
                <option value="Buddhism">Buddhism</option>
                <option value="Sikhism">Sikhism</option>
                <option value="Juche">Juche</option>
                <option value="Spiritism">Spiritism</option>
                <option value="Judaism">Judaism</option>
                <option value="Baha'i">Baha'i</option>
                <option value="Jainism">Jainism</option>
                <option value="Shinto">Shinto</option>
                <option value="Cao Dai">Cao Dai</option>
                <option value="Zoroastrianism">Zoroastrianism</option>
                <option value="Tenrikyo">Tenrikyo</option>
                <option value="Neo-Paganism">Neo-Paganism</option>
                <option value="Unitarian Universalism">Unitarian Universalism</option>
                <option value="Scientology">Scientology</option>
            </select>
            
            <br/>
            <br/>
            
            
            
            </div>
            <div id="upload_img2" class="col-md-2">
                <center>
                <label id="lprofile_pic" class="flabels">Profile Picture</label><br/><br/>
                 <img id="img" alt="Went missing Right!" src="/images/user.png" width="180" height="160"><br/>        
                <br/>
                <br/>
                 <input type="file" class="btn btn-default" onchange="readURL(this);" accept="image/*" id="select_img"  name="select_img"><br/>
                 <input type="button" class="btn btn-default" name="upload" id="upload" onclick="imgSubmit();" value="Upload">
                <input type="button" class="btn btn-default" id="clear" onclick="imgClear();" value="Clear"><br/><br/>
                <br/><br/>
                <input type="submit" class="btn btn-default" value="Update my profile"/><br/><br/>
                 <input type="reset" class=" btn btn-default"/>
                </center>
                
                </div>
            </div>
            
                <div id="bottom" class="row">
            
                </div>
            
        </form>
        
        
    </body>
</html>
