#!/usr/bin/python -v3
import smtplib,cgi, cgitb,MySQLdb,string,random,hashlib
cgitb.enable()
print "Content-type:text/html\r\n\r\n"


def pswd_generator(size=12, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
def enc_pswd(pswd):
	#Step 1 conversion of input to md5
	
	m = hashlib.md5()
	m.update(pswd)
	s1=m.hexdigest()
	#print 'Step 1 md5 ',s1

	#Step 2 Conversion of s1 to salt
	#By adding salt from 2 places from right as well left

	salt=r'tilak@Google05-05-1995#IndiaSal$100000$'
	l=len(s1)
	mid=s1[2:-2]

	s2=str(s1[0]+s1[1]+salt+mid+salt+s1[-2]+s1[-1])
	#print 's2  ',s2
	#Step 3
	#Converting salt version to md5 again

	m=hashlib.md5()
	m.update(s2)
	s3=m.hexdigest()


	#print 's3  ',s3


	#Step 4 
	#Replacement algorithm
	#replacing 9 by 1
	temp=s3.replace('9','1')
	#replacing 0 by 5
	temp=temp.replace('0','5')
	#replacing a by t
	temp=temp.replace('a','t')
	return temp


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
email = form.getvalue('email')
uname=''
pswd=''
epswd=''


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
db.close()

if not results is None:
	uname=results[0]		
else:
	uname='5'#means do not fetch pswd from admin



if not uname is "5":#update new genrated pswd
	pswd=pswd_generator()
	epswd=enc_pswd(pswd)
	# execute SQL query using execute() method.
	sql1="UPDATE admin SET password='%s' where username='%s'"%(epswd,uname)
	# Open database connection
	db1 = MySQLdb.connect("localhost","root","1","mem_info" )
	# prepare a cursor object using cursor() method
	cursor1 = db1.cursor()
	# Execute the SQL command
	cursor1.execute(sql1)
	db1.commit()
	db1.close()
if uname is '5':
	state='danger'
	head="Oh Snap !"
	msg="No account is associated with this email !"
else:
	sender = 'from@fromdomain.com'
	receivers = ['to@todomain.com']
	message = """From: From Person <from@fromdomain.com>
	To: To Person <%s>
	Subject: Request for username	
	Your password is %s.
	"""%(email,pswd)
	smtpObj = smtplib.SMTP('localhost')
   	smtpObj.sendmail(sender, receivers, message)         	
	state='success'
	head="All Right !"
	msg="An email has been sent to your email address <STRONG> %s </STRONG>"%(email)
		

		
		
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
      
         <link type="text/css" href="/css/index.css" rel="stylesheet"/>
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
      %s
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
  
        
 """ %(pswd,state,head,msg)
   
