if($("#site").length===0){
var site=$("<div class=\"well alpha-blur\"><div class=\"row\"><div class=\"col-lg-12\"><div class=\"col-lg-4 col-lg-push-8\"><a href=\"http://"+window.val["main-ans"]["website"]+"\"><img id=\"site_img\" src=\"download.jpg\"alt=\"logo\" style=\"display:block;margin-left:auto;margin-right:auto;padding-top:30px;\"></a></div><div class=\"col-lg-8 col-lg-pull-4\" style=\"\"><div id=\"site_title\" class=\"page-header\"></h1></div></div></div></div><div class=\"row\"><div class=\"col-lg-12\"><p id=\"site_details\" style=\"padding-left:20px;\"class=\"wrap\"></p></div></div></div>");
$("#predefined_questions").before(site);
if(window.val["main-ans"]["type of site"]){
$("#site_title").html("<h1>"+window.val["main-ans"]["title"].capitalizeMe()+"</h1><h4>"+window.val["main-ans"]["type of site"].capitalizeMe()+"</h4>");
}
else{
$("#site_title").html("<h1>"+window.val["main-ans"]["title"].capitalizeMe()+"</h1><h3>Company</h3>");
window.val["main-ans"]["type of site"]="";
}
$("#site_img").attr("src","http://"+window.val["main-ans"]["image"][0]);
$("#site_details").before("<p class=\"wrap\" style=\"padding-left:20px;\">"+window.val["main-ans"]["intro"].replace(/\[\d+\]/g,"").capitalizeMe()+"</p>")
$.each(window.val["main-ans"],function(k,v){

if(k!=="title"&&k!=="image"&&k!=="intro"&&k!=="type of site"&&k!=="type"&&k!=="alexa rank"){
$("#site_details").append("<h4 style=\"display:inline;\">"+k.replace(/_/g," ").capitalizeMe()+"</h4>  <h5 style=\"display:inline;\">"+v.capitalizeMe()+"</h5><br/><br/>");

}

});

$(".wrap").css({"word-break":"normal","word-wrap":"break-word"});
$("#smart_answer").addClass("hide");
$("#smart_col").removeClass("hide");
}
