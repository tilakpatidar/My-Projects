(function($){var proto = $.ui.autocomplete.prototype,	initSource = proto._initSource;function filter( array, term ) {	var matcher = new RegExp( $.ui.autocomplete.escapeRegex(term), "i" );	return $.grep( array, function(value) {		return matcher.test( $( "<div>" ).html( value.label || value.value || value ).text() );	});}$.extend( proto, {	_initSource: function() {		if ( this.options.html && $.isArray(this.options.source) ) {			this.source = function( request, response ) {				response( filter( this.options.source, request.term ) );			};		} else {			initSource.call( this );		}	},	_renderItem: function( ul, item) {		return $( "<li></li>" )			.data( "item.autocomplete", item )			.append( $( "<a></a>" )[ this.options.html ? "html" : "text" ]( item.label ) )			.appendTo( ul );	}});})( jQuery );
$("#prog").remove();
$(document).ready(function(){
$.ajaxSetup({cache:true});
window.leftauto=-1;
window.firstresize=true;
window.strlen=0;
//shadowing parthere
$(".backinput").remove();
var inp=$("#search").clone();
inp.removeClass("fostyle");
inp.removeAttr("id");
inp.removeAttr("placeholder");
inp.removeAttr("name");
inp.removeClass("ui-autocomplete-input");
inp.removeClass("btn2");
inp.addClass("btn1");
inp.addClass("backinput");
inp.attr("disabled","");
inp.autocomplete({});
if(window.location.toString().indexOf("s.py")>0){
inp.css("margin-top","8px");
inp.css("width","80%");
inp.attr("id","input_back");
}
$("#div_for_back").append(inp);
    $("#search").autocomplete({
                  
            source: "/cgi-bin/getWords.py",
            minLength: 1,
            autoFocus: false,
            appendTo:".search_div",
            html:true,
            open: function(event, ui) {
            $('ul.ui-autocomplete').addClass('opened');
                $(".ui-helper-hidden-accessible").remove();
                    $(this).autocomplete("widget").css({
                "width": ($("#search").parent().width() + "px")
            });
if(window.leftauto!==-1){
            $(".ui-autocomplete").css("postion","relative").css("left",window.leftauto+"px");
$(".ui-autocomplete").css("width","");
$(".ui-autocomplete >li").css("width","100%");
$(".ui-autocomplete >li>a").css("white-space","nowrap");//,($("#search").width()-window.strlen)+"px");
}
            event.preventDefault();
        },close: function () { 
    $('ul.ui-autocomplete')
      .removeClass('opened')
      .css('display','block'); 
  },
            focus: function (event, ui) {
            console.log(ui);
              if($("#search").val().trim()!==""){
              if(ui["item"]["resize"]){
              var d=$("#search").val().split(" ");
              
              inp.val((d.slice(0,d.length-1)+" "+ui["item"]["value"]).replace($("#search").val().toLowerCase(),$("#search").val()));
              }else{
              
              if(ui["item"]["resize"]){
             
		inp.val(ui["item"]["value"].replace($("#search").val().toLowerCase(),$("#search").val()));
}
else{
$("#search").val(ui["item"]["value"]);
inp.val(ui["item"]["value"]);

}
}
}
               
              
if(window.originalquery){
              if(window.originalquery!=""){
event.preventDefault();
var arr=window.originalquery.split(" ");
		var temp=arr.slice(0,arr.length-1).join(" ");
              $("#search").val(temp+" "+ui["item"]["value"]);
              
              }
             }




        },
response:function(event,ui){
          if($("#search").val().trim()!==""){
if(ui.content[0]["resize"]==="true"){
var arrr=$("#search").val().trim().split(" ");
		inp.val(arrr.slice(0,arrr.length-1).join(" ")+" "+ui.content[0]["value"]);
}
else{inp.val(ui.content[0]["value"].replace($("#search").val().toLowerCase(),$("#search").val()));}
}
                 

console.log(ui);
if(ui.content[0]["resize"]==="true"){
window.originalquery=$("#search").val().trim();
	if(window.firstresize){
window.space=false;
		window.defaultleft=parseInt($("#search").offset().left);
		window.firstresize=false;
		var pos=$("#search").val().length*parseInt($("#search").css("font-size").replace("px",""));
window.strlen=parseInt(pos)*0.7;
		window.leftauto=(window.defaultleft+parseInt(pos))*0.7;
	}
	else{
if(window.space){
		var pos=$("#search").val().length*parseInt($("#search").css("font-size").replace("px",""));
window.strlen=parseInt(pos)*0.7;
		window.leftauto=(window.defaultleft+parseInt(pos))*0.7;
window.space=false;
}	
}


}
else{
window.originalquery="";
window.leftauto=-1;
}
},
            select:function (e, ui) {
            
               e.preventDefault();
              
                    var query=$("#search").val().trim();
                    console.log("Query submitted");
                    console.log(query);
                    window.location="/cgi-bin/s.py?q="+query;
               
                    
               
              
        }
        ,delay:300
        
                               
                               

    });
    $("#search").on("keypress",function(event){

if($("#search").val().indexOf(" ")===0){
$("#search").val($("#search").val().replace(/\s+/g," ").trim());
}
if($("#search").val().trim()===""){
inp.val("");
}
    console.log($("#search").val());
    if((event.keyCode===13) && ($("#search").val()!=="")){
            var query=$("#search").val().trim();
            console.log("Query submitted");
            console.log(query);
            window.location="/cgi-bin/s.py?q="+query;
    
    }
    if(event.keyCode!==39){inp.val("");}
    
    });

$("#search").on("keydown",function(event){
if(event.keyCode!==39){inp.val("");}
if($("#search").val().indexOf(" ")===0){
$("#search").val($("#search").val().replace(/\s+/g," ").trim());
}

if(event.keyCode===39){
if((document.getElementById('search').selectionStart===$("#search").val().length)&&$("#search").val().length<$(".backinput").val().length){
$("#search").val($(".backinput").val());
}

}
else{
$(".backinput").val("");
}

if($("#search").val().trim()===""){
inp.val("");
}
});
    $("#search_btn").on("click",function(){
        if($("#search").val().trim()!==""){
            var query=$("#search").val().trim();
            console.log("Query submitted");
            console.log(query);
            window.location="/cgi-bin/s.py?q="+query;
        }
    });
    
    
    $(window).on("resize",function(){
    
    //hides autocomplete dropdown on screen resize
    $(".ui-autocomplete").hide();
    window.leftauto=-1;
window.firstresize=true;
window.strlen=0;
    
    });
window.connect=function(data_pass){
            var data = data_pass;
            $.ajax({
                type: 'get',
                url:'/cgi-bin/locentric.py',
                data: data,
                success : function(response){
                    window.locentric = response;
                    console.log(response);
                }
            });
        };
window.loadLocation=function(){
if(document.cookie.indexOf("latitude")>=0){
var obj={};
var arr=document.cookie.split(";");
$.each(arr,function(index,element){
var t=element.split("=");
obj[t[0].trim()]=t[1].trim();
});
window.connect({"lat":obj["latitude"], "long":obj["longitude"]});

}
else{
$.getScript("/main/js/location_centric.js");
}

};
 window.loadLocation();
 $("#search").on("keyup",function(event){


if($("#search").val().trim()===""){
inp.val("");
}
if(event.keyCode===32)

{window.space=true;}
else if(event.keyCode===8){
var a=$("#search").val();
if(a.slice(a.length-1,a.length)===" "){
if(a.slice(a.length-2,a.length)==="  "){window.space=false;}
else{
window.space=true;
}

}
}
});
if(window.location.toString().indexOf("s.py")<0){
$("input").removeClass("hide");
$(".input-group").removeClass("hide");
var img2=$("#srmse-logo");
if(window.color==="black"){img2.attr("src","/main/images/dark/srmselogo.png");}else{img2.attr("src","/main/images/light/srmselogo.png");}

img2.attr("alt","SRM Search Engine");
var img1=$("#nixi-logo");
if(window.color==="black"){img1.attr("src","/main/images/dark/nixi.png");}else{img1.attr("src","/main/images/light/nixi.png");}
img1.attr("alt","Nixi");
img1.attr("width","127px");
img1.attr("height","44px");
var img=$("#srm-logo");
if(window.color==="black"){img.attr("src","/main/images/dark/srm.png");}else{img.attr("src","/main/images/light/srm.png");}
img.attr("alt","SRM University");
img.attr("width","130px");
img.attr("height","50px");
var u=0;

var dispBtns=function(){$(".arrow_div").css("padding-left","20px");$(".arrow_div").append("<div style=\"position:relative;top:0;bottom:0;padding-top:24px;height:50px;\"><span id=\"light\" class=\"side_btns\" data-toggle=\"tooltip\" title=\"Light Theme\"><img style=\"width:31px;height:27px;top:0;bottom:0;margin:auto;\" src=\"/main/images/lighttheme.png\"></span><span id=\"dark\" class=\"side_btns\" data-toggle=\"tooltip\" title=\"Dark Theme\"><img style=\"top:0;bottom:0;margin:auto;width:31px;height:27px;margin-left:5px;\" src=\"/main/images/darktheme.png\">   </span> <span id=\"help\" class=\"side_btns\" data-toggle=\"tooltip\" title=\"Want Help !\">  <img style=\"top:0;bottom:0;margin:auto;width:31px;height:27px;margin-left:5px;\" src=\"/main/images/howtouse.png\">      </span> </div>");$(".side_btns").css("cursor","pointer");

$("#light").on('click',function(){
	document.cookie="color=white;path=/";
	window.color="white";
	$("#dark_theme").remove();
$("#light_theme").remove();
	$("head").append("<link id=\"light_theme\" rel='stylesheet' type='text/css' href='/main/css/light/styles.css' />");
	$("#nixi-logo").attr("src","/main/images/light/nixi.png");
	$("#srmse-logo").attr("src","/main/images/light/srmselogo.png");
	$("#srm-logo").attr("src","/main/images/light/srm.png");
});

$("#dark").on('click',function(){
	document.cookie="color=black;path=/";
	window.color="black";
	$("#light_theme").remove();
$("#dark_theme").remove();
	$("head").append("<link id=\"dark_theme\" rel='stylesheet' type='text/css' href='/main/css/dark/styles.css' />");
	$("#nixi-logo").attr("src","/main/images/dark/nixi.png");
	$("#srmse-logo").attr("src","/main/images/dark/srmselogo.png");
	$("#srm-logo").attr("src","/main/images/dark/srm.png");
});
var clicked=false;

$('#help').on("click",function(){
if(!clicked){
$.getScript('/main/js/modules/help.js');
clicked=true;
}
else{
$("#help_box").animate({opacity:'0'},500,function(){
$("#help_box").remove();
});

clicked=false;
}
});


};

$("#arrow").on("click",function(){
if(u===0){
$(".arrow_div").remove();
$("#arrow_parent").append("<div class=\"arrow_div\" style=\"float:left;height:75px;float:right;width:0px;margin-top:5px;\"></div>");
dispBtns();
$(".side_btns").hide();
$("#arrow").css("right","-1px");
$(".arrow_div").animate({width:'150px'},500,function(){$(".side_btns").fadeIn();});

++u;
}
else{
$(".side_btns").fadeOut(function(){$(".side_btns").hide();$(".arrow_div").css("padding-left","0px");$(".arrow_div").animate({width:'0px'},500,function(){

$("#arrow").css("right","0px");
});
u=0;});
	


}

});


}

});
