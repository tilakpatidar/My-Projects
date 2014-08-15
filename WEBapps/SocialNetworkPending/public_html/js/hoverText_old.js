/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 * Author @Tilak Patidar
 */

function hoverText(comp,text){  
                 
              $(comp).attr("value",text);
                $(comp).css("color","#999999");
           
                 //fname focusIn
                       $(comp).focusin(function(obj){

                       var content=$(comp).val();
                      
                       if((content===text)){
                           $(comp).css("color","#000000");
                           $(comp).val("");
                       }
                   });
                   $(comp).focusout(function(obj){
                       if($(comp).val()==="")
                       {
                          
                           $(comp).val(text);
                           $(comp).css("color","#999999");
                       }
                       else
                       {
                           $(comp).css("color","#000000");
                       }
                       
                   });
             
            }
           

