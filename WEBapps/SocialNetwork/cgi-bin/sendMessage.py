#!/usr/bin/python -v3
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,hashlib,sha, time, Cookie, os
from datetime import datetime
print 'Content-Type: text/html\n'
cgitb.enable()
name=""
profile_pic=""
regno=""
notify=""
senders_html=""
added_contact=""
def contactSelected():
	try:
		#print username
		# Open database connection
		db4 = MySQLdb.connect("localhost","root","1","mem_info" )

		# prepare a cursor object using cursor() method
		cursor4 = db4.cursor()

		# execute SQL query using execute() method.
		sql4="SELECT profile_pic,CONCAT(CONCAT(fname,' '),lname) from info where username='%s'"%(msg_from)

		# Execute the SQL command
		cursor4.execute(sql4)
		# Fetch all the rows in a list of lists.
		results4=cursor4.fetchall()
		
		if not results4 is None:
			for val in results4:
				pic=val[0]
				name=val[1]
				break	
			
		else:
			pic=""
			name=""
		
		
		global added_contact
		
		if str(pic)=="" or str(name)=="":
			
			
			added_contact=""
		else:
			
			added_contact="""<img style='' class='img-thumbnail' src='/images/%s' width='80' height='90' alt=''/><label class='label label-primary' style='font-size: small;'>%s</label>"""%(pic,name)
		
		db4.commit()
	except:
		db4.rollback()
		#print "something happened"
	db4.close()
			


def showSenders(username):
	try:
		#print username
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","mem_info" )

		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()

		# execute SQL query using execute() method.
		sql1="SELECT M.msg_from,COUNT(*),I.fname,I.lname,I.profile_pic,I.username from messages M,info I where M.msg_to='%s' AND M.seen='0' AND I.username = M.msg_from GROUP BY M.msg_from"%(username)
		
		# Execute the SQL command
		cursor1.execute(sql1)
		# Fetch all the rows in a list of lists.
		results1=cursor1.fetchall()
		if not results1 is None:
			for val in results1:
				msg_from=val[0]
				count=val[1]
				fname=val[2]
				lname=val[3]
				profile_pic=val[4]
				username=val[5]
				global senders_html
				senders_html=senders_html+"""
 <li class="list-group-item  " >
                                             <a href="sendMessage.py?from=%s">
                                                 <blockquote>
                                             
                                              <img style="margin-left: 2px;" class="img-thumbnail" src="/images/%s" width="50" height="50" alt=""/>
                                              
                                             
                                              <label class="label label-primary" style="font-size: small;">%s</label>
                                              <span class="badge" style="font-size:medium;">%s</span>
                                             
                                                 </blockquote>
                                                 </a>
                                        
                                    </li>
"""%(username,profile_pic,fname+" "+lname,count)
				#print notify
				
			
		else:
			print "invalid username"
		db1.commit()
	except:
		db1.rollback()
		print "something happenedd"
	db1.close()


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



def messageSeen(u,f):
	try:
		# Open database connection
		db3 = MySQLdb.connect("localhost","root","1","mem_info" )
		# prepare a cursor object using cursor() method
		cursor3 = db3.cursor()
		# execute SQL query using execute() method.
		sql3="UPDATE messages SET seen=1 WHERE msg_to='%s' AND msg_from='%s'"%(u,f)
		# Execute the SQL command
		cursor3.execute(sql3)
		
		db3.commit()
		db3.close()
	except:
		db3.rollback()
		
def webPage(notify,strr):
	contactSelected()
	global profile_pic
	global name
	global regno
	global senders_html
	global added_contact
	print """<!DOCTYPE html>
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
          <script type="text/javascript" src="/js/jQuery.js"></script>
		 
          <script type="text/javascript" src="/js/sendMessage.js"></script>
		  
           <script type="text/javascript" src="/bootstrap-3.1.1-dist/js/bootstrap.js"></script> 
          <link href="/bootstrap-3.1.1-dist/css/bootstrap.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.min.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.min.css" rel="stylesheet" media="screen">
       <link type="text/css" href="/css/sendMessage.css" rel="stylesheet"/>
       <script type="text/javascript" src="/js/jquery-1.9.1.min.js"></script>
       
<script type="text/javascript" src="/js/jquery-ui.min.js"></script>
  <link rel="stylesheet" href="/css/jquery-ui.min.css" type="text/css" /> 
  <link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.4/themes/base/jquery-ui.css">


  <script type="text/javascript" src="/js/jquery.ui.autocomplete.html.js"></script>
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
                 <div class="row" style="margin-left: 10px;float: left;width: 30&percnt;;">
		<ul class=" nav nav-pills  ">
                                   
                                    
                                    
                                    <li class="active">
                                      <a href="UserProfile.py">
                                        <span class="glyphicon glyphicon-user"></span>
                                        Profile
                                      </a>
                                    </li>

                                    
                                 
                                    <li class="active ">
                                      
                                        <a href="sendMessage.py" >
                                        Messages <span class="badge">%s</span>
                                        </a> 
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
                                <li><a href="logOut.py"><span class="glyphicon glyphicon-log-out"></span> Sign Out</a></li>
                              </ul>
                                
                            </div>
                            
                 <div style="margin-top:5px;margin-left: 10px;margin-right: 10px;width: 35&percnt;;"  class="input-group ">
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
                                    <div class="" style="width: 30&percnt;;height:600px; float: left;">

<label class="label label-primary center-block" style="font-size: small;">People who messaged you !</label>
                                                 <ul style="height: 600px; width: 100&percnt;;" class="list-group pre-scrollable">
                                   %s
                                   
                                          
                                </ul>   
                                </div>   
                                <div class="" style=" width: 55&percnt;;height: 600px;float: right;">
                                        <label class="label label-primary center-block" style="font-size: small;text-align:left;"><strong>To:</strong></label>
                                        <br/>
					 <div style="margin-right: 10px;"  class=" ">
                                               <blockquote id="contact_selected" >%s</blockquote>
                                        </div>
                                        <div style="margin-left: 10px;margin-right: 10px;"  class="input-group ">
                                            <input type="text" class="form-control autocompleteform-control" autocomplete="off" name="add" id="add" placeholder="Add Contacts">
                                            <span class="input-group-addon glyphicon glyphicon-search"></span>
                                          </div>
                                                    
                                        <div style="margin-top: 40px;margin-left: 10px;margin-right: 10px;"  >
                                            <ul id="msgs" style="height: 200px;" class="list-group pre-scrollable">

                                               %s
                                    </ul>
                                            <br/>
                                            <label style="text-align:left;font-size: larger;" class="label label-success center-block">Reply</label>
                                            <br/>
                                            
                                           
                                            <textarea id="msg" class="form-control" rows="3" placeholder="Reply . . ."></textarea>
                                            <br/>
                                             <button class="btn btn-danger" style="float: right;width:150px;margin-left: 20px;"><span class="glyphicon glyphicon-remove"></span> Clear</button>
                                              
                                             <button id="send"  class="btn btn-primary" style=" float: right;width:150px;"><span class="glyphicon glyphicon-send"></span> Reply</button>
                                           
                                        </div>
                                </div>
                               
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

"""%(notify,profile_pic,name,regno,profile_pic,regno,name,senders_html,added_contact,strr)

def createRHS(m,t,s):
	
	if s=="0":
		s=""
	elif s=="1":
		
		s="""<span class="glyphicon glyphicon-flag"></span>"""
	
	msg_list="""<li class="alert alert-warning" ><blockquote class="blockquote-reverse" >
                                            <p style="font-size:small;">%s</p>
                                            <div style="float:left;">%s</div><div style="float: right;"><footer>You<br/><p style="font-size: smaller;">%s</p></footer>
                                            </div> </blockquote></li>
					"""%(m,s,t)
	return msg_list



def createLHS(m,f,t,s):
	
	s=""
	
	
	temp="""  <li class="alert alert-success" style="background-color:#ffff99;"><blockquote > <p style="font-size: small;">%s</p><div style="float:right;">%s</div><div style="float: left;"><footer>%s<br/><p style="font-size: smaller;">%s</p></footer>
                                            </div>
                                          </blockquote></li>"""%(m,s,f,t)
	
	return temp


def convertTimeFormat(t):
	d = datetime.strptime(str(t), "%H:%M")
	return d.strftime("%I:%M %p")	
def showMessages(username,msg_from):
	try:
		
		# Open database connection
		db2 = MySQLdb.connect("localhost","root","1","mem_info" )
		# prepare a cursor object using cursor() method
		cursor2 = db2.cursor()
		# execute SQL query using execute() method.
		sql2="SELECT msg_from,message,time,seen from messages where (msg_to='%s' AND msg_from='%s') OR (msg_to='%s' AND msg_from='%s') ORDER BY time ASC"%(username,msg_from,msg_from,username)
		
		# Execute the SQL command
		cursor2.execute(sql2)
		
		results2=cursor2.fetchall()
		big_str=""
		if not results2 is None:
			
			for val in results2:
				frm=str(val[0])
				msg=str(val[1])
				time=str(val[2])
				seen=str(val[3])
				temp=time[10:len(time)-3].strip()
				
				time=convertTimeFormat(temp)
				username=str(username)
				
				if frm == username:
					big_str=big_str+createRHS(msg,time,seen)
				else:
					big_str=big_str+createLHS(msg,frm,time,seen)
					
				
		else:
			results2=""
		
		global notify
		
		db2.commit()
		
		webPage(notify,big_str)
	except:
		db2.rollback()
	db2.close()

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


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

msg_from  =form.getvalue('from')

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
		showSenders(username)
		fetchUserDetails(username)
		showMessages(username,msg_from)
		messageSeen(username,msg_from)
		
	else:
		print "Invalid Session"	


