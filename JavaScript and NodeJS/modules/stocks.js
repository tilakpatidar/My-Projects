if($("#stocks").length===0){
var stocks=$("<div id=\"stocks\" class=\"col-lg-12 well hide alpha-blur alpha-shadow\" style=\"color:white;margin-top:20px;border:0px;\">               <h4 style=\"position:relative;left:10px;\" id=\"stocks_name\">Apple Inc</h4>                 <h6 style=\"position:relative;left:10px;top:-7px;margin:0px;\" id=\"stocks_code\">NASDAQ: AAPL</h6>                <h5 style=\"position:relative;left:10px;top:-5px;margin:0px;\">Pre-market:               <span id=\"stocks_previous\">109.2</span>               </h5>               <h2 style=\"position:relative;margin:5px;color:white;text-align:center;\">               <span id=\"stocks_current\" >110</span>               <span style=\"color:#e74c3c\">               <span id=\"stocks_status\" style=\"position:relative;font-size:28px;top:-5px;left:6px;\">&#8595;</span>               <span id=\"stocks_percentage\">2.67</span>&#37;               </span>               </h2>               </div>");
$("#smart_col").html("").append(stocks);
$("#stocks2").attr("src","/ver1/images/stocks2.png");
                                $("#smart_answer").addClass("hide");
                                if(window.val["Status"]==="Gain")
{
$("#status_color").css("color","#01DF01");
$("#stocks_status").html("&uarr;");
}
else{
$("#status_color").css("color","#e74c3c");
$("#stocks_status").html("&#8595;");


}
$("#stocks_percentage").html(window.val["Percentage Change"].replace("+","").replace("-",""));
$("#stocks_current").text(window.val["Present window.value"]);
$("#stocks_name").text(window.val["Company Name"]);
$("#stocks_previous").text(window.val["Previous window.value"]);
$("#stocks").removeClass("hide");
$("#smart_col").removeClass("hide");
}
