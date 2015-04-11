if($('#help_box').length===0){
console.log('here');
$(".helpb").remove();

var help = $('<div name="alertname" style="opacity:0;" class="scheme helpb" role="alert" id="help_box"><span id="help_close" style="position:absolute;right:5px;top:5px;cursor:pointer;" class="glyphicon glyphicon-remove"></span></div>');
$('body').append(help); 
$('#help_close').on("click",function(){
$("#help_box").animate({opacity:'0'},500,function(){
$("#help_box").remove();
});
});
$("#help_box").animate({opacity:'1'},500,function(){

});
//$('#help_box').fadeIn("slow",function(){});
 var tip=new Array();

  tip[0]="If you want to Check current weather,try \"Weather New York\"";
  tip[1]="Check current Movies running near your Local Area,try \"Watch Movies\"";
  tip[2]="Get the local News of your nearby area, try \" News Nearby\"";
  tip[3]="Use the SRMSE as a Calculator, Just Write the expression as\"2*25+3-1\"";
  tip[4]="SRMSE can also be used as Currency Converter, try \"100 INR to USD \"";
  tip[5]="Don't focus much on Grammar, focus on Keywords";
  tip[6]="Check Local Hotels nearby by entering \"Hotels Nearby\"";
  tip[7]="Check highly rated nearby Food joints by entering\"Food joints Nearby\"";
  tip[8]="Find meanings of different words,just Enter \"ostentatious meaning\"";
  tip[9]="Get information about Flights and Railways in your City, Enter \"Flights today or Train tomorrow\"";
  tip[10]="Get the Chords for your favourite Songs,Enter\"Imagine Dragons impossible chords\"";
  

setInterval(function() { 
  var Q = tip.length;
var whichtip=Math.round(Math.random()*(Q-1));
$(".help-info").remove();
$('#help_box').append("<div class=\"help-info center-block\">"+tip[whichtip]+"</div>");
},5000);
  var Q = tip.length;
var whichtip=Math.round(Math.random()*(Q-1));
function showtip(){$(".help-info").remove();$("#help_box").append("<div class=\"help-info center-block\">"+tip[whichtip]+"</div>");}
showtip();

}

