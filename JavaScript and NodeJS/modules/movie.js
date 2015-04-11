if($("#smart_movie").length===0){
var movie=$(" <div class=\"well alpha-blur row hide\" id=\"smart_movie\">                     <div class=\"row\">                        <div class=\"col-lg-5 col-md-5 col-sm-5\" ><img id=\"poster\" src=\"\" class=\"full-height full-width\">                        </div>                         <div class=\"col-lg-7 col-md-7 col-sm-7\">                           <div class=\"well no-back\" id=\"name\">                              <h3><b></b></h3>                           </div>                           <ul class=\"list-group \" style=\"border:0px;text-align:left;\"> <li class=\"list-group-item no-back\" id=\"rating\"></li>                              <li class=\"list-group-item no-back\" id=\"director\"></li>                              <li class=\"list-group-item no-back\" id=\"producer\"></li>                              <li class=\"list-group-item no-back\" id=\"writer\"></li>                              <li class=\"list-group-item no-back\" id=\"editor\"></li>                              <li class=\"list-group-item no-back\" id=\"cinematography\"></li>                              <li class=\"list-group-item no-back\" id=\"music\"></li>                           </ul>                           <ul class=\"list-group \" style=\"border:0px;text-align:left;\">                              <li class=\"list-group-item no-back\" id=\"country\"></li>                              <li class=\"list-group-item no-back\" id=\"runtime\"></li>                              <li class=\"list-group-item no-back\" id=\"lang\"></li><li class=\"list-group-item no-back\" id=\"distributor\"></li>                              <li class=\"list-group-item no-back\">                                 <button type=\"button\" class=\"btn btn-primary\" style=\"border:0px;\" id=\"movie_button\">More</button>                              </li>                           </ul>                        </div>                     </div>                     <div class=\"row alpha-blur well\" id=\"movie_extra\">                        <p id=\"plot\"></p>                        <div class=\"table-responsive\" id=\"smart_cast\">                           <table class=\"table well alpha-blur\" style=\"color:white;text-align:center;border:0px;\">                              <thead>                                 <tr>                                    <th style=\"text-align:center\" colspan=\"4\">                                       <h4>Cast</h4>                                    </th>                                 </tr>                              </thead>                              <tbody id=\"cast\">                              </tbody>                           </table>                        </div>                        <div class=\"col-lg-12 col-md-12 col-sm-12\" style=\"text-align:center;\">                           <div class=\"btn-group\" role=\"group\" aria-label=\"...\">                              <button type=\"button\" class=\"btn btn-primary\" style=\"border:0px;\" id=\"plot_button\">Plot</button>                              <button type=\"button\" class=\"btn btn-primary\" style=\"border:0px;\" id=\"cast_button\">Cast</button>                           </div>                        </div>                     </div></div>");
$("#centre_parent").prepend(movie);
$("#smart_answer").addClass("hide");
                                $("#smart_movie").removeClass("hide");
                                $("#name").setHtmlValue("<h2>" + window.val["name"] + "</h2>",window.val["name"]);
                                $("#director").setHtmlValue("<b>Director : </b> <span>"+window.val["director"]+"</span>",window.val["director"]);
                                $("#producer").setHtmlValue("<b>Producer : </b> <span>"+window.val["producer"]+"</span>",window.val["producer"]);
$("#runtime").setHtmlValue("<b>Runtime : </b> <span>"+window.val["runtime"]+"</span>",window.val["runtime"]);

$("#writer").setHtmlValue("<b>Writer : </b> <span>"+window.val["writer"]+"</span>",window.val["writer"]);
                                $("#music").setHtmlValue("<b>Music : </b> <span>"+window.val["music"]+"</span>",window.val["music"]);
                                $("#editor").setHtmlValue("<b>Editor : </b> <span>"+window.val["editor"]+"</span>",window.val["editor"]);
                                $("#cinematography").setHtmlValue("<b>Cinematography : </b> <span>"+window.val["cinematography"]+"</span>",window.val["cinematography"]);
                                $("#country").setHtmlValue("<b>Country : </b> <span>"+window.val["country"]+"</span>",window.val["country"]);

                                $("#lang").setHtmlValue("<b>Language : </b> <span>"+window.val["language"]+"</span>",window.val["language"]);
$("#distributor").setHtmlValue("<b>Distributor : </b> <span>"+window.val["distributor"]+"</span>",window.val["distributor"]);
$("#rating").setHtmlValue("<b>Rating : </b> <span>"+window.val["rating"]+"</span>",window.val["rating"]);
                                $("#plot").setTextValue(window.val["plot"]);
$("#poster").attr("src",window.val["image"]);

                                var cast = window.val["cast"].split("\t");
                                var prnt = $();
                                var tr = $("<tr></tr>");
                                var tdd = [];
                                var count = 1;
                                $.each(cast, function(index, element) {
                                    //console.log(index);
                                    if (count % 4 === 0) {
                                        var t = $("<td></td>");
                                        t.html("<a class=\"cast_link\" target=\"_blank\" href=\"http://en.wikipedia.org/wiki/" + element + "\">" +element + "</a>");
                                        tdd.push(t);

                                        $.each(tdd, function(i, e) {
                                            tr.append(e);

                                        });
                                        tdd = [];
                                        prnt = prnt.add(tr);
                                        tr = $("<tr></tr>");

                                    } else {
                                        //console.log("else");
                                        var t = $("<td></td>");
                                        t.html("<a class=\"cast_link\" target=\"_blank\" href=\"http://en.wikipedia.org/wiki/" + element + "\">" + element + "</a>");
                                        tdd.push(t);
                                        //console.log(tdd);



                                    }
                                    count++;

                                });
                                $("#cast").append(prnt);
$("#smart_col").removeClass("hide");
cycle3=0;
$("#smart_cast").hide();

    $("#movie_extra").hide();
$("#colleges").hide();
    $("#cast_button").click(
        function() {
            $('#plot').slideToggle();
            $('#smart_cast').slideToggle();
        }
    );
    $("#plot_button").click(
        function() {
            $('#plot').slideToggle();
            $('#smart_cast').slideToggle();
        }
    );
    $("#movie_button").click(
        function() {

if(cycle3===0){
	    		$('#movie_extra').slideToggle();
                        $(this).text("Less");
			++cycle3;
			}
		else{
			$('#movie_extra').slideToggle();
$(this).text("More");
			cycle3=0;
		}


        }
    );
}
