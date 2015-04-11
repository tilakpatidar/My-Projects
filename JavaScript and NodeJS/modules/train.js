if($("#train").length===0){
window.ctrain = 0;
var train=$("<div id=\"train\" class=\"col-lg-12 well alpha-blur alpha-shadow hide\" style=\"margin-top:20px;border:0px;\">                  <div class=\"row\">                     <div class=\"col-lg-12\" style=\"text-align:center;\">                        <img id=\"trainimg\" src=\"\"  height=\"62\" width=\"65\">                     </div>                  </div>                  <div class=\"row\" style=\"color:white;\">                     <div class=\"col-lg-5 col-md-5 col-sm-5 col-xs-5\" id=\"train_source\" style=\"font-size:20px;text-align:right;\"></div>                     <div class=\"col-lg-2 col-md-2 col-sm-2 col-xs-2\" style=\"font-size:14px;top:5px;\">To</div>                     <div class=\"col-lg-2 col-md-2 col-sm-2 col-xs-2\" id=\"train_dest\" style=\"font-size:20px;text-align:left;\"></div>                  </div>                  <div class=\"row\" id=\"\" style=\"padding:0px;color:white;font-weight:bold;\">                     <div id=\"src_time\" class=\"col-lg-6 col-md-6 col-sm-6 col-xs-6\" style=\"text-align:center;\"></div>                     <div class=\"col-lg-2\"></div>                     <div id=\"dest_time\" class=\"col-lg-6 col-md-6 col-sm-6 col-xs-6\" style=\"text-align:center;paddding-bottom:5px !important;paddding-top:5px !important;\"></div>                  </div>                  <div class=\"row\">                     <div id=\"train_name\" class=\"col-lg-12\" style=\"font-size:14px;text-align:center;word-break:none;color:white;\"></div>                  </div>                  <div class=\"row\" style=\"text-align:center;\">                     <span id=\"train_time\" style=\"color:#e74c3c;font-size:25px;\"></span>                  </div>                  <div class=\"row\" style=\"text-align:center;\">                     <div style=\"float:left;width:50&percnt;;height:34px;\">                        <button id=\"train_prev\" style=\"background-color:#008EFF;\" class=\"btn btn-primary glyphicon glyphicon-chevron-left\" value=\"Previous\"/>                     </div>                     <div style=\"float:left;width:50&percnt;;height:34px;\">                     <button id=\"train_next\" style=\"background-color:#008EFF;\" class=\"btn btn-primary glyphicon glyphicon-chevron-right\" value=\"Next\"/>                     </div>                  </div>               </div>"); 
$("#smart_col").html("").append(train);
$("#train").on("click", "#train_next", function() {

        if (window.trains.length > 1 && window.ctrain < (window.trains.length - 1)) {
            ++window.ctrain;
            //console.log(window.ctrain);
            var val = window.trains[window.ctrain];
            $("#train_prev").removeAttr("disabled");
            var desc = val['Description'];
            var status = val['Status'];
            var status_description = val['Status Description'];
            var train_name = val['Train Name'];
            var source = val['Description'].replace("Departed from", "").trim().split("at")[0];
            var dest = val['Description'].split("Destination")[1].split("at")[0];
            //console.log(dest);
            //console.log(source);
            //console.log(train_name);
            var src_time = val['Description'].split(' at ')[1].split('on')[0];
            var dest_time = val['Description'].split(' at ')[2].split('on')[0];
            $("#train_source").html(source.replace("(", "<h6>(").replace(")", ")</h6>"));
            var date1 = val['Description'].split(',')[0].split("on")[1].trim();
            var month1 = val['Description'].split(',')[1];
            var date2 = val['Description'].split(",")[2].split(" at ")[1].split("on")[1].trim();
            var month2 = val['Description'].split(",")[3].trim();
            //console.log(date2 + " " + month2);
            $("#dest_time").text(dest_time + " " + date2 + " " + month2);
            //console.log(src_time);
            //console.log(dest_time);
            $("#src_time").text(src_time + " " + date1 + " " + month1);
            var statustrain = val["Status Descrition"];
            //Will do later
            $("#train_dest").html(dest.replace("(", "<h6>(").replace(")", ")</h6>"));
            $("#train_time").text(status);
            $("#train_name").text(train_name);
            $("#train").removeClass("hide");
            $("#smart_answer").addClass("hide");
        }
        if ((window.ctrain === (window.trains.length - 1)) && (window.trains.length !== 1)) {
            $("#train_next").attr("disabled", "disabled");
            $("#train_prev").removeAttr("disabled");

        }
    });

 $("#train_prev").attr("disabled", "disabled");
    $("#location_prev").attr("disabled", "disabled");
    $("#train").on("click", "#train_prev", function() {



        if (window.trains.length > 1 && window.ctrain < window.trains.length && window.ctrain !== 0) {


            --window.ctrain;
            //console.log(window.ctrain);
            val = window.trains[window.ctrain];
            var desc = val['Description'];
            var status = val['Status'];
            var status_description = val['Status Description'];
            var train_name = val['Train Name'];
            var source = val['Description'].replace("Departed from", "").trim().split("at")[0];
            var dest = val['Description'].split("Destination")[1].split("at")[0];
            //console.log(dest);
            //console.log(source);
            //console.log(train_name);
            var src_time = val['Description'].split(' at ')[1].split('on')[0];
            var dest_time = val['Description'].split(' at ')[2].split('on')[0];
            $("#train_source").html(source.replace("(", "<h6>(").replace(")", ")</h6>"));
            var date1 = val['Description'].split(',')[0].split("on")[1].trim();
            var month1 = val['Description'].split(',')[1];
            var date2 = val['Description'].split(",")[2].split(" at ")[1].split("on")[1].trim();
            var month2 = val['Description'].split(",")[3].trim();
            //console.log(date2 + " " + month2);
            $("#dest_time").text(dest_time + " " + date2 + " " + month2);
            //console.log(src_time);
            //console.log(dest_time);
            $("#src_time").text(src_time + " " + date1 + " " + month1);
            var statustrain = val["Status Descrition"];
            //Will do later
            $("#train_dest").html(dest.replace("(", "<h6>(").replace(")", ")</h6>"));
            $("#train_time").text(status);
            $("#train_name").text(train_name);
            $("#train_next").removeAttr("disabled");
            $("#smart_answer").addClass("hide");
        }
        if (window.ctrain === 0) {
            //console.log("0s");
            $("#train_prev").attr("disabled", "disabled");
            $("#train_next").removeAttr("disabled");
        }

    });
$("#smart_answer").addClass("hide");
                                window.trains = window.val;
                                window.val = window.val[0];
                                if (window.trains.length === 1) {
                                    $("#train_next").attr("disabled", "disabled");
                                    $("#train_prev").attr("disabled", "disabled");
                                }
                                var desc = window.val['Description'];
                                var status = window.val['Status'];
                                var status_description = window.val['Status Description'];
                                var train_name = window.val['Train Name'];
                                var source = window.val['Description'].replace("Departed from", "").trim().split("at")[0];
                                var dest = window.val['Description'].split("Destination")[1].split(" at ")[0];
                                //console.log(dest);
                                //console.log(source);
                                //console.log(train_name);
                                var src_time = window.val['Description'].split(' at ')[1].split('on')[0];
                                var dest_time = window.val['Description'].split(' at ')[2].split('on')[0];
                                $("#train_source").html(source.replace("(", "<h6>(").replace(")", ")</h6>"));
                                var date1 = window.val['Description'].split(',')[0].split("on")[1].trim();
                                var month1 = window.val['Description'].split(',')[1];
                                var date2 = window.val['Description'].split(",")[2].split(" at ")[1].split("on")[1].trim();
                                var month2 = window.val['Description'].split(",")[3].trim();
                                //console.log(date2 + " " + month2);
                                $("#dest_time").text(dest_time + " " + date2 + " " + month2);
                                //console.log(src_time);
                                //console.log(dest_time);
                                $("#src_time").text(src_time + " " + date1 + " " + month1);
                                var statustrain = window.val["Status Descrition"];
                                //Will do later
$("#trainimg").attr("src","/ver1/images/train.png");
                                $("#train_dest").html(dest.replace("(", "<h6>(").replace(")", ")</h6>"));
                                $("#train_time").text(status);
                                $("#train_name").text(train_name);
                                $("#train").removeClass("hide");
                                $("#smart_answer").addClass("hide");
$("#smart_col").removeClass("hide");
}
