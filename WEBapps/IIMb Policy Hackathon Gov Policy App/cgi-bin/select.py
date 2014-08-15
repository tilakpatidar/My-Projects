#!/usr/bin/python
import MySQLdb
import cgi,cgitb
print "Content-type: text/html\r\n\r\n"
db = MySQLdb.connect("127.0.0.1","root","1","analytics")
cursor = db.cursor()
sql = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'analytics';"
tabs = []
cursor.execute(sql)
results = cursor.fetchall()
code=""
for row in results:
	table_name = row[2]
	tabs.append(table_name)
for i in tabs:
	try:
	    	sql = "SELECT DISTINCT `name` FROM `"+i+"`;"
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			code=code+'<li class="list-group-item "><a href="display.py?f='+i+'">'+row[0]+'</a></li>'
	except:
		pass
db.close()
print """

<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>App</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="/bootstrap/css/bootstrap.css" rel="stylesheet" type="text/css"/>
         <script src="/jQuery/jQuery.js" type="text/javascript"></script>
        <script src="/bootstrap/js/bootstrap.js" type="text/javascript"></script>
        <link href="/bootstrap/css/bootstrap-theme.css" rel="stylesheet" type="text/css"/>
           
    </head>

    
    <body>
        <div id="top" class="row">
        <nav id="navbar1"  class="navbar navbar-default navbar-inverse navbar-fixed-top  " role="navigation">
             
             <div id="navbar"  class="container-fluid">
                 <div class="input-group" style="width: 40&percnt;;float: left;">
                   <a class="navbar-brand " style="" href="#">Policy Arch</a>
                </div>
                     
                 <div style="float: right;">
                     <a  class="navbar-brand" href="/help.html"><span class=" glyphicon glyphicon-user"></span>&nbsp;Help</a>
                  
                 </div>
                 <div style="float: right;">
                     <a  class="navbar-brand" data-toggle="modal"  data-target=".bs-example-modal-sm1"><span class="glyphicon glyphicon-upload "></span>&nbsp;Submit Policy</a>
                   </div>
                 <div style="float: right;">
                     <a  class="navbar-brand" href="/cgi-bin/select.py" ><span class="glyphicon glyphicon-stats"></span>&nbsp;Statistics</a>
                   </div>
            
             </div>
                 
                </nav>
        
        
        </div>
	<div style="padding-top:8&percnt;">
			<h2 style='padding-left:20px;'>Statistics Available</h2>
			<ul class="list-group pre-scrollable">%s</ul>
	</div>
           <div class="modal fade bs-example-modal-sm1" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-sm">
                    <div class="modal-content" style="padding-top: 50px;padding-bottom: 50px;">
                        <label class="center-block" style="text-align:center;">Upload a excel spreadsheet(.xlsx)</label><br/>
                     
                        <div style="margin-left: auto;margin-right: auto;width: 240px;"><input type="file" name="file" form="xl"  /></div><br/>
                        <div  style="margin-left: auto;margin-right: auto;width: 240px;"><form id="xl" enctype="multipart/form-data" action="/cgi-bin/save.py" method="post"><input type="submit" class="btn btn-success" style="width: 100&percnt;;" value="Upload"  /></form></div>
                    </div>
                </div>
</div>
        
      
    </body>
</html>


"""%(code)

