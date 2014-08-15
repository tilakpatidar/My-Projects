/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
function viewProfile(str){
   
    window.location="viewProfile.py?username="+str.toString();
}
             $(document).ready(function(){
                 $("#page").val("1");
             });
             var page=5;
            function prev(){
                var i=page-5;    
                 
                $("#pages").html("");
                for (j=0;j<5;j++)
                {
                    
                    var temp='<li><a href="javascript:$(\'#page\').val(\''+i+'\');$(\'#srch\').submit();">'+i+'</a></li>'+$("#pages").html();
                    $("#pages").html(temp);
                    i--;
                  
                     
                }
             
                
               // alert($("#pages").html());
                page=i+5;
                if(page===5)
                {
                     $("#pages").html("<li><a hidden href='javascript:prev();'>&laquo;</a></li>"+$("#pages").html()+"<li><a href='javascript:next();'>&raquo;</a></li></ul>");
                }
                else
                {
                     $("#pages").html("<li><a href='javascript:prev();'>&laquo;</a></li>"+$("#pages").html()+"<li><a href='javascript:next();'>&raquo;</a></li></ul>");
                }
                //alert(page);
                   
                
                 
             }
                
             function next(){
                var i=page;    
                  
                $("#pages").html("");
                for (j=0;j<5;j++)
                {
                    i++;
                    var temp=$("#pages").html()+'<li><a href="javascript:$(\'#page\').val(\''+i+'\');$(\'#srch\').submit();">'+i+'</a></li>';
                    $("#pages").html(temp);
                    
                  
                     
                }
                page=i;
                if(page===5)
                {
                     $("#pages").html("<li><a hidden href='javascript:prev();'>&laquo;</a></li>"+$("#pages").html()+"<li><a href='javascript:next();'>&raquo;</a></li></ul>");
                }
                else{
                 $("#pages").html("<li><a href='javascript:prev();'>&laquo;</a></li>"+$("#pages").html()+"<li><a href='javascript:next();'>&raquo;</a></li></ul>");
                }
               
            // alert(page);
                
              // alert($("#pages").html());
                
               
                
                 
             }
             // Array Remove - By John Resig (MIT Licensed)
                Array.prototype.remove = function(from, to) {
                  var rest = this.slice((to || from) + 1 || this.length);
                  this.length = from < 0 ? this.length + from : from;
                  return this.push.apply(this, rest);
                };
             var count=1;
             function isContainsValidSearchKey(key){
                var validKeys=['First Name ','Last Name ','Email Address ',' First Name ',' Last Name ',' Email Address ',' Vertical ','Vertical ',' Category ','Category ',' Year ','Year ',' Sex ','Sex '];
                 var l=validKeys.length;
                 var i=0;
                 while(i<l)
                 {
                     if(key===validKeys[i])
                     {
                         return 1;
                         break;
                     }
                     ++i;
                 }
                 return 0;
                 
             }
             function isValid(){
                 var str=$("#search").val().split(":");
                 var l=str.length;
                 
                 var i=0;
                 while(i<l)
                 {
                     if(isContainsValidSearchKey(str[i])===0)
                     {
                         
                         str.remove(i);
                         str.remove(i);
                         $("#search").val(str.toString().replace(",",":"));
                         $("#search").val($("#search").val().replace(",",":"));
                         $("#search").val($("#search").val().replace(",",":"));
                         $("#search").val($("#search").val().trim());
                     break;
                     }
                    i=i+2;//only odds
                 }
                 
             }
             function isRepeat(key){
                 
                 if($("#search").val().search(key)!==-1)
                 {
                   return 1;  
                 }
                    
                 return 0;
             }
             $(document).ready(function(){
                 
                 $("#warning").hide();
         
                 $("#body").show();
                
             });
             
             function validateForm(){
                 
                 if(($("#search").val()==="")){
                    document.getElementById("warning").innerHTML="<strong>Oh!</strong> Search cannot be left empty!.";         
                    $("#warning").show().hide(5000);
                    
                     return false;
                 }
                
                 else{
                      $("#warning").hide();
                    
                   
                     return true;
                 }
             }
              
              $(document).ready(function(){
                  $("#search").change(function(){
                      isValid();
                      if($("#search").val()==="")
                          count=1;
                  });
              });
            
            $(document).ready(function(){
                  $("#search").keypress(function(){
                      isValid();
                      if($("#search").val()==="")
                          count=1;
                  });
              });
            
            
            $(document).ready(function(){
                 //autocomplete
			$("#search").autocomplete({
                            
				source: "/php/getParms.php",
				minLength: 1,
                                maxHeight:400,
                                html:true,
                                  focus: function (event, ui) {
                                    event.preventDefault(); // <-- prevent the textarea from being updated.
                                },
                                select:function (e, ui) {
                                    
                           
                            
                                
                                if(count===1)
                                {
                                            var arr=ui.item.value.split(">");
                                            var col=arr[0].slice(2,(arr[0].length));
                                        if(col==="fname")
                                        {
                                                 
                                                     ui.item.value="First Name : ";
                                              
                                                 
                                        }
                                        else if(col==="lname")
                                        {
                                            
                                                 ui.item.value="Last Name : ";
                                        }
                                        else if(col==="email")
                                        {
                                                 ui.item.value="Email Address : ";
                                        }
                                        else if(col==="vertical")
                                        {
                                                 ui.item.value="Vertical : ";
                                        }
                                        else if(col==="category")
                                        {
                                                 ui.item.value="Category : ";
                                        }
                                        else if(col==="year")
                                        {
                                                 ui.item.value="Year : ";
                                        }
                                        else if(col==="sex")
                                        {
                                                 ui.item.value="Sex : ";
                                        }
                                        count=count+1;
                                }
                                else
                                {
                                             var arr=ui.item.value.split(">");
                                            var col=arr[0].slice(2,(arr[0].length));
                                        if(col==="fname")
                                        {
                                                if(isRepeat("First Name")===0)
                                                    ui.item.value=$("#search").val().concat(" : First Name : ");
                                                else
                                                    ui.item.value=$("#search").val().concat("");
                
                                        }
                                        else if(col==="lname")
                                        {
                                                  if(isRepeat("Last Name")===0)
                                                     ui.item.value=$("#search").val().concat(" : Last Name : ");
                                                 else
                                                     ui.item.value=$("#search").val().concat("");
                                                
                                        }
                                        else if(col==="email")
                                        {
                                                if(isRepeat("Email Address")===0)
                                                     ui.item.value=$("#search").val().concat(" : Email Address : ");
                                                 else
                                                     ui.item.value=$("#search").val().concat("");
                                                 
                                        }
                                         else if(col==="vertical")
                                        {
                                                if(isRepeat("Vertical")===0)
                                                     ui.item.value=$("#search").val().concat(" : Vertical : ");
                                                 else
                                                     ui.item.value=$("#search").val().concat("");
                                                 
                                        }
                                          else if(col==="category")
                                        {
                                                if(isRepeat("Category")===0)
                                                     ui.item.value=$("#search").val().concat(" : Category : ");
                                                 else
                                                     ui.item.value=$("#search").val().concat("");
                                                 
                                        }
                                          else if(col==="year")
                                        {
                                                if(isRepeat("Year")===0)
                                                     ui.item.value=$("#search").val().concat(" : Year : ");
                                                 else
                                                     ui.item.value=$("#search").val().concat("");
                                                 
                                        }
                                          else if(col==="sex")
                                        {
                                                if(isRepeat("Sex")===0)
                                                     ui.item.value=$("#search").val().concat(" : Sex : ");
                                                 else
                                                     ui.item.value=$("#search").val().concat("");
                                                 
                                        }
                                        
                                }
                                
                                   
                            
                        }
                               
                               

                        });
                        
                               
			});  
        

 $(function() {
     $('#srch').submit( function() {
        
         return validateForm();
         
     });
});


    