/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

             $(document).ready(function(){
             $.ajax({
				url:'/login',
				dataType:'text',
		       error: function() {
		      //test( "page not found" );
		    }
		  
		}).done(function(text){
		alert('df');
				$(document).html(text);

				});
                 });
