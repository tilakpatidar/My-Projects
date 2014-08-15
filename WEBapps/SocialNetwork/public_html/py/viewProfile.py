#!/usr/bin/python -v3
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,hashlib,sha, time, Cookie, os
print "Content-type:text/html\r\n\r\n"
cgitb.enable()

def webPage(username,fname,lname,sex,dob,year,category,vertical,position,work,skill,ach,email,mob,name,profile_pic,regno):
	print """
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
          <script type="text/javascript" src="/js/jQuery.js"></script>
          <script type="text/javascript" src="/js/viewProfile.js"></script>
           
          <link href="/bootstrap-3.1.1-dist/css/bootstrap.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.min.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.min.css" rel="stylesheet" media="screen">
       <link type="text/css" href="/css/viewProfile.css" rel="stylesheet"/>
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
		
                 <input id="search"  type="text" autocomplete="off" name="search" class="autocomplete" placeholder="Search our members">
                    <button type="submit" class="btn btn-success "><span class="glyphicon glyphicon-search"></span></button>
                
                    <a id="help" class="navbar-brand glyphicon glyphicon-user " href="/help.html"> Help</a>
                    <a id="aboutUs" class="navbar-brand glyphicon glyphicon-info-sign" href="/abt_us.html"> AboutUs</a>
                    <a id="signin" class="navbar-brand glyphicon glyphicon-log-in" href="/index.html"> SignIn</a>
                    
             </div>
                 </form>
                </nav>
        
        
        </div>
        <div class="row" id="middle"  >
               <div class="jumbotron" style="padding-bottom: 5px;margin-bottom: 0px;" >
                   <div id="img" class="thumbnail" style="float: right;  background-image: url('/images/%s');background-size:contain,cover;background-repeat: no-repeat;width: 140px;height: 160px;" >
                       <label class="label label-default">%s</label></div>
                   
                   <div class="row" style=""> <h1>%s</h1>
                   </div>
                           
                       
                   
                   
                       
                        
                </div>
            <div class="jumbotron" style="padding-top: 1&percnt;;">
                                    <ul class="nav nav-tabs">
                          <li id="profileItem" class="active"><a href="javascript:profileShow();">Profile Details</a></li>
                          <li id="academicItem" ><a href="javascript:academicShow();">Academic Details</a></li>
                          <li id="contactItem"><a href="javascript:contactShow();">Contact Details</a></li>
                        </ul>
           <br/>
           <br/>
           <div id="profile">
           <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Username</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">First Name</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Last Name</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Sex</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Date of Birth</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
           </div>
             <div id="academic">
           <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Year of Study</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Category</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Vertical</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Current Position</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Current Work</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Skills</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Achievements</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
           </div>
           <div id="contact">
           <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Email Address</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
             <label class=" label label-primary " style="font-size:larger; font-weight:200; margin-right: 15px;">Mobile Number</label>
            <label class="label label-default" style="font-size:90&percnt;;">%s</label><br/><br/>
            
           </div>
       </div>
        </div>
        <div class="row" id="bottom">
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
"""%(profile_pic,regno,name,username,fname,lname,sex,dob,year,category,vertical,position,work,skill,ach,email,mob)
	return



# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = str(form.getvalue('username'))
try:
	# Open database connection
	db = MySQLdb.connect("localhost","root","1","mem_info" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# execute SQL query using execute() method.
	sql="SELECT DISTINCT username,fname,lname,sex,dob,year,category,vertical,position,work,skill,ach,email,mob,profile_pic,regno from info where username='%s'"%(username)

	# Execute the SQL command
	cursor.execute(sql)
	# Fetch all the rows in a list of lists.
	results=cursor.fetchall()
	if not results is None:
		for val in results:
			username=val[0]
			fname=val[1]
			lname=val[2]
			sex=val[3]
			dob=val[4]
			year=val[5]
			category=val[6]
			vertical=val[7]
			position=val[8]
			work=val[9]
			skill=val[10]
			ach=val[11]
			email=val[12]
			mob=val[13]
			name=str(fname)+" "+str(lname)
			profile_pic=val[14]
			regno=val[15]
			break	
		webPage(username,fname,lname,sex,dob,year,category,vertical,position,work,skill,ach,email,mob,name,profile_pic,regno)
	else:
		print "invalid username"

except:
	print "something happened"

