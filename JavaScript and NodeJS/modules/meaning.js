if($("#meaning").length===0){
var meaning=$("<div class=\"well alpha-blur\" style=\"border:0px;color:white;text-align:left;\" id=\"dictionary\"> <div><h1 id=\"dict_keyword\" style=\"margin:0px;display:inline;\"></h1></div><div id=\"dict_details\" style=\"padding-top:0px\"></div> <div style=\"padding-top:0px;display:block;height:28px;\"><button class=\"btn glyphicon glyphicon-th-list\" id=\"dict_button\" style=\"border:0px;background-color:transparent;\">&nbsp;Verbs, synonyms etc</button><a href=\"http://dictionary.reference.com/browse/"+window.val["keyword"]+"\" target=\"_blank\" class=\"btn dic\" style=\"float:right;border:0px;background-color:transparent;line-height:16px;font-size:16px;\"><img src=\"http://www.google.com/s2/favicons?domain=http://dictionary.com\" height=\"16\" style=\"padding-right:5px;\"/>Dictionary.com</a> </div></div>");
$.getScript("/main/js/modules/voice.js");
$("#predefined_questions").before(meaning);
once=1;
$("#dict_keyword").html(window.val["keyword"]);

var count=0;
var keys=Object.keys(window.val);
keys.sort();
$.each(keys,function(index,el){
	key=el;
	element=window.val[el];
	if(key!=="keyword"){
	if(once===1){
	$("#dict_keyword").after("<h4 id=\"fs_key\"><i>"+key+"</i></h4>");
			var main=$();
		$.each(element,function(k,element){
			if(element.indexOf(":")>=0){
				var k=element.split(":");
				main=main.add($("<h5 class=\"dict_noun_meaning\" style=\"padding-left:15px;\" >"+k[0]+"</h5>"));
	main=main.add($("<h5 class=\"dict_noun_meaning\" style=\"padding-left:25px;\" >\""+k[1]+"\"</h5>"));
			}
else{
			main=main.add($("<h5 class=\"dict_noun_meaning\" style=\"padding-left:15px;\" >"+element+"</h5>"));
}
		});
		$("#fs_key").after(main);
	once=2;
	}
	else{
	var t=$("#dict_details").append("<h4 id=\""+key+"\"><i>"+key+"</i></h4>");
		var main=$();
		var rem=false;
		$.each(element,function(k,e){
			if(e===""){
				rem=true;
			}
else{
		if(e.indexOf(":")>=0){
				var k=e.split(":");
				main=main.add($("<h5 class=\"dict_noun_meaning\" style=\"padding-left:15px;\" >"+k[0]+"</h5>"));
	main=main.add($("<h5 class=\"dict_noun_meaning\" style=\"padding-left:25px;\" ><i>\""+k[1].trim()+"\"</i></h5>"));
			}
else{
			main=main.add($("<h5 class=\"dict_noun_meaning\" style=\"padding-left:15px;\" >"+e+"</h5>"));
}
rem=false;
}
		});
			if(rem===true){
			console.log(t);
			$("#"+key).remove();
			}
else{
$("#dict_details").append(main);

}
		
	}
}
count++;
});

if(count===2){

$("#dict_details").remove();
$("#dict_button").remove();
}
else{
$("#dict_details").prepend("<hr>");
$("#dict_details").hide();
$("#dict_button").click ( function() { $("#dict_details").slideToggle(); } );
}
$("#fs_key").before("<span class=\"glyphicon glyphicon-volume-up\" id=\"speak\" style=\"font-size:22px;padding-left:15px;cursor:pointer;\"></span>");
$("#speak").click(function(){

responsiveVoice.speak(window.val["keyword"]);

});
$("#smart_answer").addClass("hide");
$("#smart_col").removeClass("hide");
}
