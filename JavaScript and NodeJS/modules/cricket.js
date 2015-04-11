function returnValue(k,v)
{
        var returnString = "";
        $.each(v,function(key,element){
        if(JSON.stringify(element).slice(0,1)==="{"){
                if(Object.keys(element).length!=0)
		{
         
                returnString  = returnString+ "<h5>"+key+"</h5><ul class=\"nav nav-pills\">";
  
               $.each(element,function(kk,ee){
		if (kk!="10")
                returnString= returnString+"<li class=\"alert alpha-blur\" style=\"padding:5px\">"+kk+" <span class=\"badge\">"+ee+"</span></li>";
                });
		returnString = returnString +"</ul>";
               }
        }
        else{
        returnString  =returnString+"<p><b>"+key+"</b> : "+element+"</p>";
        }
	});

        return returnString;

}



if($("#cricket_stats").length===0){
var cricket_stats=$("<div class=\"well alpha-blur\" id=\"cricket_players\" style=\"border:0px;color:white;\">                <!-- Player info -->                  <div id=\"player_info\" class=\"row\">                        <div class=\"col-xs-12 col-sm-3 col-md-3 col-lg-3\" style=\"margin-top:10px;\">                            <img id=\"cric_img\"class=\"media-object img-responsive\"  alt=\"image\">                        </div>                        <div id=\"pl_info\" class=\"col-xs-12 col-sm-9 col-md-9 col-lg-9\" style=\"margin-top:10px\">                                                                             </div>                  </div>                <!-- /Player info -->                              <div class=\"row\" style=\"margin:0px\" id=\"cricket_players_details\">                  <div id=\"pl_other_info\" class=\"col-xs-12 alpha-blur\" style=\"border:0px solid;margin-bottom:5px\" id=\"cricket_players_batting\">                                                                                                            </div>                                    </div>            <div class=\"row\">  <div class=\"col-lg-6\">                   </div>  <div class=\"col-lg-6\"> <button type=\"button\" class=\"btn btn-default alpha-blur\" style=\"float:right;color:white;border:0px\" aria-label=\"Left Align\" id=\"cricket_players_button\">                    <span class=\"glyphicon glyphicon-stats\" aria-hidden=\"true\"></span> Click for more information                </button>           </div>    </div>  </div>");
$("#predefined_questions").before(cricket_stats);
$("#cricket_players_details").hide();
$("#smart_answer").addClass("hide");
 
$("#cricket_players_details").append("<ul class=\"nav nav-tabs\"><li role=\"presentaenttion\" class=\"active\"><a href=\"#\" onclick=\"changeDiv('cs');return false;\">Career Statistics</a></li><li role=\"presentation\"><a href=\"#\" onclick=\"changeDiv('bowl');return false;\">Bowling</a></li><li role=\"presentation\"><a href=\"#\" onclick=\"changeDiv('bat');return false;\">Batting</a></li></ul>");
$("#cricket_players_details").append("<div class=\"row\" id=\"cont\"></div>");
$("#bowling").click(function(){$("#cont").empty();$("#cont").append(bowl);});

cycle=0;
var cs="";
var bowl="";
var bat="";
var recent="";

function changeDiv(typ)
{

$("#cont").empty();

$("#cont").append(eval(typ));
}
$("#cricket_players_button").on("click",function(){

  $("#cricket_players_details").slideToggle(function(){
    		if(cycle===0){
	    		$("#cricket_players_button").attr("title","Click to see less statistics");
			++cycle;
			}
		else{
			$("#cricket_players_button").attr("title","Click to see more statistics");

			cycle=0;
		}
});


});
$.each(window.val["main-ans"],function(k,v){

if(k==="player-info"){
	$("#pl_info").append("<h3 style=\"margin:0px !important;\">"+window.val["main-ans"]["name"]+"</h3>");
	$("#pl_info").append("<h4 style=\"margin:0px !important;padding-top:5px !important;\">"+window.val["main-ans"]["team"]+"</h4><hr style=\"margin-top:8px !important;\">");
	$.each(v,function(k1,v1){
	
	$("#pl_info").append("<div style=\"margin-bottom:5px;\"><h4 style=\"display:inline;\">"+k1+" :</h4><h5 style=\"display:inline;\"> <span id=\"player_team\">"+v1+"</span></h5></div>");


	});
}

else if (k==="img"){
	$("#cric_img").attr("src",window.val["main-ans"]["img"]);
	$("#cric_img").css({"display":"block","margin-left":"auto","margin-right":"auto"});
}
else if (k==="CAREER STATISTICS")
{

	cs="";
	cs = "<div class =\"col-sm-12\">"+returnValue(k,v)+"</div>";
}

else if (k==="BATTING")
{

        bat = "<div class =\"col-sm-12\">"+ returnValue(k,v)+"</div>";


}

else if(k==="BOWLING"){
	bowl ="<div class =\"col-sm-12\">"+ returnValue(k,v)+"</div>";
}
else if(k!=="name" && k!=="team" && k!=="link"){

$.each(v,function(key,element){
	if(JSON.stringify(element).slice(0,1)==="{"){
	
		var temp="";
		$.each(element,function(kk,ee){
		temp+="<li class=\"alert alpha-blur\" style=\"padding:5px\">"+kk+" <span class=\"badge\">"+ee+"</span></li>";
		});
		$("#"+k).append("<ul class=\"nav nav-pills\">"+temp+"</ul>");
		if(k==="CAREER STATISTICS"){
		cs="<ul class=\"nav nav-pills\">"+temp+"</ul>";
		$("#cont").append(temp);
		}
		if(k=="BOWLING"){bowl="<ul class=\"nav nav-pills\">"+temp+"</ul>";}
		if(k==="BATTING"){bat="<ul class=\"nav nav-pills\">"+temp+"</ul>";}
		if(k==="RECENT"){recent="<ul class=\"nav nav-pills\">"+temp+"</ul>";}
		
	
	}
	else{
	$("#"+k).append("<p>"+element+"</p>");
	}


});
}	



});

$("#smart_col").removeClass("hide");
$("#cont").append(cs);


}

