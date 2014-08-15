#!/usr/bin/python -v3
import smtplib,cgi, cgitb,MySQLdb
cgitb.enable()
print "Content-type:text/html\r\n\r\n"
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
email = form.getvalue('email')


try:
	# execute SQL query using execute() method.
	sql="SELECT username from info where email='%s'"%(email)
	# Open database connection
	db = MySQLdb.connect("localhost","root","1","mem_info" )
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	# Execute the SQL command
	cursor.execute(sql)
	# Fetch all the rows in a list of lists.
	results=cursor.fetchone()
	uname=''
	if not results is None:
		uname=results[0]
	else:
		uname='5'
	if not uname is "5":
		sender = 'from@fromdomain.com'
		receivers = ['to@todomain.com']
		message = """From: From Person <from@fromdomain.com>
		To: To Person <%s>
		Subject: Request for username	
		Your username is %s.
		"""%(email,uname)
		smtpObj = smtplib.SMTP('localhost')
	   	smtpObj.sendmail(sender, receivers, message)         
	   	
		db.commit()
		state='success'
		head="All Right !"
		msg="An email has been sent to your email address <STRONG> %s </STRONG>"%(email)
		
	elif uname is '5':
		state='danger'
		head="Oh Snap !"
		msg="No account is associated with this email !"
		
		
	
   	db.commit()
   	
except:
	db.rollback()
        db.close()
        state='danger'
	head="Oh Snap !"
	msg="An error ocurred !"
db.close()
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
      
         <link type="text/css" href="/css/logIn.css" rel="stylesheet"/>
         <script type="text/javascript">
             $(document).ready(function(){
                 
                 $("#warning").hide();
         
                 $("#body").show();
                
             });
             
             
             
              
        
           
           </script>
           
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.min.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.min.css" rel="stylesheet" media="screen">
       
    </head>
    <body  id="body" >
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
        		<nav id="navbar1"  class="navbar navbar-default navbar-inverse navbar-fixed-top " role="navigation">
                <div id="navbar"  class="container-fluid">
                    <a id="home" class="navbar-brand glyphicon glyphicon-home" href="/">Home</a>
                    <a id="help" class="navbar-brand glyphicon glyphicon-user  " href="/help.html"> Help</a>
                    <a id="aboutUs" class="navbar-brand glyphicon glyphicon-info-sign" href="/abt_us.html"> AboutUs</a>
                    <a id="signin" class="navbar-brand glyphicon glyphicon-log-in" href="/index.html"> SignIn</a>
                    
                </div>
                </nav>
        
        
        </div>
        <div style="padding-left:50&percnt;padding-top:10&percnt;;" id="middle">
<center>
       <div class="alert alert-%s" style="width:50&percnt;" id="message"><strong>%s</strong>%s</div>
            </center>
                
            <br/>
            
            
            
                            
            
        
      
        </div>
        <div class="row" id="bottom">
			<nav class="navbar navbar-default navbar-inverse navbar-fixed-bottom  " role="navigation">
                       
                       
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
  
        
 """ %(state,head,msg)
