$("#smart_answer").addClass("hide");
$("#smart_col").addClass("hide");

                                var prnt = $();
                                $.each(window.val, function(k, v) {
                                    var t = $("<span class=\"h5\"></span>");
                                    var d = $("<span class=\"h5\"></span>");
                                    var m = $("<p></p>");

                                    t.html("<b>" + (k.replace("_", " ") + " : ").capitalizeMe() + "</b>");
                                    d.text((v.replace("_", " ")).capitalizeMe());
                                    m.append(t);
                                    m.append(d);
                                    prnt = prnt.add(m);
                                    $("#smart_answer").append(prnt);
                                    $("#smart_answer").removeClass("hide");


                                });

