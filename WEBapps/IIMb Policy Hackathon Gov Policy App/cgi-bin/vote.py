#!/usr/bin/python
import cgi, os,MySQLdb
import cgitb
print "Content-Type: text/html\r\n\r\n"
form = cgi.FieldStorage()
pid=form.getvalue('pid')
idd=""
title=""
desc=""
def fetch(pid):
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","iimb" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		#1 for gov and 0 for suggested
		sql="SELECT pid,ptitle,pdesc,time from main where pid='%s'"%(pid)
		# Execute the SQL command
		cursor.execute(sql)
		results=cursor.fetchall()
		if not results is None:
			for r in results:
				idd=r[0]
				title=r[1]
				desc=r[2]
				break
		db.close()
	except:
		print "Unable to update the database !"
fetch(pid)
print """

<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>TODO supply a title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="/bootstrap/css/bootstrap.css" rel="stylesheet" type="text/css"/>
         <script src="/jQuery/jQuery.js" type="text/javascript"></script>
        <script src="/bootstrap/js/bootstrap.js" type="text/javascript"></script>
        <link href="/bootstrap/css/bootstrap-theme.css" rel="stylesheet" type="text/css"/>
            <link href="/bootstrap/css/index.css" rel="stylesheet" type="text/css"/>
            <script type="text/javascript">
                
             function refreshPolicyGov(){
                 
                     if (window.XMLHttpRequest)
                            {// code for IE7+, Firefox, Chrome, Opera, Safari
                            xmlhttp1=new XMLHttpRequest();
                            
                            }
                        else
                          {// code for IE6, IE5
                          xmlhttp1=new ActiveXObject("Microsoft.XMLHTTP");
                          }
                          
                          xmlhttp1.onreadystatechange=function()
                            {
                            if (xmlhttp1.readyState===4 && xmlhttp1.status===200)
                              {
                              
                            		  var img1=xmlhttp1.responseText.toString().split(";;");
					 var i1=0;
					$("#policy_grp_gov").html("");
					var code1="";
				          while (i1<(img1.length-1)){
						//alert(img);
                                                var details1=img1[i1].toString().split("||");
                                                details1.pop();
				              code1=code1+"<li class=\"list-group-item new\"><b>Policy Code: </b>"+details1[0]+"<blockquote>&nbsp;&nbsp;&nbsp;"+details1[1]+"&nbsp;&nbsp;&nbsp;<label class=\"label label-default\">New</label><button style=\"float:right;\" class=\"btn btn-success\" onclick=\"javascript:window.location='/cgi-bin/vote.py?pid=&percnt;s;'\">Vote</button></blockquote></li>";
				            i1++;  
				          }
					$("#policy_grp_gov").html(code1);
                             
                             
                              }
                             };
                           
                                  
                                 
                                   
                          xmlhttp1.open("GET","/cgi-bin/getGovPolicy.py",true);
                          xmlhttp1.send();
                          
                        
               }
                function refreshPolicyUser(){
                    $("#vote").click(function(){
                        console.log("You clicked me");
                    });
                    /*function displayDetails(){
                                            alert("Hello");
                                        }*/
                     if (window.XMLHttpRequest)
                            {// code for IE7+, Firefox, Chrome, Opera, Safari
                            xmlhttp=new XMLHttpRequest();
                            
                            }
                        else
                          {// code for IE6, IE5
                          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
                          }
                          
                          xmlhttp.onreadystatechange=function()
                            {
                            if (xmlhttp.readyState===4 && xmlhttp.status===200)
                              {
                              
                            		  var img=xmlhttp.responseText.toString().split(";;");
                                          
					 var i=0;
					$("#policy_grp_user").html("");
					var code="";
                                        
				          while (i<(img.length-1)){
                                              
						//alert(img[i]);
                                                var details=img[i].toString().split("||");
                                                details.pop();
                                                //alert(details);

                                                code=code+"<li class=\"list-group-item new\"><b>Policy Code: </b>"+details[0]+"<blockquote>&nbsp;&nbsp;&nbsp;"+details[1]+"&nbsp;&nbsp;&nbsp;<label class=\"label label-default\">New</label><input type=\"button\" style=\"float:right;\" onclick=\"window.location='/cgi-bin/vote.py?pid=&percnt;s;'\" class=\"btn btn-success\"   id=\"vote\" value=\"vote\"></blockquote></li>";
				            i++;  
                                           
				          }
					$("#policy_grp_user").html(code);
                             
                             
                              }
                             };
                           
                                  
                                 
                                   
                          xmlhttp.open("GET","/cgi-bin/getUserPolicy.py",true);
                          xmlhttp.send();
                          
                        
               }
               
                    $(document).ready(function(){
                    
                 var intervalId = setInterval(function(){refreshPolicyGov();}, 1000);
                 var intervalId1 = setInterval(function(){refreshPolicyUser();}, 1000);
              });
              
                </script>
    </head>

    
    <body>
        <div id="top" class="row">
        <nav id="navbar1"  class="navbar navbar-default navbar-inverse navbar-fixed-top  " role="navigation">
             
             <div id="navbar"  class="container-fluid">
                 <div class="input-group" style="width: 40&percnt;;float: left;margin-top: 10px;">
                   
                </div>
                     
                 <div style="float: right;">
                     <a id="help" class="navbar-brand" href="/help.html"><span class=" glyphicon glyphicon-user"></span>&nbsp;Help</a>
                  
                 </div>
                 <div style="float: right;">
                     
                     <a id="help" class="navbar-brand" data-toggle="modal"  data-target=".bs-example-modal-sm"><span class="glyphicon glyphicon-upload "></span>&nbsp;Submit Policy</a>
                   </div>
            
             </div>
                 
                </nav>
        
        
        </div>
        <div class="jumbotron" style=" width: 100&percnt;; height: 45&percnt;;">
           
            <h2 id="pname">%s</h2>
                <h3 id="pcode">%s</h3>
                <p>Vote now!</p>
                <button class="btn btn-success"><span class="glyphicon glyphicon-thumbs-up"></span></button>
                <button class="btn btn-danger"><span class="glyphicon glyphicon-thumbs-down"></span></button>
                <button class="btn btn-primary" data-toggle="modal"  data-target=".comment"><span class="glyphicon glyphicon-comment" ></span></button>
            
                
              
                
       
                <p style="float:right;"><a data-toggle="collapse" data-parent="#accordion" href="#collapseOne" class="btn btn-primary btn-lg"  role="button">Learn more</a></p>
                
       </div>
        
    
        <div id="collapseOne" class="panel-collapse collapse" style="">
                        <div id="pdesc" class="panel-body">
                    %s
                  </div>
        </div>
        <div class="container">
            <div class="row">
                <div class="col col-lg-6">
                    <label class="label label-info" style=" font-size: large;width: 50&percnt;; height: 100&percnt;; ">Goverment Policies</label>
                        <ul class="list-group pre-scrollable" id="policy_grp_gov">
                            <li class="list-group-item new"><b>Policy Code: </b>P785<blockquote>&nbsp;&nbsp;&nbsp;Cras justo odio&nbsp;&nbsp;&nbsp;<label class="label label-default">New</label><button style="float:right;" class="btn btn-success" onclick="javascript:window.location='/vote';">Vote</button></blockquote></li>
                             <li class="list-group-item"><blockquote>&nbsp;&nbsp;&nbsp;Cras justo odio&nbsp;&nbsp;&nbsp;<button style="float:right;" class="btn btn-success" onclick="javascript:window.location='/vote';">Vote</button></blockquote></li>
                             <li class="list-group-item"><blockquote>&nbsp;&nbsp;&nbsp;Cras justo odio&nbsp;&nbsp;&nbsp;<button style="float:right;" class="btn btn-success" onclick="javascript:window.location='/vote';">Vote</button></blockquote></li>

                      </ul>
                </div>
                <div class="col col-lg-6">
                    <label class="label label-info" style="font-size: large;width: 50&percnt;; height: 100&percnt;;">Suggested Policies</label>
                    <ul class="list-group pre-scrollable" id="policy_grp_user">
                            <li class="list-group-item new"><b>Policy Code: </b>P785<blockquote>&nbsp;&nbsp;&nbsp;Cras justo odio&nbsp;&nbsp;&nbsp;<label class="label label-default">New</label><button style="float:right;" class="btn btn-success" onclick="javascript:window.location='/vote';">Vote</button></blockquote></li>
                             <li class="list-group-item"><blockquote>&nbsp;&nbsp;&nbsp;Cras justo odio&nbsp;&nbsp;&nbsp;<button style="float:right;" class="btn btn-success" onclick="javascript:window.location='/vote';">Vote</button></blockquote></li>
                             <li class="list-group-item"><blockquote>&nbsp;&nbsp;&nbsp;Cras justo odio&nbsp;&nbsp;&nbsp;<button style="float:right;" class="btn btn-success" onclick="javascript:window.location='/vote';">Vote</button></blockquote></li>

                      </ul>
                </div>
            </div>
        </div>
       
        <div class="modal fade bs-example-modal-sm" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-sm">
                    <div class="modal-content" style="padding-top: 50px;padding-bottom: 50px;">
                        <label class="center-block" style="text-align:center;">Upload a excel spreadsheet(.xlsx)</label><br/>
                     
                        <div style="margin-left: auto;margin-right: auto;width: 240px;"><input type="file" name="file" form="xl"  /></div><br/>
                        <div  style="margin-left: auto;margin-right: auto;width: 240px;"><form id="xl" enctype="multipart/form-data" action="/cgi-bin/save.py" method="post"><input type="submit" class="btn btn-success" style="width: 100&percnt;;" value="Upload"  /></form></div>
                    </div>
                </div>
</div>
       <div class="modal fade comment" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-sm">
                    <div class="modal-content" style="padding-top: 50px;padding-bottom: 50px;padding-left: 50px;padding-right: 50px;">
                      <label class="center-block" style="text-align:center;">Post a comment</label><br/>
                     
                          <textarea cols="32" rows="5"></textarea><br/>
                          <button class="btn btn-primary center-block" style="text-align: center;" ><span class="glyphicon glyphicon-comment"></span>&nbsp;Comment</button>
                          
                  </div>
                </div>
</div>      
            
            
        
    </body>
</html>


"""%(title,idd,desc)
