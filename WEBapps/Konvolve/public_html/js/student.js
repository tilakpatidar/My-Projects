function removeAllActive(){
    $(".tabs").parent().attr("class","");
}

function loadAttendance(){
$("#pleaseWaitDialog").attr("class","modal show");
            	$.ajaxSetup ({
		cache: false
	});
	
//	load() functions
	$.ajax({type:"GET",url:"/cgi-bin/refreshAttendance.py",success:function(data,status){
	
    	$("#mainArea").html("");
    	 $("#mainArea").html(data);
    	$("#pleaseWaitDialog").attr("class","modal hide");
    	
  }});
	
       
   
}
function noOfDays(f,l){
var oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
f=f.toString().split('-')
l=l.toString().split('-')
var firstDate = new Date(f[0],f[1],f[2]);
var secondDate = new Date(l[0],l[1],l[2]);

var diffDays = Math.round((secondDate.getTime()-firstDate.getTime())/(oneDay));
if (parseInt(diffDays)<0){
$("#days").val("0");
alert("To date must be greater than From date.");
}
else{
$("#days").val(diffDays);
}
}
function loadCam(){

$("#webcamDialog").attr("class","modal show");
$("#webcam").scriptcam({
					showMicrophoneErrors:false,
					onError:onError,
					cornerRadius:20,
					disableHardwareAcceleration:1,
					cornerColor:'e3e5e2',
					onWebcamReady:onWebcamReady,
					uploadImage:'upload.gif'
					//onPictureAsBase64:base64_tofield_and_image
				});
			
			function base64_tofield() {
				$('#proof').val($.scriptcam.getFrameAsBase64());
				alert($("#proof"));
			};
			function changeCamera() {
				$.scriptcam.changeCamera($('#cameraNames').val());
			}
			function onError(errorId,errorMsg) {
				$( "#btn1" ).attr( "disabled", true );
				$( "#btn2" ).attr( "disabled", true );
				alert(errorMsg);
			}			
			function onWebcamReady(cameraNames,camera,microphoneNames,microphone,volume) {
				$.each(cameraNames, function(index, text) {
					$('#cameraNames').append( $('<option></option>').val(index).html(text) )
				}); 
				$('#cameraNames').val(camera);
			}
			
$("#camcapture").bind('click',function(){base64_tofield();alert("Image Captured");});
$("#camclose").bind('click',function(){$("#webcamDialog").attr("class","modal hide");});
}
function loadOD(){
$("#pleaseWaitDialog").attr("class","modal show");
            	$.ajaxSetup ({
		cache: false
	});
	
//	load() functions
	$.ajax({type:"GET",url:"/cgi-bin/refreshOD.py",success:function(data,status){
	
    	$("#mainArea").html("");
    	 $("#mainArea").html(data);
    	$("#pleaseWaitDialog").attr("class","modal hide");
    	
    	  $('#to').bind('change', function(){noOfDays($('#from').val(),$('#to').val())});
    	    $('#proofYes').bind('change', function(){loadCam();});
  }});
	
       
   
}
$(document).ready(function(){
    $("#home").parent().attr("class","active");
        $("#attendance").click(function(){
            removeAllActive();
            $("#attendance").parent().attr("class","active");
            $("#mainArea").html("");
            loadAttendance();
            
        });
         $("#home").click(function(){
            removeAllActive();
            $("#home").parent().attr("class","active");
        });
        
         $("#od").click(function(){
            removeAllActive();
            loadOD();
            $("#od").parent().attr("class","active");
            
        });
         $("#ml").click(function(){
            removeAllActive();
            $("#ml").parent().attr("class","active");
            
        });
        //for cam
   
				
});
