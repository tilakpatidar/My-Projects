if($("#weather").length===0){

var weather = $("<div class=\"col-md-12 well hide alpha-blur alpha-shadow\" id=\"weather\" style=\"color:white;margin-top:20px;border:0px;\">                  <div class=\"row\">                                         <div class=\"col-lg-7 col-md-7 col-sm-7 col-xs-7\" id=\"weather\">                        <div style=\"font-size:20px;font-weight:bold;text-align: left;color:white\" id=\"weather_city\">Chennai</div>                                             </div>                     <div class=\"col-lg-5 col-md-5 col-sm-5 col-xs-5\">                        <img width=\"60\" height=\"60\" id=\"img_today\"  src=\"\">                         <div style=\"color:white;font-size:18px;\" id=\"weather_max\"></div>                     </div>                                       </div>                                                                             <div class=\"row\" id=\"weather_details\" style=\"color:white;\">                   <div class=\"col-lg-12\">                   <hr>                  <table class=\"table\">                  <tbody>                   <tr>                  <td class=\"h5\">                  Today Sunset&nbsp;                  </td>                  <td id=\"weather_today_sunset\">                  </td>                  </tr>                  <tr>                  <td class=\"h5\">                  Tomorrow Sunrise&nbsp;                  </td>                  <td id=\"weather_tomorrow_sunrise\">                  </td>                  </tr>                  <tr>                  <td class=\"h5\">                  Today Moonrise&nbsp;                  </td>                  <td id=\"weather_moonrise\">                  </td>                  </tr>                  <tr>                  <td class=\"h5\">                  Tomorrow Moonset&nbsp;                  </td>                  <td id=\"weather_moonset\">                  </td>                  </tr>                  </tbody>                  </table>                  <hr>                  </div>                                       <div class=\"col-lg-12\" id=\"days_weather\" style=\"\">                                            </div>                                          <div class=\"col-lg-4\"></div>                     <div class=\"col-lg-4\"></div>                     <div class=\"col-lg-12\" style=\"text-align:center;\">                     </div>                  </div>                  <div class=\"row\" style=\"color:#999999;text-align:center;\">                     <button id=\"weather_button\" style=\"color:black;top:5px;color:white;\" data-toggle=\"tooltip\" data-placement=\"bottom\" title=\"Click to see more statistics\" class=\"btn btn-primary glyphicon glyphicon-chevron-down\"></button>                  </div>               </div>");
$("#smart_col").html("");
$("#smart_col").append(weather);
$("#weather_details").hide();
cycle=0;
    $("#weather_button").click(
        function() {
		$("#weather_button").toggleClass("glyphicon-chevron-down glyphicon-chevron-up");

            $("#weather_details").slideToggle(function(){
    		if(cycle===0){
	    		$("#weather_button").attr("title","Click to see less statistics");
			++cycle;
			}
		else{
			$("#weather_button").attr("title","Click to see more statistics");

			cycle=0;
		}
});
});
var imgs=["clear sky","clear","haze","light rain","mainly clearly sky","mainly or generally cloudy sky","mainly or generally cloudy sky with possibility of rain","mist","moderate rain","moderate snow","partly cloud sky with possibility of rain or thunder","partly cloudy","partly cloudy sky","partly cloudy sky with thundery development","rain or snow","thunderstorm with rain","fog"];

                                $.each(imgs,function(index,element){

                                if(window.val['forecast'].indexOf(element)>-1){
                                $("#img_today").attr("src","/main/images/"+window.color+"/"+element+".png");
                                $("#img_today").css("-webkit-filter","invert(100%)");
$("#img_today").css("-moz-filter","invert(100%)");
}




});

                                var city = window.val['City'];
                                var maxx = window.val['Maximum'];
                                var minn = window.val['Minimum'];
                                var moonrise = window.val['Moonrise'];
                                var moonset = window.val['Moonset'];
                                var rainfall = window.val['Rainfall'];
                                var today_sunset = window.val['Today_Sunset'];
                                var tomorow_sunrise = window.val['Tomorrow_Sunrise'];
                                var forecast = window.val['forecast'];
                                var days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
                                var today = days.indexOf(window.val["day"]);
                                var future = window.val["future"];
				$("#weather_city").text(city);
				$("#weather_city").append("<br/>");
console.log("sdf");
				$("#weather_city").append("<span style=\"font-weight:400;font-size:0.65em;line-height:1.3em;max-width:200px;display:block;\">"+window.val["forecast"].capitalizeMe()+"</span>");
console.log("sdf");
                                var w = [];
                                var i = 0;
                                var row = $("<div></div>");
                                row.addClass("row");
                                while (i <= 3) {
                                    ++today;
                                    if (today > 6) {
                                        today = 0;
                                    }




                                    var d = $("<div></div>");
                                    d.addClass("col-lg-6");
                                    d.css({
                                        "font-size": "16px"
                                    });

                                    var img = $("<img></img>");
 $.each(imgs,function(index,element){

                                if(future[i]['forecast'].indexOf(element)>-1){

                                img.attr("src","/main/images/"+window.color+"/"+element+".png");
                                img.css("-webkit-filter","invert(100%)");

}




});
                                    img.attr("width", "60");
                                    img.attr("height", "60");
                                    img.css({
                                        "display": "block",
                                        "margin-left": "auto",
                                        "margin-right": "auto"
                                    });
                                    d.append(img);
                                    var s = $("<span style=\"display:block;text-align:center;\">" + days[today] + "</span>");
                                    d.append(s);
                                    var l = $("<span style=\"display:block;text-align:center;\">" + future[i]["maximum"] + "/" + future[i]["minimum"] + "<sup>&deg;C</sup>" + "</span>");
                                    d.append(l);
                                    row.append(d);
                                    if (i == 1) {
                                        $("#days_weather").append(row);
                                        var row = $("<div></div>");
                                        row.addClass("row");


                                    }



                                    ++i;

                                }
                                $("#days_weather").append(row);
                                $("#weather_max").html(maxx + "/" + minn + "<sup>&deg;C</sup>");
                                $("#weather_moonrise").text(moonrise);
                                $("#weather_moonset").text(moonset);
                                $("#weather_today_sunset").text(today_sunset);
                                $("#weather_tomorrow_sunrise").text(tomorow_sunrise);

                                $("#weather").removeClass("hide");
                                $("#smart_answer").addClass("hide");
$("#smart_col").removeClass("hide");
}
