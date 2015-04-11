var wiki=$("<div class=\"well alpha-blur alpha-shadow\" style=\"margin-top:20px;border:0px;\" id=\"wiki\"><div class=\"panel panel-primary\" style=\"margin-bottom:0px;\">       <div class=\"panel-heading\" style=\"background-color:#00B4FF;\"> <h3 class=\"panel-title\" id=\"name\" style=\"text-align: center;\"> </h3></div> <div class=\"panel-body\" style=\"color:#474747;\">  <div class=\"row\">   <div class=\"col-lg-12 col-md-12 col-sm-4 col-xs-4\"><a href=\"#\" class=\"thumbnail\">      <img id=\"info_pic\" src=\"\" alt=\"...\">  </a></div>  <div class=\"col-lg-12 col-md-12 col-sm-8 col-xs-8\"> <table class=\"wiki_table\"></table> </div>   </div>   </div>  </div>");
$("#smart_col").html("").append(wiki);
$("#smart_answer").addClass("hide");
var dic=window.val["infobox"];

if(dic["image"]){
var s="image";
}
else if(dic["logo"]){
s="logo";
}
$("#name").text(dic["name"]["text"]);
delete dic["name"];
$.each(dic,function(k,v){
 if(k.indexOf(s)<0){
		$(".wiki_table").append("<tr style=\"padding-top:15px;\"> <td><b>"+k.replace(/_/g,' ').capitalizeMe()+"</b>: "+v["text"]+"</br> </td> </tr> ");
}
else{
$.ajax({
type:"GET",
dataType:"jsonp",
url:"http://commons.wikimedia.org/w/api.php?action=query&titles=File:"+v["text"]+"&prop=imageinfo&iiprop=url&format=json",
crossDomain:true,
success:function(data){
try{
var js=data;
var a=Object.keys(js["query"]["pages"])[0];
$("#info_pic").attr("src",js["query"]["pages"][a]["imageinfo"][0]["url"]);
}
catch(err){
console.log(err);
$("#info_pic").attr("src","http://upload.wikimedia.org/wikipedia/en/8/80/Wikipedia-logo-v2.svg");

}
}

});

}
	
});
$("#name").text(window.val["wiki"]["infobox"]["name"]["text"]);
$("#one").text(window.val["wiki"]["infobox"]["website"]["text"]);
$("#two").text(window.val["wiki"]["infobox"]["caption"]["text"]);
$("#three").text(window.val["wiki"]["infobox"]["birth_place"]["text"]);
$("#smart_col").removeClass("hide");


