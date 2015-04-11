if($("#differences").length===0){
var differences=$('<div class="well alpha-blur" style="border:0px;color:white;text-align:left" id="differences"><h3 style="margin-top:0px;">Difference between <span id="dif_title1"></span> and <span id="dif_title2"></span></h3><h6 id="dif_text"></h6><h5><a href="#" style="color:green" id="dif_link"></a></h5></div>');
$("#predefined_questions").before(differences);
$("#smart_answer").addClass("hide");
$("#dif_title1").setTextValue(window.val["title1"]);
$("#dif_title2").setTextValue(window.val["title2"]);
$("#dif_link").setTextValue(window.val["link"]);
$("#dif_link").css('color','#2ECC40');
var re1=new RegExp(window.val["title1"],"g");
var re2=new RegExp(window.val["title2"],"g");
$("#dif_text").html(window.val["description"].replace(re1,"<b>"+window.val["title1"]+"</b>").replace(re2,"<b>"+window.val["title2"]+"</b>"));
$("#dif_text").append("<span><a style=\"padding-left:5px;color:white;\" target=\"_blank\" href=\""+window.val["link"]+"\">...</a></span>");

$("#dif_text >span>a").css('text-decoration','none');
$("#dif_link").attr("href",window.val["link"]);
$("#dif_link").attr("target","_blank");
$("#dif_link").css('font-size','14px');
$("#dif_text").css('font-size','16px');
$("#smart_col").removeClass("hide");
}

