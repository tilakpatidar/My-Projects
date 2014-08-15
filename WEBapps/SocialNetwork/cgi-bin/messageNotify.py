#!/usr/bin/python -v3
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,hashlib,sha, time, Cookie, os
print 'Content-Type: text/html\n'

name=""
profile_pic=""
regno=""
notify=""
def verifySession(sid):
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","mem_info" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT username from session where sid='%s'"%(sid)
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchone()
		if not results1 is None:
			for val in results1:
				username=val
				break
		else:
			print "Invalid session !"
		
		db1.commit()
		db1.close()
		return username
	except:
		db1.rollback()
		print "Invalid session !"

	db1.close()
	return ""

def messageNotify(username):
	
	
def fetchUserDetails(username):
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","mem_info" )

		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		# execute SQL query using execute() method.
		sql="SELECT DISTINCT username,fname,lname,profile_pic,regno from info where username='%s'"%(username)

		# Execute the SQL command
		cursor.execute(sql)
		# Fetch all the rows in a list of lists.
		results=cursor.fetchall()
		if not results is None:
			for val in results:
				username=val[0]
				fname=val[1]
				lname=val[2]
				global name
				global profile_pic
				global regno
				name=str(fname)+" "+str(lname)
				profile_pic=val[3]
				regno=val[4]
				break	
			
		else:
			print "invalid username"

	except:
		print "something happened"


	
	return



def showNotification(username):
	try:
		#print username
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","mem_info" )

		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()

		# execute SQL query using execute() method.
		sql1="SELECT COUNT(*) from messages where msg_to='%s' AND seen='0'"%(username)

		# Execute the SQL command
		cursor1.execute(sql1)
		# Fetch all the rows in a list of lists.
		results1=cursor1.fetchall()
		if not results1 is None:
			for val in results1:
				count=val[0]
				global notify
				notify=count
				#print notify
				break	
			
		else:
			print "invalid username"
		db1.commit()
	except:
		db1.rollback()
		print "something happenedd"
	db1.close()

def webPage():
	global profile_pic
	global name
	global regno
	global notify
	
	print"""
<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>www.blah.com</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width">
          <script type="text/javascript" src="js/jQuery.js"></script>
          <script type="text/javascript" src="js/messageNotify.js"></script>
           <script type="text/javascript" src="bootstrap-3.1.1-dist/js/bootstrap.js"></script> 
          <link href="bootstrap-3.1.1-dist/css/bootstrap.css" rel="stylesheet" media="screen">
       <link href="bootstrap-3.1.1-dist/css/bootstrap.css.map" rel="stylesheet" media="screen">
       <link href="bootstrap-3.1.1-dist/css/bootstrap.min.css" rel="stylesheet" media="screen">
       <link href="bootstrap-3.1.1-dist/css/bootstrap-theme.css" rel="stylesheet" media="screen">
       <link href="bootstrap-3.1.1-dist/css/bootstrap-theme.css.map" rel="stylesheet" media="screen">
       <link href="bootstrap-3.1.1-dist/css/bootstrap-theme.min.css" rel="stylesheet" media="screen">
       <link type="text/css" href="css/messageNotify.css" rel="stylesheet"/>
       <script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>
       
<script type="text/javascript" src="js/jquery-ui.min.js"></script>
  <link rel="stylesheet" href="css/jquery-ui.min.css" type="text/css" /> 
  <link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.4/themes/base/jquery-ui.css">


  <script type="text/javascript" src="js/jquery.ui.autocomplete.html.js"></script>
    </head>
    <body>
        <div id="fb-root"></div>
            <script>(function(d, s, id) {
              var js, fjs = d.getElementsByTagName(s)[0];
              if (d.getElementById(id)) return;
              js = d.createElement(s); js.id = id;
              js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.0";
              fjs.parentNode.insertBefore(js, fjs);
            }(document, 'script', 'facebook-jssdk'));</script>
        
        <div class="alert alert-danger" id="warning"><strong>Oh Snap !</strong> This website works on JavaScript ! Please enable it !</div> 
        <div id="top" class="row">
        <nav id="navbar1"  class="navbar navbar-default navbar-inverse navbar-fixed-top  " role="navigation">
             <form method="POST" action="cgi-bin/search.py">
             <div id="navbar"  class="container-fluid">
                 <div class="row" style="margin-left: 10px;float: left;width: 30%;">
		<ul class=" nav nav-pills  ">
                                    <li class="active">
                                      <a href="homePage.py">
                                        <span class="glyphicon glyphicon-home"></span>
                                        Home
                                      </a>
                                    </li>
                                    
                                    
                                    <li class="active">
                                      <a href="UserProfile.py">
                                        <span class="glyphicon glyphicon-user"></span>
                                        Profile
                                      </a>
                                    </li>

                                    
                                 
                                    <li class="active">
                                      
                             
                                        <a href="messageNotify.py">  
                                       
                                        Messages<span class="badge pull-right ">42</span></a>
                                                          
                                    
                                        
                                        
                                        
                                    </li>
                                    
                                    
                                    
                                  </ul>
                                
                 </div>
                
                
                 
                 
               
                            <div class="btn-group nav nav-pills" style="width:250px;float: right; ">
                                
                                <button type="button" style=""  class="btn btn-primary dropdown-toggle"  data-toggle="dropdown">
                                Account <span class="caret"></span>
                              </button>
                              <ul class="dropdown-menu" role="menu">
                                  <li><div style="width: 250px;height: 120px;"><div style="float: left;"><img style="margin-left: 2px;" class="img-thumbnail" src="/images/%s" width="110" height="110" alt=""></div><div style="float: right;height: 110px;"><label class="label label-primary " style="font-size: medium; margin-right: 7px; " >%s</label><br/><label class="label label-default" style="font-size:xx-small;">%s</label></div></div></li>
                                <li><a href="#"><span class="glyphicon glyphicon-lock"></span> Account Settings</a></li>
                                
                                <li class="divider"></li>
                                <li><a href="#"><span class="glyphicon glyphicon-log-out"></span> Sign Out</a></li>
                              </ul>
                                
                            </div>
                            
                 <div style="margin-top:5px;margin-left: 10px;margin-right: 10px;width: 35%;"  class="input-group ">
                                            <input type="text" class="form-control autocompleteform-control" autocomplete="off" name="search" id="search" placeholder="Search our members">
                                            <span class="input-group-addon glyphicon glyphicon-search"></span>
                                          </div>
                              
                    
                 
                 
             </div>
                   
                    
                    
                 </form>
                </nav>
        
        
        </div>
        <div class="row" id="middle"  >
                        <div class="jumbotron" style="height: 230px;float: top;border-bottom:cornflowerblue;border-bottom-width: thick;border-bottom-style:solid;" >
                               <div id="img" class="thumbnail" style="float: right;  background-image: url('/images/%s');background-size:contain,cover;background-repeat: no-repeat;width: 140px;height: 160px;" >
                                   <label class="label label-default">%s</label></div>

                               <div class="row" style="float: left;"> <h1>%s</h1>
                               </div>
                        </div>

                        <div id="middle_btm" style="height: 970px;float: bottom;">
                            <div class="jumbotron" style="height:200px;float: bottom;">
                                <ul style="height: 800px; width: 50%;" class="list-group pre-scrollable center-block">
                                   
                                    <li class="list-group-item  " >
                                             <a href="#">
                                                 <blockquote>
                                             
                                              <img style="margin-left: 2px;" class="img-thumbnail" src="images/user.png" width="50" height="50" alt=""/>
                                              
                                             
                                              <label class="label label-primary" style="font-size: small;">Tilak Patidar</label>
                                              <span class="badge" style="font-size:medium;">42</span>
                                             
                                                 </blockquote>
                                                 </a>
                                        
                                    </li>
                                          <li></li>
                                </ul>   
                               
                            </div>
                        </div>
          
        </div>
        <div class="row" id="bottom" style="margin-top: 20px;">
                    <nav id="nav_btm" class="navbar navbar-default navbar-inverse navbar-fixed-bottom   " role="navigation">
                       
                       
                        <div class="fb-like" style="float: left; margin-top: 10px;margin-left: 5px;" data-href="https://www.facebook.com/srmse" data-layout="standard" data-action="like" data-show-faces="false" data-colorscheme="dark" data-share="true"></div>
                     
                      <div style="float: right;margin-top: 10px;">
                                    <div class="g-plusone" align="right" data-annotation="inline" data-width="300"></div>

                                    <script type="text/javascript">
                                      (function() {
                                        var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
                                        po.src = 'https://apis.google.com/js/platform.js';
                                        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
                                      })();
                                    </script>
                      </div>
                    </nav>
        </div>
    </body>
</html>

"""%(profile_pic,name,regno,profile_pic,regno,name)
#Loading sid from cookie
cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
if string_cookie is None:
	print  "<SCRIPT type='text/javascript'>window.location.href='/';</SCRIPT>"
else:
	cookie.load(string_cookie)
	sid = cookie['sid'].value
	username=verifySession(sid)


	if username !="":
		showNotification(username)
		fetchUserDetails(username)
		messageNotify(username)
		
		
	else:
		print "Invalid Session"	

