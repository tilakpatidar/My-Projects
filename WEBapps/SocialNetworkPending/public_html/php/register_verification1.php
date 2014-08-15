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
      
        <script type="text/javascript" src="/js/jQuery.js"></script>
        <script type="text/javascript" src="/js/hoverText.js"></script>
         <link type="text/css" href="/css/register.css" rel="stylesheet"/>
        <script type="text/javascript">
            function validateEmail(sEmail) {
    var filter = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    if (filter.test(sEmail)) {
       
        return 1;
    }
    else {
         
        return 0;
    }
}
             $(document).ready(function(){
                hoverText("#code","Enter verification code");
                hoverText("#email","Enter your email address");
            });
            
            //code focus out
            $(document).ready(function(){
                $("#code").focusout(function(){
                    $("#code").val($("#code").val().trim());
                    if($("#code").val().length!==5)
                    {
                        $("#code").val("");
                        $("#scode").attr("class","visible");
                        document.getElementById("scode").innerHTML="Verification code must be 5 digit";
                       $("#submit").attr("disabled","");
                    }
                    else if(isNaN($("#code").val())){
                        $("#code").val("");
                       $("#scode").attr("class","visible");
                       document.getElementById("scode").innerHTML="Verification code must be 5 digit";
                        $("#submit").attr("disabled","");
                    }
                    else{
                        $("#scode").attr("class","hidden");
                        document.getElementById("scode").innerHTML="Verification code must be 5 digit";
                        $("#submit").removeAttr("disabled"); 
                    }
                });
            });
            
            //email focus out
            $(document).ready(function(){
                $("#email").focusout(function(){
                    if(validateEmail($("#email").val())===1)
                    {
                        $("#semail").attr("class","hidden");
                        document.getElementById("semail").innerHTML="Invalid email address";
                        ("#submit").removeAttr("disabled");
                    }
                    else if(validateEmail($("#email").val())===0)
                    {
                        $("#email").val("");
                        $("#semail").attr("class","visible");
                         document.getElementById("semail").innerHTML="Invalid email address";
                         $("#submit").attr("disabled","");
                    }
                    
                });
            });
        </script>
    </head>
    
    
    <body>
     
        <form name="verify" id="verify" action="/php/register_verification2.php" method="POST">
            <label id="lemail">Enter your email address :</label>
            <input type="text" name="email" autocomplete="off" id="email"/><label class="hidden" id="semail"></label>
            <br/>
            <label id="l1">Enter your 5 digit verification code :</label>
            <input type="text" name="code" autocomplete="off" id="code"/><label class="hidden" id="scode"></label>
            <br/>
            <input type="submit" disabled id="submit" value="Verify my email address"/>
            <input type="reset" id="reset" value="Clear"/>
        </form>
    </body>
</html>
