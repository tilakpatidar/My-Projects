if($("#smart_minerals").length===0){
var minerals=$('<div class="col-lg-12 well alpha-blur alpha-shadow" style="margin-top:20px;border:0px;color:white;text-align:center" id="smart_minerals"><div class="col-lg-12" style="text-align:center;"><img src="/ver1/images/minerals.png" width="58px" height="55px"></div><h3 id="commodity">Gold</h3><h4>Live Price : <span id="Live_Price"></span></h4></div>');
$("#smart_col").html("").append(minerals);
$("#smart_answer").addClass("hide");
console.log(window.val);
$("#commodity").setTextValue(window.val["name"].capitalizeMe());
$("#Live_Price").setTextValue(window.val["value"].replace("Rs.","₹ "));
$("#smart_col").removeClass("hide");
}

