/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

             $(document).ready(function(){
                 
                 $("#warning").hide();
         
                 $("#body").show();
                
             });
		$(document).ready(function(){
                 //autocomplete
			$("#search").autocomplete({
                            
				source: "/php/getSearch.php",
				minLength: 1,
                                maxHeight:400,
                                html:true,
                                 focus: function (event, ui) {
        event.preventDefault(); // <-- prevent the textarea from being updated.
    },
                                select:function (e, ui) {
                                    
                            if(ui.item.value==="<center><div style='color:#0044cc;text-decoration:underline;font-size:small;'>Search using filters</div></center>")
                            {
                                ui.item.value="";
                                window.location="memberSearch.html";
                            }
                            else
                            {
                                var arr=ui.item.value.split(">");
                                
                                ui.item.value=arr[0].slice(2,(arr[0].length));
                                 window.location="cgi-bin/viewProfile.py?username="+ui.item.value;
                            }
                           
                        }
                               
                               

                        });
                        
                               
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
           
          

