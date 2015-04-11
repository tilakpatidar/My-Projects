if($("#highcourt").length===0){
var hc=$("<div class=\"col-lg-12 well alpha-blur alpha-shadow\" style=\"margin-top:20px;border:0px;text-align:center\" id=\"high_court\">   <div class=\"panel panel-primary\" style=\"margin-bottom:0px;\">       <div class=\"panel-heading\" style=\"background-color:#00B4FF;\"> <h3 class=\"panel-title\" id=\"name\" style=\"text-align: center\"> </h3></div> <div class=\"panel-body\" style=\"color:#474747;\">  <div class=\"row\">   <div class=\"col-lg-12 col-md-12 col-sm-4 col-xs-4\"><a href=\"#\" class=\"thumbnail\">      <img id=\"info_pic\" src=\"\" alt=\"...\">  </a></div>  <div class=\"col-lg-12 col-md-12 col-sm-8 col-xs-8\"> <table class=\"high_table\"></table> </div>   </div>   </div>  </div>");
$("#smart_col").html("").append(hc);
$("#smart_answer").addClass("hide");
var dic=window.val["main-ans"];
$("#name").text(dic["name"].capitalizeMe());
$("#info_pic").attr("src",dic["image"]);
$.each(dic,function(k,v){
 if(k.indexOf("image")<0 && k!=="name"){

 if(window.val["required"][0]===k){ $(".high_table").append("<tr style=\"padding-top:15px;\"> <td><b>"+k.replace(/_/g,' ').capitalizeMe()+"</b>: <u><b>"+v+"</b></b></br> </td> </tr> ");}else{
		$(".high_table").append("<tr style=\"padding-top:15px;\"> <td><b>"+k.replace(/_/g,' ').capitalizeMe()+"</b>: "+v+"</br> </td> </tr> ");
		}
}
	
});
$("#smart_col").removeClass("hide");

}
