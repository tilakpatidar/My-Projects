if($("#bank").length===0){

var bank=$("<div class=\"col-lg-12 well alpha-blur alpha-shadow\" style=\"margin-top:20px;border:0px;text-align:center\" id=\"bank\">   <div class=\"panel panel-primary\" style=\"margin-bottom:0px;\">       <div class=\"panel-heading\" style=\"background-color:#00B4FF;\"> <h3 class=\"panel-title\" id=\"name\" style=\"text-align: center\"> </h3></div> <div class=\"panel-body\" style=\"color:#474747;\">  <div class=\"row\">   <div class=\"col-lg-12 col-md-12 col-sm-4 col-xs-4\"><a href=\"#\" class=\"thumbnail\">      <img id=\"min_pic\" src=\"\" alt=\"...\">  </a></div>  <div class=\"col-lg-12 col-md-12 col-sm-8 col-xs-8\"> <table id=\"bank_table\" class=\"table\" style=\"text-align: center \"></table> </div>   </div>   </div>  </div>");
console.log(bank);
$("#smart_col").html("").append(bank);
$("#smart_answer").addClass("hide");
$("#name").text(window.val["main-ans"]["name"]);
var end="";
$.each(window.val["main-ans"],function(key,element){

if(key!=="name" && key!=="image source"){
if(window.val["required"].join(" ").indexOf(key)>=0){
end+="<tr><td class=\"td_border\"><b>"+key.capitalizeMe()+" : "+element+"</b></td></tr> ";
}else{
$("#bank_table").append("<tr><td class=\"td_border\">"+key.capitalizeMe()+" : "+element+"</td></tr> ");
}
}
});
$("#bank_table").prepend(end);
$.ajax({
type:"GET",
dataType:"jsonp",
url:"http://commons.wikimedia.org/w/api.php?action=query&titles="+window.val["main-ans"]["image source"].split("/").pop()+"&prop=imageinfo&iiprop=url&format=json",
crossDomain:true,
success:function(data){

try{
var js=data;
var a=Object.keys(js["query"]["pages"])[0];
$("#min_pic").attr("src",js["query"]["pages"][a]["imageinfo"][0]["url"]);
}
catch(err){
$("#min_pic").attr("src","http://upload.wikimedia.org/wikipedia/commons/1/1b/Seal_of_the_Reserve_Bank_of_India.svg");

}
}

});

$("#smart_col").removeClass("hide");
}
