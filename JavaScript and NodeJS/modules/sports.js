if($("#sports").length===0){
var sports=$("  <div id=\"sports\" class=\"col-lg-12 well alpha-blur hide alpha-shadow\" style=\"border:0px;color:white;margin-top:20px;\">               <div class=\"row\" style=\"text-align:center;\">               <div class=\"col-lg-5 col-md-5 col-sm-5 col-xs-5 \"><span class=\"h5\" id=\"sport_title1\"></span></br><span class=\"h6\" id=\"team1score\"></span></div>               <div class=\"col-lg-2 col-md-2 col-sm-2 col-xs-2\"><h4 id=\"sports_teams_style\" style=\"color:#ecf0f1\">v/s</h4></div>               <div class=\"col-lg-5 col-md-5 col-sm-5 col-xs-5\"><span class=\"h6\" id=\"sport_title2\"></span></br><span class=\"h5\" id=\"team2score\"></span></div>               </div>               <!--div class=\"row\">                  <h2 style=\"position:relative;margin:5px;color:#000;text-align:center;\">                  <span id=\"stocks_current\" style=\"color:white;\">229</span>                  (<span style=\"color:#cccccc;font-weight: 300 ;\">300</span>)                  </h2>                  </div-->               <div class=\"row\" id=\"sports_status\">               <br><br>               <div id=\"sport_desc\" class=\"col-lg-12\" style=\"text-align:center;\">Australia bowled well overall today but the Indian batsmen were up for the challenge once again. Starc and Watson have two wickets so far while Lyon has one.Cheers!</div></div>               <div class=\"row\" id=\"sports_details\">               <hr>               <div class=\"col-lg-12\" style=\"color:#2ecc71;\">               <div class=\"col-lg-2 col-md-2 col-sm-2 col-xs-2\"><img class=\"batimg\" src=\"\" alt=\"Smiley face\" height=\"42\" width=\"42\"></div>               <div class=\"col-lg-4 col-md-4 col-sm-4 col-xs-4\" style=\"text-align:left;padding:0px;top:10px;left:4px;\"><span id=\"bat1\">Sehwag*</span></br><span id=\"bat1score\"></span></div>               <div class=\"col-lg-2 col-md-2 col-sm-2 col-xs-2\"><img class=\"batimg\" src=\"\" alt=\"Smiley face\" height=\"42\" width=\"42\"></div>               <div class=\"col-lg-4\" style=\"text-align:left;padding:0px;top:10px;left:4px;\"><span id=\"bat2\">Sachin</span></br><span id=\"bat2score\"></span></div>               </div>               <div class=\"col-lg-12\" style=\"text-align:center;\"><div class=\"row\" style=\"display:block;margin-left;auto;margin-right;auto;text-align:center;\">               <img id=\"ballimg\" src=\"\" alt=\"Smiley face\" height=\"42\" width=\"42\"/><span id=\"bowl\">Brett Lee</span></div><div class=\"row\"><span id=\"overs\"></span></div>               </div>               </div>               <div class=\"row\" style=\"color:#999999;text-align:center;\">               <button class=\"btn btn-primary glyphicon glyphicon-chevron-down\" id=\"sports_button\" style=\"color:white;top:5px;\" data-toggle=\"tooltip\" data-placement=\"bottom\" title=\"Show more details\"></button>               </div>                </div>");
$("#smart_col").html("").append(sports);
$("#smart_answer").addClass("hide");

                                var patt = /\d+/;
                                //console.log(window.val);
$(".batimg").attr("src","/ver1/images/bat.png");
$("#ballimg").attr("src","/ver1/images/ball.png");
if(window.val["Batting"].indexOf("&")>=0){
                                var batsmen_1_score = window.val["Batting"].split("&")[0].match(patt)[0];
                                var batsmen_1_name = window.val["Batting"].split("&")[0].replace(batsmen_1_score, "").trim();

          
                      var batsmen_2_score = window.val["Batting"].split("&")[1].match(patt)[0];
                                var batsmen_2_name = window.val["Batting"].split("&")[1].replace(batsmen_2_score, "").trim();
}
else{
var batsmen_1_score = window.val["Batting"].match(patt)[0];
                                var batsmen_1_name = window.val["Batting"].replace(batsmen_1_score, "").trim();
var batsmen_2_name="";
var batsmen_2_score ="";
$(".batimg")[1].remove();
}

				var w=window.val["General"].replace(/[/]/g,"");
                                var team1 = window.val["General"].split("/", 1)[0].replace(window.val["General"].split("/", 1)[0].trim().match(patt)[0], "");
                                var team2 = w.split(" v ")[1].replace(w.split(" v ")[1].trim().match(patt)[0], "").replace("*","").trim();

                           //     team2 = team2.split("/", 1)[0];
                                var team1score = window.val["General"].split(" v ")[0].replace(team1, "").trim();
				
                                var team2score = window.val["General"].split(" v ")[1].replace(team2, "").trim();
				
                              //  var team2 = window.val["General"].split(" v ")[1].split(" ")[0];
                                var title1 = window.val["General"].split(" v ")[0];
                                var title2 = window.val["General"].split(" v ")[1];
                                var bowling = window.val["Bowling"];
                                var overs = window.val["Overs"];
                                var description = "<b>" + window.val["Status"] + "<br/><br/>" + window.val["Description"];
                                $("#bat1").text(batsmen_1_name + "*");
                                $("#bat2").text(batsmen_2_name);
                                $("#bat1score").text(batsmen_1_score);
                                $("#bat2score").text(batsmen_2_score);
                                $("#sport_desc").html(description);
                                $("#bowl").text(bowling);
                                $("#overs").text("Overs " + overs);
                                $("#sport_title1").text(team1);
                                //console.log(team2);
                                $("#sport_title2").text(team2);
                                $("#team1score").text(team1score);
                                $("#team2score").text(team2score);
                                $("#sports").removeClass("hide");
                                $("#smart_answer").addClass("hide");
$("#smart_col").removeClass("hide");
cycle1=0;
$("#sports_details").hide();
$("#sports_button").click(
        function() {
		$("#sports_button").toggleClass("glyphicon-chevron-down glyphicon-chevron-up");

            $("#sports_details").slideToggle(function(){
    		if(cycle1===0){
	    		$("#sports_button").attr("title","Click to see less");
			++cycle1;
			}
		else{
			$("#sports_button").attr("title","Click to see more");

			cycle1=0;
		}
});
});
}
