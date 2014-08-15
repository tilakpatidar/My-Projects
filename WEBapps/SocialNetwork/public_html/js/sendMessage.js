/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
var new_msgs;
 var intervalId = setInterval(function() {
     if($("#contact_selected").html()!==""){
     var msg_from=window.location.toString().split("=");
                                  var msg_from=msg_from[1];
    refreshMessages(msg_from);
}
}, 1000);
function refreshMessages(msg_from){
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
                              
                            
                             
                             
                              }
                             };
                           
                                  
                                 
                                   
                          xmlhttp.open("GET","msgRefresh.py?msg_from="+msg_from,false);
                          xmlhttp.send();
                          
                          var new_msgs=xmlhttp.responseText.toString();
                          $("#msgs").html(new_msgs);
}
function reply(){
    
         
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
                              
                            
                             
                             
                              }
                             };
                           
                                  
                                  var msg_to=window.location.toString().split("=");
                                  var msg_to=msg_to[1];
                                 var msg=$("#msg").val();
                                   
                          xmlhttp.open("GET","reply.py?"+"msg_to="+msg_to+"&msg="+msg,false);
                          xmlhttp.send();
                          
                          var new_msgs=xmlhttp.responseText.toString();
                          $("#msgs").html(new_msgs);
                                
                               
        
    }
$(document).ready(function(){
   
    
            
        
    $("#send").click(function(){
           $("#msg").val($("#msg").val().trim());
        if( $("#msg").val()===""){
            document.getElementById("warning").innerHTML="<strong>Oh!</strong> Cannot send empty messages!";         
                    $("#warning").show().hide(5000);
                    
        }
        else
        {
            reply();
        }
                      
    });
});

             $(document).ready(function(){
                 
                 $("#warning").hide();
         
                 $("#body").show();
                 
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
          $(document).ready(function(){
                 //autocomplete
			$("#add").autocomplete({
                            
				source: "/php/addContact.php",
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
                                 window.location="sendMessage.py?from="+ui.item.value;
                            }
                           
                        }
                               
                               

                        });
                        
                               
			});
          
        
          






