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
        
         <script type="text/javascript" src="js/jQuery.js"></script>
         <script type="text/javascript" src="js/hoverText.js"></script>
         <link type="text/css" href="css/index.css" rel="stylesheet"/>
         <script type="text/javascript">
             $(document).ready(function(){
                 
                 $("#warning").hide();
         
                 $("#body").show();
                
             });
             function capLock(e){
             kc = e.keyCode?e.keyCode:e.which;
             sk = e.shiftKey?e.shiftKey:((kc == 16)?true:false);
             if(((kc >= 65 && kc <= 90) && !sk)||((kc >= 97 && kc <= 122) && sk)){
                 $("#warning").show();
              document.getElementById('warning').innerHTML="Caps Lock <strong>On</strong>";
          }
          else
          {
              $("#warning").hide();
              
          }
             }
             function validateForm(){
                 if(($("#uname").val()==="")||($("#uname").val()==="Enter your User Name,Mobile Number or email address")){
                    document.getElementById("warning").innerHTML="<strong>Oh!</strong> Username cannot be left blank.";         
                    $("#warning").show().hide(10000);
                    
                     return false;
                 }
                 else if(($("#pswd").val()==="")||($("#pswd").val()==="Enter your Password"))
                 {
                     document.getElementById("warning").innerHTML="<strong>Oh!</strong> Password cannot be left blank."; 
                     $("#warning").show().hide(10000);
                    
                     return false;
                 }
                 else{
                      $("#warning").hide();
                    
                   
                     return true;
                 }
             }
              
         $(document).ready(function(){
             hoverText("#uname","Enter your User Name,Mobile Number or email address");
             hoverText("#pswd","Enter your Password");
             
           });
           //foscus out of uname
           $(document).ready(function(){
               $("#uname").focusout(function(){
                   
                   if($("#uname").val().length>25)
                   {
                       $("#uname").val('');
                      $("#warning").show().hide(10000);
                      document.getElementById("warning").innerHTML="<strong>Oh!</strong> Username must be max 25 characters in length.";
                   }
                   else
                   {
                       $("#warning").hide(); 
                        document.getElementById("warning").innerHTML="<strong>Oh!</strong> Username must be max 25 characters in length.";
                   }
               });
           });  
           //focus out of pswd
            $(document).ready(function(){                    
                $("#pswd").focusout(function(){

                    if((($("#pswd").val().length)>=8)&&(containsNum("#pswd")===1))
                    {

                       $("#warning").hide();
                        document.getElementById("warning").innerHTML="<strong>Oh!</strong> Password format is wrong!";
                       
                    }
                    else{
                         $("#pswd").val('');
                         $("#warning").show().hide(10000);
                         document.getElementById("warning").innerHTML="<strong>Oh!</strong> Password format is wrong!";
                        
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
 $(function() {
     $('#login').submit( function() {
        
         return validateForm();
         
     });
});

$(document).ready(function(){
    $("#chk").change(function(){
       
        if($("#chk").val()==="0")
        {
            $("#chk").val("1");
           
        }
        else if($("#chk").val()==="1")
        {
            $("#chk").val("0");
            
        }
        
    });
});
           
           </script>
           
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.min.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.min.css" rel="stylesheet" media="screen">
       
    </head>
    <body  id="body" >
      
        
        <div class="alert alert-danger" id="warning"><strong>Oh Snap !</strong> This website works on JavaScript ! Please enable it !</div> 
        <div id="top" class="row">
        
        
        
        </div>
        <div class="row" id="middle">
        <form name="login" id="login" action="php/auth.php" method="POST">
            <center>
                <div class="form-inline"> 
                <label id="luname" class="flabels"> User Name </label>
                <input id="uname" class="fields form-control" type="text" name="uname" />
             <br/>
                </div>
                <div class="form-inline"> 
            <label id="lpswd" class="flabels"> Password  </label>
            <input id="pswd" autocomplete="off" class="fields form-control" onkeypress="capLock(event)" type="password" name="pswd"/>
            <br/><br/>
            <input type="checkbox" id="chk" value="0" name="chk"/><label style="font-weight:600;">Keep signed in</label>
            
            <br/>
            <input type="submit" class="flabels btn btn-success"   id="submit"  name="submit" value="Log In"/><br/>
                </div>
            </center> 
            <br/>
            
                <center>
            <a href="">Trouble logging in !</a><br/>
            Not a user yet?
            <a href="register.html" class="fields">Join Now!</a>
            </center>
            
                            
            
        </form>
      
        </div>
        <div class="row" id="bottom"></div>
       
    </body>
</html>
  
        