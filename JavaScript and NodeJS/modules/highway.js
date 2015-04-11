if($("#highway").length===0){
var highway=$("<div id=\"highway\" class=\"module col-md-12 well alpha-blur\" style=\"border:0px;margin-top:20px;color:white;\"> <div class=\"row\" style=\"text-align:center\"> <img src=\"/main/images/highway.png\" height=\"62\" width=\"65\"> </div> <div class=\"row\" style=\"text-align:center;padding-top:5px\"> <h4 id=\"highway_highway\"></h4> <h5><span id=\"route\"></span></h5> <h6 id=\"highway_length_state\"></h6> <h5><b>Total Length - </b><span id=\"highway_length_total\"></span></h5> </div><div class=\"row\" style=\"text-align:center;\">                     <div style=\"float:left;width:50&percnt;;height:34px;\">                        <button id=\"high_prev\" style=\"background-color:#008EFF;\" class=\"btn btn-primary glyphicon glyphicon-chevron-left\" value=\"Previous\"/>                     </div>                     <div style=\"float:left;width:50&percnt;;height:34px;\">                     <button id=\"high_next\" style=\"background-color:#008EFF;\" class=\"btn btn-primary glyphicon glyphicon-chevron-right\" value=\"Next\"/>                     </div>                  </div>          </div>");

$("#smart_col").html("").append(highway);
$("#smart_answer").addClass("hide");
window.high=window.val["ans"];
window.chigh=0;
$("#high_prev").attr("disabled", "disabled");
$("#highway_length_state").text(window.val["ans"][0]["length_state"]);
$("#highway_length_total").text(window.val["ans"][0]["length_total"]);
var k=window.val["ans"][0]["route"];
var cities=[];
$.each(k,function(index,element){
if($("#search").val().trim().toLowerCase().indexOf(element)>=0 && (element!==k[0] && element!==k[k.length-1])){
cities.push(element);

}

});
if(cities.length!==0){$("#route").text(k[0]+" - "+cities.join(" - ")+" - "+k[k.length-1]);}else{$("#route").text(k[0]+" - "+k[k.length-1]);}
$("#smart_col").removeClass("hide");
$("#high_prev").on("click", function() {

   if (window.high.length > 1 && window.chigh < window.high.length && window.chigh !== 0) {
	--window.chigh;
	var val=window.val["ans"][chigh];
	var k=val["route"];
var cities=[];
$.each(k,function(index,element){
if($("#search").val().trim().toLowerCase().indexOf(element)>=0 && (element!==k[0] && element!==k[k.length-1])){
cities.push(element);

}

});
	$("#highway_length_state").text(val["length_state"]);
	$("#highway_length_total").text(val["length_total"]);
	if(cities.length!==0){$("#route").text(k[0]+" - "+cities.join(" - ")+" - "+k[k.length-1]);}else{$("#route").text(k[0]+" - "+k[k.length-1]);}
	 $("#high_next").removeAttr("disabled");
	 $("#smart_answer").addClass("hide");
}
 if (window.chigh === 0) {
            $("#high_prev").attr("disabled", "disabled");
            $("#high_next").removeAttr("disabled");
        }

});
$("#high_next").on("click", function() {
	if (window.high.length > 1 && window.chigh < (window.high.length - 1)) {
		++window.chigh;
		$("#high_prev").removeAttr("disabled");
		var val=window.val["ans"][chigh];
			var k=val["route"];
var cities=[];
$.each(k,function(index,element){
if($("#search").val().trim().toLowerCase().indexOf(element)>=0 && (element!==k[0] && element!==k[k.length-1])){
cities.push(element);

}

});
		$("#highway_length_state").text(val["length_state"]);
		$("#highway_length_total").text(val["length_total"]);
		if(cities.length!==0){$("#route").text(k[0]+" - "+cities.join(" - ")+" - "+k[k.length-1]);}else{$("#route").text(k[0]+" - "+k[k.length-1]);}
		$("#highway").removeClass("hide");
		$("#smart_answer").addClass("hide");
	}
	 if ((window.chigh === (window.high.length - 1)) && (window.high.length !== 1)) {
		    $("#high_next").attr("disabled", "disabled");
		    $("#high_prev").removeAttr("disabled");

		}


});
}

