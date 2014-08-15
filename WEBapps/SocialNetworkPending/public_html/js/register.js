/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
var own_q=0;
function containsChar(val)
{
    var filter=/.*[a-zA-Z]+.*/;
    if(filter.test(val))
    {
        //contains char
        return 1;
    }
    else
    {
        return 0;
        //only num
    }
}
function capitalizeMe(val){
    return val.charAt(0).toUpperCase()+val.substr(1).toLowerCase();
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

function visibleAns()
{
    $("#lsec_a").show();
    $("#sec_a").show();
    $("#bsec_q").hide();
}
function createQues(){
   
    //max 100 limit
    
   
   $("#sec_q").remove();
    $("#bsec_q").remove();
    $("#sec_q2").show();
    own_q=1;
}
function validateForm(){
    
   if(($("#fname").val()==="")||($("#fname").val()==="Enter your First Name")){
       $("#warning").show().hide(5000);
        document.getElementById("warning").innerHTML="<strong>Oh!</strong> First Name required !";
        return false;
       
   }
   else if(($("#lname").val()==="")||($("#lname").val()==="Enter your Last Name"))
   {
       $("#warning").show().hide(5000);
         document.getElementById("warning").innerHTML="<strong>Oh!</strong> Last Name required !";
        return false;
   }
   else if(($("#dob").val()==="")||($("#dob").val()==="dd-mm-yyyy")){
   $("#warning").show().hide(5000);
     document.getElementById("warning").innerHTML="<strong>Oh!</strong> Date of Birth required !";
        return false;
    }
   else if(($("#email").val()==="")||($("#email").val()==="Enter your email address")){
       $("#warning").show().hide(5000);
         document.getElementById("warning").innerHTML="<strong>Oh!</strong> Email address required !";
        return false;
   }
    else if(($("#mob").val()==="")||($("#mob").val()==="Enter your registered mobile number")){
       $("#warning").show().hide(5000);
       document.getElementById("warning").innerHTML="<strong>Oh!</strong> Mobile number required !";
        return false;
   }
   else if(($("#username").val()==="")||($("#username").val()==="Enter your User Name")){
       $("#warning").show().hide(5000);
       document.getElementById("warning").innerHTML="<strong>Oh!</strong> Username required !";
        return false;
   }
    else if(($("#alt_name").val()==="")||($("#alt_name").val()==="Enter your Profile Name")){
       $("#warning").show().hide(5000);
       document.getElementById("warning").innerHTML="<strong>Oh!</strong> Profile Name required !";
        return false;
   }
   else if(($("#pswd1").val()==="")||($("#pswd1").val()==="Enter your password")){
     $("#warning").show().hide(5000);
     document.getElementById("warning").innerHTML="<strong>Oh!</strong> Password required !";
        return false;
    }
   else if(($("#pswd2").val()==="")){
       $("#warning").show().hide(5000);
       document.getElementById("warning").innerHTML="<strong>Oh!</strong> Confirm Password required !";
        return false;
   }
   else if(($("#sec_a").val()==="")||($("#sec_a").val()==="Enter your Answer")){
     $("#warning").show().hide(5000);
      document.getElementById("warning").innerHTML="<strong>Oh!</strong> Security Answer required !";
       
        return false;  
    }
    else if(($("#sec_q2").val()==="")&&(own_q===1)){
     $("#warning").show().hide(5000);
      document.getElementById("warning").innerHTML="<strong>Oh!</strong> Security Question required !";
       
        return false;  
    }
   else
   {
       $("#warning").hide();
       return true;
   }
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
function validateEmail(sEmail) {
    var filter = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    if (filter.test(sEmail)) {
       
        return 1;
    }
    else {
         
        return 0;
    }
}
//fname focus out
//fnmae must be 45
$(document).ready(function(){                    
    $("#fname").focusout(function(){
       
       $('#fname').val($('#fname').val().trim());
       $('#fname').val(capitalizeMe($('#fname').val()));
      //  checkSpecialChar( $('#fname').val());
      // $("#fname").attr("value",trim);
       
        if(((checkSpecialChar( $('#fname').val())===1)||(($("#fname").val().length)>45))||((containsNum("#fname")===1)||(!isNaN($('#fname').val()))))
        {
            $("#warning").show().hide(5000);
            document.getElementById("warning").innerHTML="First Name must not contain[0-9][!-)]";
            $('#fname').val('');
        }
       
        else{
              $("#warning").hide();
              document.getElementById("warning").innerHTML="First Name must not contain[0-9][!-)]";
        }
    });
});
//lname focus out
//lname must be  45 char
$(document).ready(function(){                    
    $("#lname").focusout(function(){
        $('#lname').val($('#lname').val().trim());
        $('#lname').val(capitalizeMe($('#lname').val()));
         if(((checkSpecialChar( $('#lname').val())===1)||(($("#lname").val().length)>45))||((containsNum("#lname")===1)||(!isNaN($('#lname').val()))))
        {
            $("#warning").show().hide(5000);
             document.getElementById("warning").innerHTML="Last Name must not contain[0-9][!-)]";
            $('#lname').val('');
        }
        
        else{
              $("#warning").hide();
              document.getElementById("warning").innerHTML="Last Name must not contain[0-9][!-)]";
        }
    });
});
//email focusout
$(document).ready(function(){                    
    $("#email").focusout(function(){
        $('#email').val($('#email').val().trim());
        $('#email').val($('#email').val().toLowerCase());
        var email= $('#email').val().toString();
        if(($("#pswd1").val()===$("#email").val())&&($("#email").val()!==""))
        {
            $("#warning").show().hide(5000);
           
            document.getElementById("warning").innerHTML="Password must not be same as username or email.";
            $("#pswd1").val("");
            $("#pswd2").val("");
            $("#email").val("");
        }
         else if(validateEmail(email)===0){
            $('#email').val('');
             $("#warning").show().hide(5000);
             document.getElementById("warning").innerHTML="Please enter a valid email address !";
        }
        else
        {
            $("#warning").hide();
            document.getElementById("warning").innerHTML="Please enter a valid email address !";
        }
        
    });
});
$(document).ready(function(){
    $("#chkbox").click(function(){
        if($("#chkbox").val()==="false")
        {
            //checked
            $("#chkbox").val("true");
            $("#submit").removeAttr("disabled");
        }
        else if($("#chkbox").val()==="true")
        {
            $("#chkbox").val("false");
            $("#submit").attr("disabled","");
        }
    });
});

//pswd1 focusout
$(document).ready(function(){                    
    $("#pswd1").focusout(function(){
         if((($("#pswd1").val()===$("#username").val()))&&($("#pswd1").val()!==""))
        {
            $("#warning").show().hide(5000);
           
            document.getElementById("warning").innerHTML="Password must not be same as username or email.";
            $("#pswd1").val("");
            $("#pswd2").val("");
            $("#username").val("");
        
        }
        else if((($("#pswd1").val()===$("#email").val()))&&($("#pswd1").val()!==""))
        {
            $("#warning").show().hide(5000);
           
            document.getElementById("warning").innerHTML="Password must not be same as username or email.";
            $("#pswd1").val("");
            $("#pswd2").val("");
            $("#email").val("");
        }
        else if((($("#pswd1").val().length)>=8)&&(containsNum("#pswd1")===1))
        {
          //fav cond
           $("#warning").hide();
           
           document.getElementById("warning").innerHTML="Password must be alpha-numeral and minimum 8 characters in length.";
           $("#pswd2").removeAttr("disabled");
           //$("#pswd2").val('');
           if($("#pswd1").val().toString()!==$("#pswd2").val().toString())
                     {
                         document.getElementById("warning").innerHTML="Passwords do not match !";
                        
                         $("#pswd2").val("");
                     }
           $("#pswd2").focus();
                        
        }
        
        else{
             $("#pswd1").val('');
             $("#warning").show().hide(5000);
              document.getElementById("warning").innerHTML="Password must be alpha-numeral and minimum 8 characters in length.";
              
        }
    });
});
//mob focusout
$(document).ready(function(){                    
    $("#mob").focusout(function(){
        $("#mob").val($("#mob").val().trim());
        if((isNaN($("#mob").val()))||($("#mob").val().length!==12))
        {
          
           $("#warning").show().hide(5000);
           document.getElementById("warning").innerHTML="Invalid mobile number.";
           
           $("#mob").val('');
        }
        else{
            
             $("#warning").hide();
             document.getElementById("warning").innerHTML="Invalid mobile number.";
              
        }
    });
});
//sec_ans focusout
$(document).ready(function(){                    
    $("#sec_a").focusout(function(){
        $("#sec_a").val($("#sec_a").val().trim());
          $('#sec_a').val($('#sec_a').val().toLowerCase());
        if($("#sec_a").val().length>30)
        {
          $("#sec_a").val('');
          $("#warning").show().hide(5000);
          document.getElementById("warning").innerHTML="Not more than 30 characters.";
           
        }
        else{
             $("#warning").hide();
              document.getElementById("warning").innerHTML="Not more than 30 characters.";
        }
    });
});
//PSWD2 focusout
$(document).ready(function(){                    
    $("#pswd2").focusout(function(){
        if($("#pswd1").val()===""){
             document.getElementById("warning").innerHTML="Please enter the password first !";
             $("#pswd2").val("");
            $("#warning").show().hide(5000);
        }
        else if($("#pswd2").val()===$("#pswd1").val())
        {
         //pswd matched
            document.getElementById("warning").innerHTML="Passwords matched successfully !";
           $("#warning").attr("class","alert alert-success");
            $("#warning").show().hide(5000);
            $("#warning").attr("class","alert alert-danger");
           
        }
        else{
            $("#pswd1").val('');
            $("#pswd2").val('');
            document.getElementById("warning").innerHTML="Passwords do not match !";
            
            $("#warning").show().hide(5000);
             //pswd do not match
        }
    });
});
//sec_q2 focus out
$(document).ready(function(){                    
    $("#sec_q2").focusout(function(){
        $("#sec_q2").val($("#sec_q2").val().trim());
        $('#sec_q2').val($('#sec_q2').val().toLowerCase());
       if($("#sec_q2").val().length>60)
        {
           
          
           $("#warning").show().hide(5000);
           document.getElementById("warning").innerHTML="Maximum 60 characters allowed!";
           $("#sec_q2").val("");
            
           
        }
        else if($("#sec_q2").val()==="")
        {
            $("#warning").show().hide(5000);
           document.getElementById("warning").innerHTML="Cannot leave security question empty!"; 
        }
        else{
            
          
            $("#warning").hide();
           
        }
    });
});

//alt_name focus out
$(document).ready(function(){
    $("#alt_name").focusout(function(){
        $("#alt_name").val($("#alt_name").val().trim());
         if($("#alt_name").val().length>90)
        {
            $("#warning").show().hide(5000);
            document.getElementById("warning").innerHTML="Profile name must be of maximum 90 characters.";
            $("#alt_name").val("");
        }
        else
        {
            $("#warning").hide();
             document.getElementById("warning").innerHTML="Profile name must be of maximum 90 characters.";
        }
    });
});
//username focus out
$(document).ready(function(){
    
    $("#username").focusout(function(){
        $("#username").val($("#username").val().trim());
        $('#username').val($('#username').val().toLowerCase());
        if($("#username").val()==="")
        {
            $("#warning").hide();
        }
        else if(($("#pswd1").val()===$("#username").val()))
        {
            $("#warning").show().hide(5000);
           
            document.getElementById("warning").innerHTML="Password must not be same as username or email.";
            $("#pswd1").val("");
            $("#pswd2").val("");
            $("#username").val("");
        
        }
        else if(containsChar($("#username").val())===0)
        {
            $("#username").val("");
            $("#warning").show().hide(5000);
            document.getElementById("warning").innerHTML="Username must contain atleast one character.";
        }
        
        else if(($("#username").val()!=="Enter your User Name")&&($("#username").val()!==""))
        {
        $("#warning").hide();
                        if (window.XMLHttpRequest)
                            {// code for IE7+, Firefox, Chrome, Opera, Safari
                            xmlhttp=new XMLHttpRequest();
                            
                            }
                        else
                          {// code for IE6, IE5
                          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
                          }
                          
                          xmlhttp.onreadystatechange=function()
                            {
                            if (xmlhttp.readyState===4 && xmlhttp.status===200)
                              {
                                  
                             
                             document.getElementById("warning").innerHTML="<strong>"+xmlhttp.responseText+"</strong>";
                             if(document.getElementById("warning").innerHTML==="<strong>Not Available</strong>")
                            {
                                $("#warning").attr("class","alert alert-danger");
                                $("#warning").show().hide(5000);
                                 
                                $("#username").val("");
                            }
                            else if(document.getElementById("warning").innerHTML==="<strong>Available</strong>")
                            {
                                $("#warning").attr("class","alert alert-success");
                                $("#warning").show().hide(5000,function(){
                                   $("#warning").attr("class","alert alert-danger");
                                });
                            }
                              }
                             };
                            var str=$("#username").val();
                          xmlhttp.open("GET","php/getAvail.php?username="+str,true);
                          xmlhttp.send();
                          
                           
        }   
      
        });
         });
 
  $(function() {
     $('#register').on('submit', function() {
        
         return validateForm();
         
     });
});


  $(function() {
     $('#register').on('reset', function() {
        
         
         
     });
});
    
    
    

