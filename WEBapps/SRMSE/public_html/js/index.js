/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function validateForm(){
    
   if(($("#name").val()==="")){
      $("#warning").show().hide(10000);
        document.getElementById("warning").innerHTML="<strong>Oh!</strong> Name required !";
        return false;
       
   }
   else if(($("#email").val()==="")){
       $("#warning").show().hide(10000);
         document.getElementById("warning").innerHTML="<strong>Oh!</strong> Email address required !";
        return false;
   }
 
   
   else if(($("#subject").val()==="")){
     $("#warning").show().hide(10000);
      document.getElementById("warning").innerHTML="<strong>Oh!</strong> Subject Required !";
       
        return false;  
    }
 else if(($("#message").val()==="")){
       $("#warning").show().hide(10000);
       document.getElementById("warning").innerHTML="<strong>Oh!</strong> Cannot send message without body !";
        return false;
   }
   
   else
   {
      
       return true;
   }
}
            
        function capitalizeMe(val){
    		return val.charAt(0).toUpperCase()+val.substr(1).toLowerCase();
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

$(document).ready(function(){    
                
    $("#name").focusout(function(){
       
       $('#name').val($('#name').val().trim());
         $('#name').val(capitalizeMe($('#name').val()));
       
        if(((checkSpecialChar( $('#name').val())===1)||(($("#name").val().length)>45))||((containsNum("#name")===1)||(!isNaN($('#name').val()))))
        {
            $("#warning").show().hide(10000);
            document.getElementById("warning").innerHTML="Name must be max 45 characters long and must not contain[0-9][!-)]";
            $('#name').val('');
        }
       
        else{
              $("#warning").hide();
              document.getElementById("warning").innerHTML="Name must be max 45 characters long and must not contain[0-9][!-)]";
        }
    });
});
    $(document).ready(function(){                    
    $("#email").focusout(function(){
        $('#email').val($('#email').val().trim());
        $('#email').val($('#email').val().toLowerCase());
        var email= $('#email').val().toString();
        if(validateEmail(email)===0){
            $('#email').val('');
             $("#warning").show().hide(10000);
             document.getElementById("warning").innerHTML="Please enter a valid email address !";
        }
        else
        {
		if(($('#email').val().length)>45){
			$('#email').val('');
             			$("#warning").show().hide(10000);
             			document.getElementById("warning").innerHTML="Please enter a valid email address !";
		}
		else{
			$("#warning").hide();
            document.getElementById("warning").innerHTML="Please enter a valid email address !";
			}
            
        }
        
    });
});
          $(document).ready(function(){                    
    $("#subject").focusout(function(){
        $('#subject').val($('#subject').val().trim());
        $('#subject').val($('#subject').val().toLowerCase());
	if(($('#subject').val().length)>45)
			{
				$('#subject').val('');
             			$("#warning").show().hide(10000);
             			document.getElementById("warning").innerHTML="Maximum 45 characters allowed !";
			}
	else
        {
            $("#warning").hide();
            document.getElementById("warning").innerHTML="Maximum 45 characters allowed !";
        }
});
});

        $(document).ready(function(){                    
    $("#message").focusout(function(){
        $('#message').val($('#message').val().trim());
        $('#message').val($('#message').val().toLowerCase());
	if(($('#message').val().length)>200)
			{
				$('#message').val('');
             			$("#warning").show().hide(10000);
             			document.getElementById("warning").innerHTML="Maximum 200 characters allowed !";
			}
	else
        {
            $("#warning").hide();
            document.getElementById("warning").innerHTML="Maximum 200 characters allowed !";
        }
});
});

        $(document).ready(function() {
            $('#lcircle').click(function(e){
                 e.preventDefault();
                 $('html, body, .content').animate({scrollTop: $(document).height()*16/100}, 1500);
           
                });
            $('#rcircle').click(function(e){
                 e.preventDefault();
                 $('html, body, .content').animate({scrollTop: $(document).height()*48/100}, 1500);
                });
                
             $('#bcircle').click(function(e){
                 e.preventDefault();
                 $('html, body, .content').animate({scrollTop: $(document).height()*83/100}, 1500);
                });
              $('#contact_us').click(function(e){
                 e.preventDefault();
                 $('html, body, .content').animate({scrollTop: $(document).height()*83/100}, 1500);
                });


       
                // if text input field value is not empty show the "X" button
                $("#field").keyup(function() {
                        $("#x").fadeIn();
                        if ($.trim($("#field").val()) == "") {
                                $("#x").fadeOut();
                        }
                });
                // on click of "X", delete input field value and hide "X"
                $("#x").click(function() {
                        $("#field").val("");
                        $(this).hide();
                });
                $(window).load(function(){
        $('#myModal').modal('show');
        $('#myModal').on('hidden.bs.modal', function (e) {
  // do something...
 // alert("dsfs");
});
    });
        });
      
function swapImages(){
      var $active = $('#myGallery .active');
      var $next = ($('#myGallery .active').next().length > 0) ? $('#myGallery .active').next() : $('#myGallery img:first');
      $active.fadeOut(function(){
      $active.removeClass('active');
      $next.fadeIn().addClass('active');
      });
    }
 
    $(document).ready(function(){
      setInterval('swapImages()', 5000);
    });


$(function() {
                $('#form').on('submit', function() {

		
                  return validateForm();

                });
           });
