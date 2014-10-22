function removeAllActive(){
    $(".tabs").parent().attr("class","");
}
function getForm(){
loadhours();
$("#btm_form").attr('class','show');
}
function getSub(){
$("#pleaseWaitDialog").attr("class","modal show");
            	$.ajaxSetup ({
		cache: false
	});
	
//	load() functions
var t=$('#inputClass').val().split(':');
	$.ajax({type:"GET",url:"/cgi-bin/getSub.py?q="+t[t.length-1],success:function(data,status){
	
    	
    	$("#inputSub").html("");
    	$("#inputSub").html(data);
    	$( "#inputSub" ).prop( "disabled", false );
   	
    	$("#pleaseWaitDialog").attr("class","modal hide");
    	
   $('#inputSub').bind('change', function(){getForm();}).click(function(){
   if($('#inputSub').length == 1) {
    getForm();
  }
});
    	
  }});
}
function loadDod(){
$("#pleaseWaitDialog").attr("class","modal show");
            	$.ajaxSetup ({
		cache: false
	});
	var t=$('#inputDate').val();
	//alert(t);
//	load() functions
	$.ajax({type:"GET",url:"/cgi-bin/getDod.py?d="+t,success:function(data,status){
	
    	$( "#inputDod" ).val(data);
    	//alert(data);
    	$( "#linputDod" ).attr( "class", "col-lg-2  control-label show" );
    	$( "#inputDod" ).attr( "class", "form-control show" );
    	$( "#inputClass" ).prop( "disabled", false );
    	$("#pleaseWaitDialog").attr("class","modal hide");
    	
}
});
}
function updateAttendance(){
$("#pleaseWaitDialog").attr("class","modal show");
            	$.ajaxSetup ({
		cache: false
	});
	var t=$("#form").serialize();
	$.ajax({type:"GET",url:"/cgi-bin/updateAttendance.py?"+t,success:function(data,status){
	
    	$("#pleaseWaitDialog").attr("class","modal hide");
    	loadAttendance();
}
});
}
function loadhours(){
$("#pleaseWaitDialog").attr("class","modal show");
            	$.ajaxSetup ({
		cache: false
	});
	var t=$('#inputClass').val().split(':');
	var x=$('#inputDod').val();
	var s=$('#inputSub').val();
//	load() functions
	$.ajax({type:"GET",url:"/cgi-bin/getHours.py?c="+t[t.length-1]+"&dod="+x+"&sub="+s,success:function(data,status){
	
    	
    	$("#hour").html(data);
    	$("#pleaseWaitDialog").attr("class","modal hide");
    	
}
});
}
function loadStudents(){
$("#pleaseWaitDialog").attr("class","modal show");
            	$.ajaxSetup ({
		cache: false
	});
	var t=$('#inputClass').val().split(':');
//	load() functions
	$.ajax({type:"GET",url:"/cgi-bin/loadStudents.py?c="+t[t.length-1],success:function(data,status){
	
    	
    	$("#students").html(data);
    	$("#pleaseWaitDialog").attr("class","modal hide");
    	
}
});
    	

}
function loadAttendance(){
$("#pleaseWaitDialog").attr("class","modal show");
$.ajaxSetup ({
		cache: false
	});
	//var ajax_load = "<center><img src='/images/loading.gif' alt='loading...' /></center>";
//	load() functions
	$.get("/cgi-bin/getClasses.py",function(data,status){
    			$("#mainArea").html("");
    $("#mainArea").append('<form id="form" class="form-horizontal">  <fieldset>    <legend>Update Attendance</legend>  <div class="form-group">      <label for="inputDate" class="col-lg-2  control-label"> Date</label>      <div class="col-lg-4">        <input class="form-control" id="inputDate" name="inputDate" type="date"/>     </div>    </div>     <div class="form-group">      <label for="inputDod" id="linputDod" name="linputDod" class="col-lg-2  control-label hide">Day Order</label>      <div class="col-lg-4">        <input type="text" class="form-control hide" id="inputDod" name="inputDod" disabled="">      </div>    </div>    <div class="form-group">      <label for="inputClass" class="col-lg-2 control-label"> Class</label>      <div class="col-lg-10">        <select class="form-control" name="inputClass" id="inputClass" disabled="">  '+data+'        </select>      </div>    </div>     <div class="form-group">      <label for="inputSub" class="col-lg-2 control-label"> Subject</label>      <div class="col-lg-10">        <select class="form-control"  id="inputSub" name="inputSub" disabled="">           </select>      </div>    </div>  <div id="btm_form" class="hide"> <div class="form-group">      <label for="inputOpt" class="col-lg-2 control-label"> Hours</label>      <div class="col-lg-10" id="hour">            </div>    </div>  <div class="form-group">      <label class="col-lg-2 control-label"></label>      <div class="col-lg-10">        <div class="radio">          <label>            <input type="radio" name="optionsRadios" id="optionsRadios1" value="All absent">            All absent          </label>        </div>        <div class="radio">          <label>            <input type="radio" name="optionsRadios" id="optionsRadios2" value="All Present">            All Present          </label>        </div>   <div class="radio">          <label>            <input type="radio" name="optionsRadios" id="optionsRadios3" value="Select Manually">            Select Manually          </label>        </div>    </div>    </div> <div class="col-lg-10 col-lg-offset-2" id="students" style="overflow-y: auto;height: 200px;"> </div>  </div> <div class="form-group hide" id="btns">     <div class="col-lg-10 col-lg-offset-2">        <button type="Reset" id="cancel" class="btn btn-default">Cancel</button>        <button type="submit" class="btn btn-primary" id="form1">Update</button>      </div>    </div> </fieldset></form>');
    
     $('#inputClass').bind('change', function(){getSub();}).click(function(){
   if($('#inputClass').length == 1) {
    getSub();
  }
});
 $('#optionsRadios3').bind('change', function(){loadStudents();$("#btns").attr("class","form-group show");});
 $('#inputDate').bind('change', function(){loadDod();});
 $('#optionsRadios1').bind('change', function(){$("#students").html('');$("#btns").attr("class","form-group show");});
 $('#optionsRadios2').bind('change', function(){$("#students").html('');$("#btns").attr("class","form-group show");});
  $('#form').bind('submit', function(){updateAttendance();return false;});
 $('#cancel').bind('click', function(){loadAttendance();});
 $("#pleaseWaitDialog").attr("class","modal hide");
 });
}
$(document).ready(function(){
	$("#pleaseWaitDialog").attr("class","modal hide");
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
        
         $("#rod").click(function(){
            removeAllActive();
            $("#rod").parent().attr("class","active");
            
        });
         $("#rml").click(function(){
            removeAllActive();
            $("#rml").parent().attr("class","active");
            
        });
         $("#odh").click(function(){
            removeAllActive();
            $("#odh").parent().attr("class","active");
            
        });
        
     
       
});
