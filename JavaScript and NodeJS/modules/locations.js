if($("#location").length===0){
var l=$("<div id=\"location\" class=\"col-lg-12 well alpha-blur alpha-shadow hide\" style=\"border:0px;margin-top:20px;\">                  <div class=\"row\">                     <div class=\"col-lg-12\" style=\"text-align:center;\">                        <img id=\"locationimg\" src=\"\"  height=\"62\" width=\"65\">                     </div>                  </div>                                                     <div class=\"row\">                     <div id=\"location_name\" class=\"col-lg-12\" style=\"font-size:14px;text-align:center;word-break:none;color:white;\"></div>                  </div>                  <div class=\"row\" style=\"text-align:center;color:white;\">                     <span id=\"location_city\" style=\"font-size:25px;\"></span><span id=\"location_state\" style=\"font-size:25px;\"></span>                  </div><div class=\"row\" style=\"text-align:center;color:white;\">                     <span id=\"location_address\" style=\"font-size:25px;\"></span></span>                  </div><div class=\"row\" style=\"text-align:center;color:white;\">                     <span id=\"location_description\" style=\"font-size:25px;\"></span></span>                  </div><div class=\"row\" style=\"text-align:center;color:white;\">                     <span id=\"location_co\" style=\"font-size:25px;\"></span></span></br>                  </div>                  <div class=\"row\" style=\"text-align:center;\">                     <div style=\"float:left;width:50&percnt;;height:34px;\">                        <button id=\"location_prev\" style=\"background-color:#008EFF;\" class=\"btn btn-primary glyphicon glyphicon-chevron-left\" value=\"Previous\"/>                     </div>                     <div style=\"float:left;width:50&percnt;;height:34px;\">                     <button id=\"location_next\" style=\"background-color:#008EFF;\" class=\"btn btn-primary glyphicon glyphicon-chevron-right\" value=\"Next\"/>                     </div>                  </div>               </div>");

$("#smart_col").html("");
$("#smart_col").append(l);
$("#location").on("click", "#location_next", function() {

        if (window.locations.length > 1 && window.clocation < (window.locations.length - 1)) {
            ++window.clocation;
            var val = window.locations[window.clocation];
            $("#location_prev").removeAttr("disabled");
            var name = val['name'];
                                var city=val['city'];
                                var state=val['state'];
                                var loc=val["loc"];
                                var description=val["description"];
                                var address=val["address"];
                                var type=loc["type"];
                                var co=loc["coordinates"];
                                $("#locationimg").attr("src","/ver1/images/hotel.png");
                                $("#location_name").setHtmlValue("<h3>"+name.capitalizeMe()+"</h3>",name);
                                $("#location_city").setHtmlValue("<h4>"+city.capitalizeMe()+"</h4>",city);
                                $("#location_state").setHtmlValue("<h4>"+state.capitalizeMe()+"</h4>",state);
                                $("#location_address").setHtmlValue("<h5>"+address.capitalizeMe()+"</h5>",address);

$("#location_description").setHtmlValue("<h5>"+description.capitalizeMe()+"</h5>",description);
$("#location_co").setHtmlValue("<h5>"+(type+" "+co).capitalizeMe()+"</h5>",type+co);
            $("#location").removeClass("hide");
            $("#smart_answer").addClass("hide");
        }
        if ((window.clocation === (window.locations.length - 1)) && (window.locations.length !== 1)) {
            $("#location_next").attr("disabled", "disabled");
            $("#location_prev").removeAttr("disabled");

        }
    });
$("#location").on("click", "#location_prev", function() {



        if (window.locations.length > 1 && window.clocation < window.locations.length && window.clocation !== 0) {


            --window.clocation;
            //console.log(window.ctrain);
            val = window.locations[window.clocation];
             var name = val['name'];
                                var city=val['city'];
                                var state=val['state'];
                                var loc=val["loc"];
                                var description=val["description"];
                                var address=val["address"];
                                var type=loc["type"];
                                var co=loc["coordinates"];
                                $("#locationimg").attr("src","/ver1/images/hotel.png");
                                $("#location_name").setHtmlValue("<h3>"+name.capitalizeMe()+"</h3>",name);
                                $("#location_city").setHtmlValue("<h4>"+city.capitalizeMe()+"</h4>",city);
                                $("#location_state").setHtmlValue("<h4>"+state.capitalizeMe()+"</h4>",state);
                                $("#location_address").setHtmlValue("<h5>"+address.capitalizeMe()+"</h5>",address);
$("#location_description").setHtmlValue("<h5>"+description.capitalizeMe()+"</h5>",description);
//$("#location_co").setHtmlValue("<h5>"+(type+" "+co).capitalizeMe()+"</h5>",type+co);
            $("#location_next").removeAttr("disabled");
            $("#smart_answer").addClass("hide");
        }
        if (window.clocation === 0) {
            //console.log("0s");
            $("#location_prev").attr("disabled", "disabled");
            $("#location_next").removeAttr("disabled");
        }

    });

window.locations = window.val;
                                window.val = window.val[0];

                                if (window.locations.length === 1) {
                                    $("#location_next").attr("disabled", "disabled");
                                    $("#location_prev").attr("disabled", "disabled");
                                }          
                                var name = window.val['name'];
                                var city=window.val['city'];
                                var state=window.val['state'];
                                var loc=window.val["loc"];
                                var description=window.val["description"];
                                var address=window.val["address"];
                                var type=loc["type"];
                                var co=loc["coordinates"];

                                $("#locationimg").attr("src","/ver1/images/hotel.png");

                                $("#location_name").setHtmlValue("<h3>"+name.capitalizeMe()+"</h3>",name);

                                $("#location_city").setHtmlValue("<h4>"+city.capitalizeMe()+"</h4>",city);

                                $("#location_state").setHtmlValue("<h4>"+state.capitalizeMe()+"</h4>",state);
                               //problem with db $("#location_address").setHtmlValue("<h5>"+address.capitalizeMe()+"</h5>",address);
$("#location_description").setHtmlValue("<h5>"+description+"</h5>",description);
$("#location_co").setHtmlValue("<h5>"+(type+" "+co)+"</h5>",type+co);

                                $("#location").removeClass("hide");
                                $("#smart_answer").addClass("hide");
$("#smart_col").removeClass("hide");
}
