if($("#exams").length===0){
var exam=$("<div id=\"exams\" class=\"well alpha-blur hide\" style=\"margin-top:20px;border:0px;color:white;\"><div class=\"row\"><div class=\"col-lg-12\" style=\"text-align:center;\"><img id=\"book\" src=\"\" height=\"62\" width=\"65\"></div></div><div class=\"row\" id=\"exam_name\" style=\"text-align:center;\"><h3><span></span></h3></div><div class=\"row\" id=\"exam_full_name\" style=\"text-align:center;\"><span><b></b></span></div><div class=\"row\" id=\"exam_course\" style=\"text-align:center;\"><b>Course - </b><span></span></div><div class=\"row\" id=\"exam_pattern\" style=\"text-align:center;\"><b>Pattern - </b><span></span></div> <div class=\"row\" id=\"exam_date\" style=\"text-align:center;\"><b>Date - </b><span></span></div><div class=\"row\" style=\"text-align:center;\"><div class=\"col-lg-12\" id=\"colleges\"><ul class=\"list-group\"><br></ul></div></br><button style=\"color:white;\" class=\"btn-group btn-group-xs btn btn-primary glyphicon glyphicon-chevron-down\" id=\"exams_button\" style=\"color:black;top:5px;\" data-toggle=\"tooltip\" data-placement=\"bottom\" title=\"Click to see more\"></button> </div></div>");
$("#smart_col").html("").append(exam);
$("#book").attr("src","/ver1/images/book.png");
                            $("#smart_answer").addClass("hide");
$("#smart_col").removeClass("hide");
                            $("#exams").removeClass("hide");
                                $("#exam_name > h3 >span").text(window.val["name"]);
                                $("#exam_full_name >span >b").text(window.val["fullform"]);
                                $("#exam_course>span").text(window.val["course"]);
                                $("#exam_pattern>span").text(window.val["pattern"]);
                                $("#exam_date>span").text(window.val["date"]);
                                $.each(JSON.parse(window.val["colleges"]),function(index,element){

                                $("#colleges >ul").append($("<li class=\"list-group-item alpha-blur\">"+element.capitalizeMe()+"</li>"));




});
cycle2=0;
 $("#exams_button").click(
        function() {
		$("#exams_button").toggleClass("glyphicon-chevron-down glyphicon-chevron-up");

            $("#colleges").slideToggle(function(){
    		if(cycle2===0){
	    		$("#exams_button").attr("title","Click to see less");
			++cycle2;
			}
		else{
			$("#exams_button").attr("title","Click to see more");

			cycle2=0;
		}
});
});
}
