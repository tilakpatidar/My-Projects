function main(){
if($("#theater").length===0){
var theater=$("<div class=\"well alpha-blur\" style=\"border:0px;color:white;text-align:left;\" id=\"theater\">    <div class=\"container-fluid box\">        <div class=\"row row_data\" style=\"height:100%;\">            <div class=\"col-lg-3 col-md-3\" style=\"height:100%;padding-left:0px;\"><img id=\"img_link\" style=\"display:block;margin-left:auto;margin-right:auto;\" class=\"\"/>            </div>            <div class=\"col-lg-9 col-md-9\" style=\"height:100%;\">                <div class=\"topcrop2\">                        <div class=\"moviedesc\">                            <div class=\"movietitle\"></div>     <div class=\"theatre_name\"></div>                     </div>                                                       <table class=\"minfo\" style=\"padding-top:10px;\"><td>Locations Available</td><td><div class=\"dropdown\">  <button class=\"btn btn-default dropdown-toggle\" type=\"button\" id=\"loc\" data-toggle=\"dropdown\" aria-expanded=\"true\">  Locations    <span class=\"caret\"></span>  </button>  <ul class=\"dropdown-menu\" id=\"loc-ul\" role=\"menu\" aria-labelledby=\"dropdownMenu1\">   </ul></div> </td></table>                    </div> <div id=\"theatre_toggle\" class=\"hide\">                              <div class=\"\" style=\"padding-top:20px;\">                    <div class=\"table-responsive\">                        <table style=\"width:100%;\">                            <tbody class=\"time-table\">                                <tr style=\"height:30px;\">                                    <td>Theatre</td><td>                                    Show Times</td> </tbody>                        </table>                    </div>                </div>   </div>         </div>        </div>    </div>");
var m=window.val[0];
$("#predefined_questions").before(theater);
$("#loc").css({'color':'whitesmoke','background-color':'#2d2d2d'});
$("#img_link").attr("src",m["img_link"]);
$(".minfo").append("<tr style=\"height:30px;\"><td style=\"width:100px;\">Rating </td><td>"+m["rating"]+"</td></tr>");
$(".minfo").append("<tr style=\"height:30px;\"><td style=\"width:100px;\">Director </td><td>"+m["director"]+"</td></tr>");
+$(".minfo").append("<tr style=\"height:30px;\"><td style=\"width:100px;\">Duration </td><td>"+m["duration"]+"</td></tr>");
$(".minfo").append("<tr style=\"height:30px;\"><td style=\"width:100px;\">Release Date </td><td>"+m["rel_date"]+"</td></tr>");
$(".minfo").append("<tr style=\"height:30px;\"><td style=\"width:100px;\">Genre </td><td>"+m["genre"]+"</td></tr>");
$(".minfo").append("<tr style=\"height:30px;\"><td style=\"width:100px;\">City </td><td>"+m["city"]+"</td></tr>");
$(".minfo").append("<tr style=\"height:30px;\"><td style=\"width:100px;\">Language </td><td>"+m["language"]+"</td></tr>");
//$(".minfo").append("<tr style=\"height:30px;\"><td>Time </td><td>"+JSON.parse(m["times"].replace(/\\/g,"")).join(" ")+"</td></tr>");
$(".minfo").append("<tr style=\"height:30px;\"><td>Cast </td><td>"+m["cast"]+"</td></tr>");
console.log(m["avai_cities"]);
$.each(window.val,function(k,v){
var times=eval(v["times"].replace(/\\'/g,'"'));
$(".time-table").append(" <tr style=\"border-top:1px solid;width:100%;\"><td>"+v["theatrename"]+"</td><td>"+times.join(" ").filter().capitalizeMe()+"</td></tr>");
});
$("#loc-ul").on('click',"li",function(){

var city=$("#search").val().replace(m["city"],$(this).find("a").text());
	$.ajax({
                    async: true,
                    url: "/cgi-bin/new2/smart/getSmartAns.py",
		    data:{q:city},
                    dataType: 'text',
                    type: "GET",
                    error: function() {
                        //console.log("page not found");
                    }

                }).done(function(text){
			$("#theater").remove();
		        window.val=JSON.parse(text)["theatre"];
			main();


                });
});
$.each(m["avai_cities"].sort(),function(index,e){

 
$("#loc-ul").append("<li role=\"presentation\"><a role=\"menuitem\" tabindex=\"-1\" href=\"#\">"+e.capitalizeMe()+"</a></li> ");


});
$(".row_data").after("<div id=\"ttgl\" style=\"cursor:pointer;text-align:center;height:40px;font-size:18px;padding-top:10px;padding-bottom:10px;\" class=\"row\">Show More</div>");
$("#theatre_toggle").prepend("<div style=\"margin-top:35px;\">"+m["synopsis"]+"</div>");
$(".movietitle").css({'font-size':'25px','font-weight':'400','padding-bottom':'10px'});
$(".theatre_name").css({'font-size':'18px','font-weight':'400','padding-bottom':'10px'});
var tt=0;
$("#ttgl").on("click",function(){
if(tt===0){
$("#theatre_toggle").removeClass("hide");
$("#ttgl").text("Show Less");
++tt;}
else{
$("#theatre_toggle").addClass("hide");
$("#ttgl").text("Show More");
tt=0;}
});
$(".movietitle").text(m["moviename"].capitalizeMe());
$(".time-table").find("td").css({'padding-top':'10px','padding-bottom':'10px'});
$("#smart_answer").addClass("hide");
$("#smart_col").removeClass("hide");
}
}
main();
