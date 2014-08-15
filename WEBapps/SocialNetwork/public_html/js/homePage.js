/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

             $(document).ready(function(){
                 
                 $("#warning").hide();
         
                 $("#body").show();
                 $("#academic").hide();
                 $("#contact").hide();
                //Caused error with search autocomplete $(".dropdown-toggle").dropdown();
                
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
                                 window.location="viewProfile.py?username="+ui.item.value;
                            }
                           
                        }
                               
                               

                        });
                        
                               
			});
        
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
     $('#srch').submit( function() {
        
         return validateForm();
         
     });
});


function profileShow(){
    $("#profile").show();
    $("#profileItem").attr("class","active");
    $("#academicItem,#contactItem").attr("class","");
    $("#academic,#contact").hide();
}
function academicShow(){
    $("#academic").show();
    $("#academicItem").attr("class","active");
    $("#profileItem,#contactItem").attr("class","");
    $("#profile,#contact").hide();
}
function contactShow(){
    $("#contact").show();
    $("#contactItem").attr("class","active");
    $("#profileItem,#academicItem").attr("class","");
    $("#profile,#academic").hide();
}

