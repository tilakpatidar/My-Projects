/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


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
          
           
              
        
          




