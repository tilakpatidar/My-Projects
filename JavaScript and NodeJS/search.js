/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 
 Author Tilak Patidar
 email tilakpatidar@gmail.com
 github http://github.com/tilakpatidar      
  */
$(document).ready(function() {


var img2=$("#srmse-logo");
if(window.color==="black"){$("head").append("<link id=\"dark_theme\" rel='stylesheet' type='text/css' href='/main/css/dark/search.css' />");img2.attr("src","/main/images/dark/srmselogo.png");}else{img2.attr("src","/main/images/light/srmselogo.png");$("head").append("<link id=\"light_theme\" rel='stylesheet' type='text/css' href='/main/css/light/search.css' />");}

img2.attr("alt","SRM Search Engine");

$.ajaxSetup({cache:true});




    $.getScript( "/main/js/jquery-ui.min.js",function(){
 $.getScript( "/main/js/scripts.js");

});
   var u=0;
   var dispBtns=function(){$(".arrow_div").css("padding-left","20px");$(".arrow_div").append("<div style=\"position:relative;top:0;bottom:0;padding-top:18px;height:50px;\"><span id=\"light\" class=\"side_btns\" data-toggle=\"tooltip\" title=\"Light Theme\"><img style=\"top:0;bottom:0;margin:auto;width:31px;height:27px;\" src=\"/main/images/lighttheme.png\"></span><span   class=\"side_btns\" id=\"dark\" data-toggle=\"tooltip\" title=\"Dark Theme\"><img style=\"top:0;bottom:0;margin:auto;width:31px;height:27px;margin-left:5px;\" src=\"/main/images/darktheme.png\">   </span> <span class=\"side_btns\" data-toggle=\"tooltip\" title=\"Want Help !\">  <img style=\"top:0;bottom:0;margin:auto;width:31px;height:27px;margin-left:5px;\" src=\"/main/images/howtouse.png\">      </span> </div>");$(".side_btns").css("cursor","pointer");
   $("#light").on('click',function(){
	window.color="white";
document.cookie="color=white;path=/";
	$("#dark_theme").remove();
$("#light_theme").remove();
	$("head").append("<link id=\"light_theme\" rel='stylesheet' type='text/css' href='/main/css/light/search.css' />");
	$("#srmse-logo").attr("src","/main/images/light/srmselogo.png");
});

$("#dark").on('click',function(){
	window.color="black";
document.cookie="color=black;path=/";
	$("#light_theme").remove();
	$("#dark_theme").remove();
		$("head").append("<link id=\"dark_theme\" rel='stylesheet' type='text/css' href='/main/css/dark/search.css' />");
	$("#srmse-logo").attr("src","/main/images/dark/srmselogo.png");
});
   
   };
function arrowClick(){
	if(u===0){
	$(".arrow_div").remove();
	$("#arrow_parent").append("<div class=\"arrow_div\" style=\"float:left;height:62px;float:right;width:0px;\"></div>");
	dispBtns();
	$(".side_btns").hide();
	$(".arrow_div").animate({width:'150px'},500,function(){$(".side_btns").fadeIn();});

	++u;
	}
	else{
	$(".side_btns").fadeOut(function(){$(".side_btns").hide();$(".arrow_div").css("padding-left","0px");$(".arrow_div").animate({width:'0px'},500,function(){
	});
	u=0;});
	

	}

}
$("#arrow").on("click",arrowClick);
/*document.getElementById("arrow").addEventListener('touchstart', function(e){
        arrowClick();
        e.stopPropa
        gation();
    }, false);*/


    window.i = 0;
    window.j = 10;
    IDS = [];
    IDSwiki=[];
    IDSnews=[];
    window.trains = [];
    window.wi=0;
    window.wj=1;
    window.icluster = 0;
    window.jcluster = 4;
    window.results = true;
    window.clusters = [];
    window.locations=[];
    window.clocation=0;
    window.val={};
window.tap=false;
window.scrolled=false;
window.wiki=false;

//caching scripts
   $.ajaxSetup({
  cache: true
});
//scroll button

var screensize=$("html").height();
 $(function(){ 

$(document).on( 'scroll', function(){ 

if ($(window).scrollTop() > 100) {
 $('.scroll-top-wrapper').addClass('show');setTimeout(function(){$('.scroll-top-wrapper').removeClass('show');},4000); } else { $('.scroll-top-wrapper').removeClass('show'); } }); $('.scroll-top-wrapper').on('click', scrollToTop); }); function scrollToTop() { verticalOffset = typeof(verticalOffset) != 'undefined' ? verticalOffset : 0; element = $('body'); offset = element.offset(); offsetTop = offset.top; $('html, body').animate({scrollTop: offsetTop}, 500, 'linear'); } 

    var load = $("<div id=\"loading\" style=\"background-color:#333333;\"><img src=\"/main/images/ajax-loader.gif\" width=\"20\" height=\"20\"/></div>");
    function navChanger() {
        $(".newside").remove();
//fixing affix
$("#smart_col").width($("#smart_col").parent().width());
$(".nav-sidebar").css("width","inherit");

        //hides autocomplete dropdown on screen resize
        $(".ui-autocomplete").removeClass("show");
        if ($(window).width() <= 1000) {

if($("#tap").length<=0 && !window.tap && window.clusters.length>0){
var tap=$("<div id=\"tap\" style=\"position:absolute;top:122px;width:100%;height:50px;z-index:99;\"><button class=\"btn btn-danger\" style=\"width:100%;height:100%;\" type=\"button\">Tap to see clusters</button></div>");
$("body").append(tap);
tap.on("click",function(){
 $(this).slideUp("fast",function(){
	$(this).hide();
});
});
window.tap=true;
}
else if(window.tap){

}
else{
$("#tap").show();
}
if(window.clusters.length===0){
$("#smart_answer").css("margin-top","102px");
$(".side").removeClass("full-height");
}
else{
$("#smart_col").css("margin-top","62px");
$(".side").addClass("full-height");
}     
       
$(".side").addClass("hide");

$("#centre_parent").css("margin-top","20px");
console.log("resize");
            var newnav = $("<div class=\"alpha-blur newside\" style=\"width:"+$(".nav_changer").width()+"px;\"></div");
            var lbtn = $("<button style=\"\" class=\"cluster_lbtn btn alpha-blur glyphicon glyphicon-chevron-left\"></button>");
            var rcol = $("<div style=\"float:left;height:100%;width:40px;\" class=\"\"></div>");
            var lcol = $("<div style=\"float:left;height:100%;width:40px;\" class=\"\"></div>");
            var rbtn = $("<button style=\"\" class=\"cluster_rbtn btn alpha-blur glyphicon glyphicon-chevron-right\"></button>");
            var r = $("<div style=\"width:100%;height:100%;padding-top:5px;padding-bottom:5px;\"></div>");
            var main = $("<div style=\"padding:0px !important;height:50px;width:"+($(".nav_changer").width()-80)+"px;\" class=\"col-lg-10 col-md-10 col-sm-10 col-xs-10\"></div>");
            rcol.append(rbtn);
            lcol.append(lbtn);
            r.append(lcol);



            if (window.clusters.length > 0) {
                var m = $();
                //console.log(window.clusters.slice(window.icluster, window.jcluster));
                $.each(window.clusters.slice(window.icluster, window.jcluster), function(index, element) {
                    //console.log(element);
                    var h=($(".nav_changer").width()-105)/4;
if(index===window.jcluster){
var temp = $("<div data-toggle=\"tooltip\" data-placement=\"bottom\" class=\"cluster_btn\" title=\""+element.capitalizeMe()+"\" style=\"width:"+h+"px;\"></div>");

                    temp.text(element.capitalizeMe());
                    m = m.add(temp);
}
else{
                    var temp = $("<div data-toggle=\"tooltip\" data-placement=\"bottom\" class=\"cluster_btn\" title=\""+element.capitalizeMe()+"\" style=\"width:"+h+"px;\"></div>");

                    temp.text(element.capitalizeMe());
                    m = m.add(temp);
}
                });
                main.append(m);
                r.append(main);
                r.append(rcol);
                newnav.append(r);

                newnav.height("50");
                $(".nav_changer").prepend(newnav);
                main.on("mouseenter", "div", function() {
                    $(this).css({
                        "color": "#e2e2e2",
                        "background-color": "rgba(99,0,24,0.3)"
                    });

                });
                main.on("mouseleave", "div", function() {
                    $(this).css({
                        "color": "#e2e2e2",
                        "background-color": "transparent"
                    });
                    main.on("click", "div", function() {

                        $(this).addClass("active");
                        var old = $("#search").val();
                        window.cluster = $(this).text();

                        window.location = "/cgi-bin/s.py?q=" + $("#search").val().trim() + "&c=" + window.cluster;

                    });

                });
                lbtn.on("click", function() {
                    if (window.icluster !== 0) {
                        window.icluster -= 3;
                        window.jcluster -= 3;
                        //console.log(window.icluster);
                        $(".navside").remove();
                        navChanger();

                    }

                });
                rbtn.on("click", function() {
                    if ((window.jcluster + 3) <= window.clusters.length) {
                        window.icluster += 3;
                        window.jcluster += 3;
                        //console.log(window.icluster);
                        $(".navside").remove();
                        navChanger();
                    }
                });
            } else {

                getClusters();
            }

$(".newside").css("margin-top","122px");

        } else {
$("#tap").hide();
$("#centre_parent").css("margin-top","82px");
$(".newside").css("margin-top","82px");
$("#smart_col").css("margin-top","82px");
if(window.clusters.length>0){
            $(".side").removeClass("hide");
}
else{
$("#smart_answer").css("margin-top","22px");

}

        }




    }
    navChanger();
    $(window).on("resize", navChanger);

    //clusters click event
    $(".nav-sidebar").on("click", "a", function() {

        $(this).addClass("active");
        var old = $("#search").val();
        window.cluster = $(this).text();
        window.location = "/cgi-bin/s.py?q=" + $("#search").val().trim() + "&c=" + window.cluster;

    });
    $("#predefined_questions").hover(function() {
        $("#collapsee").collapse('show');

    });
    $("#collapsee").on("mouseleave", function() {
        $("#collapsee").collapse('hide');
    });
    $("#search_btn").on("submit", function() {
        if ($("#search").val().trim() !== "") {
            var query = $("#search").val().trim();
            return true;
        }
    });


    $("#logo").on("click", function() {

        window.location = "/main/";
    });

    //click on suggested ques
    $("#collapsee").on("click", "a", function() {
        var v = $(this).text();
        $("#search").val(v);
        $("#search").attr("value", v);
        window.location = "/cgi-bin/s.py?q=" + $("#search").val().trim() + "&c=" + window.cluster;
    });
    function didYouMean(a){
if(a && a.trim()!==""){
console.log(a);
	$(".dym").removeClass("hide");
	$("#dym_val").text(" "+a);
	$("#dym_val").attr("href","http://srmsearchengine.in/cgi-bin/s.py?q="+a+"&c="+window.cluster);
}


}
window.hard=function(d){
                    var js = JSON.parse(d);
                    IDS = js["ids"];
		    didYouMean(js["Did You Mean: "]);
		    renderResult(js["results"],$("#search_results"));
};


    function getIdsResults(bool) {

        if ($("#search").val().trim() !== "") {
            if (window.cluster === "") {
	
                $.ajax({
                    async: bool,
                    url: "/cgi-bin/queryret/getIds.py",
		    data:{q:$("#search").val().trim().toLowerCase(),f:1},
                    dataType: 'text',
                    type: "GET",
                    error: function() {
                        //console.log("page not found");
                        window.results=false;
                    }

                }).done(function(text){
                try{
		  window.hard(text);
		  window.results=true;
		}
		catch(err){
			window.results=false;
		}
                });
		
            } else {

                $.ajax({
                    async: bool,
                    url: "/cgi-bin/queryret/getIds.py",
	            data:{q:$("#search").val().trim().toLowerCase(),f:1,c:window.cluster},
                    dataType: 'text',
                    type: "GET",
                    error: function() {
                    window.results=false;
                    }

                }).done(function(text) {
                   window.hard(text);
                   window.results=true;

                });

            }

        }

    }
function renderResult(arr,fat,wiki){
 if (arr[0]) {

 			if(wiki===""){
 				window.wiki=true;
 					window.wi+=1;
					window.wj+=1;
 				
 			}
 			else{
 			window.results = true;
                    window.i+=10;
                    window.j+=10; 			
 			}
                    
                    var main = $();
                    $.each(arr, function(index, element) {
                        var prnt = $("<div></div>");
                        prnt.addClass("search_result effect");
                        prnt.addClass("alpha-blur");
                        
                        var title = $("<div style=\"display:block;\"></div>");
                        titlea = $("<a></a>");
                        titlea.addClass("search_title");
			if(wiki===""){
			if($(".wiki_nav").length===0){
				fat.append("<div class=\"wiki_nav\"><nav class=\"navbar navbar-default\">  <div class=\"container-fluid\">    <div class=\"navbar-header\" style=\"float:left;\">      <a class=\"navbar-brand\" href=\"#\">        <img alt=\"Brand\" src=\"http://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Black_W_for_promotion.png/40px-Black_W_for_promotion.png\">      </a>      </div><div class=\"wiki_head\"><h4 style=\"float:left;\">Results from Wikipedia.org</h4></div>  </div></nav></div> ");
				}
				titlea.attr("href", "http://en.wikipedia.org/wiki/"+element["title"]);
				element['url']="http://en.wikipedia.org/wiki/"+element["title"];
				element['body']=element['body'].filter();
			}
			else{
				titlea.attr("href", element["url"]);
			}
			var g=element["title"].replace(/_/g," ").split(" ");
			if(g.length>10){  
				var ti=g.slice(0,10).join(" ")+" ...";
			}
			else{
				var ti=g.slice(0,10).join(" ");
			}
                        
                        titlea.text(ti.capitalizeMe());
                        title.append(titlea);
                        var imgspan = $("<div></div>");
imgspan.addClass("search_green");
                        imgspan.append(element["url"]);
var img=new Image();
var u="http://www.google.com/s2/favicons?domain=" + element['url'];
img.onload=function(){imgspan.prepend(img);prnt.find("p").after(imgspan);};
img.src=u;
img.width=15;
img.height=15;
$(img).css("margin-right","10px");
                       
                        var p = $("<p></p>");
                        p.addClass("search_info");
                        p.text(element["body"]);
                        prnt.append(title);
                        prnt.append(imgspan);
                        
                        prnt.append(p);
                        main = main.add(prnt);



                    });
                   
                    fat.append(main);
                    $(".effect").hide();
                    $(".effect").show("slow");
                    $(".effect").removeClass("effect");
			if(wiki===""){
			$(".wiki_more_btn").remove();
			var more_btn=$("<div class=\"wiki_more_btn container\" style=\"width:inherit;\"><div class=\"row\" style=\"height:60px;\">  <div class=\"alpha-blur col-lg-9 col-md-9 hidden-sm hidden-xs\" style=\"height:inherit;\"></div>  <div id=\"load_wiki\" class=\"col-lg-3 col-md-3 col-sm-12 col-xs-12 text-center\" style=\"cursor:pointer;height:inherit;padding-top:10px;	\">  <img src=\"http://www.google.com/s2/favicons?domain=http://en.wikipedia.org/\" width=\"20\" height=\"20\" style=\"margin-right: 10px;margin-top:5px;\"><span style=\"font-size:18px;color:#DDDDDD;top:5px;position:relative;\">More Results</span></div></div></div>");
			fat.append(more_btn);
			more_btn.on("click",function(){
			getResultswiki(window.wi,window.wj,true);
			
			
			});
			}
                    $("#loading").remove();
                    $(window).scroll(bindScroll);
                } else {
			if(!window.scrolled){
				if(!(IDSwiki.length>0 || IDSnews.length>0)){
					load.remove();
                        var prnt = $("<div><span></span></div>");
                        prnt.width($("#search_results").width());
                        prnt.addClass("h6 text-center no-results");
                        prnt.text("No more results available");
				}
			}
                    else if (window.results) {
                        load.remove();
                        var prnt = $("<div><span></span></div>");
                        prnt.width($("#search_results").width());
                        prnt.addClass("h6 text-center no-results");
                        prnt.text("No more results available");
                        fat.append(prnt);
                        window.results = false;
                    }

                }


}
    function getResultswiki(i, j, bool) {
    console.log(i);
    var r=IDSwiki.slice(i,j);
    console.log(r);
if(r.length!==0){
console.log("yes");
        
        
            $.ajax({
                url: "/cgi-bin/queryret/getMore.py",
                dataType: 'text',
                type: "GET",
                async: bool,
                data: {
                    q: "" + r.toString(),
		    f:"2"
                },
                error: function() {

                    load.remove();
                    var prnt = $("<div><span></span></div>");
                    prnt.width($("#search_results").width());
                    prnt.addClass("h6 text-center no-results");
                    prnt.text("No more results available");
                    load.remove();
                    $("#search_results").append(prnt);
                    window.wiki = false;


                }

            }).done(function(text) {
                var arr = JSON.parse(text);
               renderResult(arr["results"],$("#wikiMain"),"");
	

            });

        
}
else{
window.wiki=false;
                    $(".wiki_more_btn").remove();
    
    }
    }
    function getResultsResults(i, j, bool) {
if(i<IDS.length){
        if (IDS && window.results) {
            $.ajax({
                url: "/cgi-bin/queryret/getMore.py",
                dataType: 'text',
                type: "GET",
                async: bool,
                data: {
                    q: "" + IDS.slice(window.i, window.j).toString(),
		    f:"1"
                },
                error: function() {

                    load.remove();
                    var prnt = $("<div><span></span></div>");
                    prnt.width($("#search_results").width());
                    prnt.addClass("h6 text-center no-results");
                    prnt.text("No more results available");
                    load.remove();
                    $("#search_results").append(prnt);
                    window.results = false;


                }

            }).done(function(text) {
                var arr = JSON.parse(text);
console.log(arr);
               renderResult(arr["results"],$("#search_results"));


            });

        }
}
else{
 load.remove();
$(".no-results").remove();
                    var prnt = $("<div><span></span></div>");
                    prnt.width($("#search_results").width());
                    prnt.addClass("h6 text-center no-results");
                    prnt.text("No more results available");
                    load.remove();
                    $("#search_results").append(prnt);
                    window.results = false;
}



    }

    function bindScroll() {
    
        if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
       
            $(window).unbind('scroll');
            if (window.results) {
		window.scrolled=true;
                $("#search_results").append(load);
                $("#loading").width($("#search_results").width());
                setTimeout(function() {
                    getResultsResults(i, j, true);
                }, 1000);

            }

        }

    }
function getIdsWiki(bool){
 $.ajax({
                async: bool,
                url: "/cgi-bin/queryret/getIds.py",
                dataType: 'text',
                type: "GET",
                data: {
                    q: $("#search").val().trim().toLowerCase(),f:2,c:window.cluster
                },
                error: function() {
                }

            }).done(function(text) {
            try{
                var js = JSON.parse(text);
                IDSwiki=js["ids"];
		renderResult(js["results"],$("#wikiMain"),"");
		window.wiki=true;
		}
		catch(err){
		window.wiki=false;
		}

            });



}
function getIdsNews(bool){
 $.ajax({
                async: bool,
                url: "/cgi-bin/queryret/getIds.py",
                dataType: 'text',
                type: "GET",
                data: {
                    q: $("#search").val().trim().toLowerCase(),f:3,c:window.cluster
                },
                error: function() {
                }

            }).done(function(text) {
            try{
                var js = JSON.parse(text);
                IDSnews=js["ids"];
		renderResult(js["results"],$("#news"));
		window.news=true;
		}
		catch(err){
		window.news=false;
		}
            });



}
    function getSuggestedQuestions() {
        if ($("#search").val().trim() !== "") {
            //console.log("getSuggestedQuestions q:" + $("#search").val().trim().toLowerCase());
            $.ajax({
                async: true,
                url: "/cgi-bin/getQuestions.py",
                dataType: 'text',
                type: "GET",
                data: {
                    q: $("#search").val().trim().toLowerCase()
                },
                error: function() {
                    //console.log("err suggested");
                    $("#predefined_questions").removeClass("show");
                }

            }).done(function(text) {
                var arr = JSON.parse(text);
              //  console.log(arr);
                if (arr.length > 0) {
                    var prnt = $();
                    $.each(arr.slice(0,5), function(index, element) {
                        var a = $("<a></a>");
                        a.addClass("list-group-item");
                        a.addClass("list-group-item");
                        a.attr("href", "#");
                        a.text(element.capitalizeMe());
                        prnt = prnt.add(a);
                    });
                    $("#collapsee").append(prnt);
                    $("#predefined_questions").removeClass("hide");
                } else {
                    //console.log("No suggested questions !");
                    $("#predefined_questions").removeClass("show");
                }


            });
        }

    }

   window.getSmartAns=function() {
        if ($("#search").val().trim() !== "") {
            //console.log("getSmartAns q:" + $("#search").val().trim().toLowerCase());
            $.ajax({
                async: true,
                url: "/cgi-bin/new2/smart/getSmartAns.py",
                dataType: 'text',
                type: "GET",
                data: {
                    q: $("#search").val().trim().toLowerCase()
                },
                error: function() {
                    console.log("error smart ans");
                    $("#smart_answer").removeClass("show");
                  $("#smart_col").addClass("hide");
                     
                }

            }).done(function(textt) {
	try{
		$.ajaxSetup({cache:false});
                var js = JSON.parse(textt.replace(/\n/g, "").trim());
                if (!$.isEmptyObject(js)) {
                    $.each(js, function(key, val) {
                       window.val=val;
                        switch (key) {

                            case "general":
				$.getScript("/main/js/modules/general.js");
                                break;
                            case "sports":
                                $.getScript("/main/js/modules/sports.js");
                                break;
                            case "stock":
                                $.getScript("/main/js/modules/stocks.js");
                                break;
                            case "train":
                                $.getScript("/main/js/modules/train.js");
                                break;

                            case "weather":

                              $.getScript("/main/js/modules/weather.js");
                                break;
                            case "movie":
                               $.getScript("/main/js/modules/movie.js"); 
                            break;
                            case "exam":
			       $.getScript("/main/js/modules/exam.js");
				 
                            break;
                           case "location":
                              $.getScript("/main/js/modules/locations.js");
                            break;
                           case "minerals":
                               $.getScript("/main/js/modules/minerals.js");
			 break;
			 case "differences":
                               $.getScript("/main/js/modules/differences.js");	
			break;
			case "wiki":
                               $.getScript("/main/js/modules/wiki.js");
			 break;
			case "dict":
                            $.getScript("/main/js/modules/meaning.js");
			 break;
			case "theatre":
                               $.getScript("/main/js/modules/theater.js");
			 break;
			case "highway":
                               $.getScript("/main/js/modules/highway.js");
			 break;
			case "cricket-players":
				$.getScript("/main/js/modules/cricket.js");
			 break;
			 case "ministers":
				$.getScript("/main/js/modules/ministers.js");

			break;
			 case "bank":
				$.getScript("/main/js/modules/bank.js");

			break;
			case "site":
				$.getScript("/main/js/modules/site.js");

			break;
			case "highcourt":
				$.getScript("/main/js/modules/highcourt.js");

			break;
                            default:
                                $("#smart_answer").addClass("hide");
                            break;

                        }

                    });
                } else {

                    if ($("#search").val().trim().toLowerCase().indexOf('convert') > -1) {
                    
                            $.getScript("/main/js/modules/glaConv.js");
  			    $.getScript("/main/js/modules/metric.js");
  			     $.getScript("/main/js/modules/convert.js");
  			}		
                    console.log("No smart  ans questions !");
                    $("#smart_answer").addClass("hide");
   $("#smart_col").addClass("hide");
                  
                }

}
catch(err){
	  console.log("No smart  ans questions !");
                    $("#smart_answer").addClass("hide");
   $("#smart_col").addClass("hide");
		}
            });
        }

    };
    function getClusters() {
        if ($("#search").val().trim() !== "") {
            //console.log("getClusters q;:" + $("#search").val().trim().toLowerCase());
            $.ajax({
                async: true,
                url: "/cgi-bin/getClusters.py",
                dataType: 'text',
                type: "GET",
                data: {
                    q: $("#search").val().trim().toLowerCase()
                },
                error: function() {
                    console.log("error clusters");
                    window.clusters=[];
$(".side").removeClass("col-md-2 col-lg-2 hide");
$(".side").addClass("col-md-1 col-lg-1");
$("#centre_parent").parent().removeClass("col-lg-7 col-md-7 col-lg-pull-3 col-md-pull-3");
$("#centre_parent").parent().addClass("col-lg-8 col-md-8 col-lg-pull-3 col-md-pull-3");
$("#smart_col").parent().removeClass("col-lg-push-7 col-md-push-7 col-lg-3 col-md-3");
$("#smart_col").parent().addClass("col-lg-push-8 col-md-push-8 col-lg-3 col-md-3");
                }

            }).done(function(textt) {

                var arr = JSON.parse(textt);
                if (arr.length > 0) {
                    var main = $();
                    window.clusters = arr;
                    $.each(arr, function(index, element) {
if(element){
                        var li = $("<li></li>");
                        var a = $("<a></a>");
			li.addClass("alpha-blur");
			a.attr("data-toggle","tooltip");
			a.attr("data-placement","right");
			a.attr("title",element.capitalizeMe());
                        a.attr("href", "/cgi-bin/s.py?q="+window.query+"&c="+element);
                        a.text(element.capitalizeMe());
                        li.append(a);
                        main = main.add(li);
$(".side").removeClass("hide");
                        navChanger(); //for nav
}

                    });
                    $(".nav-sidebar").append(main);
		
                } else {
                    console.log("no clusters");
window.clusters=[];
                   $(".side").html("");
$(".side").removeClass("hide");
$(".side").removeClass("col-md-2 col-lg-2");
$(".side").addClass("col-md-1 col-lg-1");
$("#centre_parent").parent().removeClass("col-lg-7 col-md-7 col-lg-pull-3 col-md-pull-3");
$("#centre_parent").parent().addClass("col-lg-8 col-md-8 col-lg-pull-3 col-md-pull-3");
$("#smart_col").parent().removeClass("col-lg-push-7 col-md-push-7 col-lg-3 col-md-3");
$("#smart_col").parent().addClass("col-lg-push-8 col-md-push-8 col-lg-3 col-md-3");
                }


            });
        }

    }

   


    //fix scroll later
    $(window).bind('scroll', bindScroll);
    getIdsResults(true);
    getIdsWiki(true);
    getIdsNews(true);
    getSuggestedQuestions();
    window.getSmartAns();
    getClusters();

});

  

   String.prototype.capitalizeMe=function() {
try{
        return this.charAt(0).toUpperCase() + this.substr(1).toLowerCase();
}
catch(err){
return "";
}
    }; 
   String.prototype.filter=function() {
try{
	data = this + " ";
	//approved by sai prashanth
	data = data.replace(/®/g, " ").replace(/©/g, " ").replace(/[\.\,-\/#!<>?$%\^&\*;:\+{}=\-_`~()\[\]]/g, " ").replace(/\\u.*\s/g, " ").replace(/\\n+/g, " ").replace(/\\t+/g, " ").replace(/\\r+/g, " ").replace(/\\x.*\s/g, " ").replace(/\\/g,"").replace(/\'/g,"").replace(/\"/g,"").replace(/\\/g,"").replace(/\s+/g, " ").replace(/\|/g,' ').replace(/redirect/g,' ').trim();

	return data;
}
catch(err){
return "";
}
    };
$.prototype.setTextValue=function(t){
if(t===""||t===undefined){
//console.log("empty");
$(this).remove();

}
else{
$(this).text(t);

}


};
$.prototype.setHtmlValue=function(t,test){

if(test===""||test===undefined){

$(this).remove();


}
else{
$(this).html(t);

}


};
window.asyncImage=function(src1,w,h){
var img=new Image();
img.width=w;
img.height=h;
img.src=src1;
return $(img);
};
