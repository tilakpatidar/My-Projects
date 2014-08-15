#!/usr/bin/python -v3
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,hashlib,os
cgitb.enable()
# Create instance of FieldStorage 
form = cgi.FieldStorage()

#get data from html form
fileitem=form['file']
fname=str(form.getvalue('fname'))
lname=str(form.getvalue('lname'))
sex=str(form.getvalue('sex'))
dob=str(form.getvalue('dob'))
year=str(form.getvalue('year'))
category=str(form.getvalue('category'))
vertical=str(form.getvalue('vertical'))
position=str(form.getvalue('position'))
work=str(form.getvalue('work'))
email=str(form.getvalue('email'))
mob=str(form.getvalue('mob'))
username=str(form.getvalue('username'))
pswd=str(form.getvalue('pswd1'))
skill=str(form.getvalue('skill'))
ach=str(form.getvalue('ach'))
file_choosen=str(form.getvalue("file_choosen"))
sec_q1=str(form.getvalue('sec_q'))
sec_q2=str(form.getvalue('sec_q2'))
sec_q=""
regno=str(form.getvalue('regno'))

#Check if user selected an image

file_empty=0#flag for empty profile pic 0 means file is choosen
if file_choosen is "0":
	fileitem=open("user.png")
	file_empty=1

#Check if user used created ques or created a new ques
if sec_q1=="None":
	sec_q=sec_q2
elif sec_q2=="None":
	sec_q=sec_q1


#Hashing of entered pswd started

key=str(pswd)

#Step 1 conversion of input to md5

m = hashlib.md5()
m.update(key)
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
pswd=temp#This is hashed pswd

# Open database connection
db = MySQLdb.connect("localhost","root","1","mem_info" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.


sql1="INSERT INTO admin (username,password) VALUES('%s','%s')"%(username,pswd)



try: # Windows needs stdio set for binary mode for uploading file.
    	import msvcrt
    	msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    	msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    	pass

# strip leading path from file name to avoid directory traversal attacks
#add extension to file name
fn=''
old_file=''#old file name viz displayed to user

if file_empty==1:
	l=len(fileitem.name)
	ext=fileitem.name[-4:l+1]
	fn=str(username)+''+str(ext)#global var carries file name from orignal file path
elif file_empty==0:
	filee=os.path.basename(fileitem.filename)
	old_file=filee
	l=len(filee)
	ext=filee[-4:l+1]
	fn=str(username)+''+str(ext)#global var carries file name from orignal file path

sql = "INSERT INTO info (fname, lname, email,dob,mob, sex,vertical,position,work,year,category,security_q,username,ach,skill,profile_pic,regno) VALUES ('%s', '%s','%s', '%s','%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(fname,lname,email,dob,mob,sex,vertical,position,work,year,category,sec_q,username,ach,skill,fn,regno)


state=''
head=''
message='' 
try:
   # Execute the SQL command
   cursor.execute(sql)
   cursor.execute(sql1)
   
   if file_empty==0:
	#means user selected a file
	
	
	open('/var/www/AmigosNet/public_html/images/' + fn, 'wb').write(fileitem.file.read())
	message = 'Profile created and the file <strong>"' + old_file + '"</strong> was uploaded successfully'
	state='success'
	head="Thank You !"
   elif file_empty==1:
	#means upload default pic
	
        
	open('/var/www/AmigosNet/public_html/images/' + fn, 'wb').write(fileitem.read())
	message = 'Profile created and <strong>"' + 'Default' + '"</strong> profile picture is choosen successfully'
	state='success'
	head="Thank You !"
   	
   else:
	#if error while copying
	db.rollback()
	state='danger'
	head="Oh Snap !"
   	message = 'Unable to create profile'


   #undo everything if uploaded pic is not found
   
   if not os.path.isfile('/var/www/AmigosNet/public_html/images/' + fn):
	db.rollback()
   	os.remove('/var/www/AmigosNet/public_html/images/' + fn)
	state='danger'
	head="Oh Snap !"
   	message = 'Unable to create profile'

   
   
except:
   # Rollback in case there is any error
   db.rollback()
   
   if os.path.isfile('/var/www/AmigosNet/public_html/images/' + fn):
   	os.remove('/var/www/AmigosNet/public_html/images/' + fn)
   state='danger'
   head="Oh Snap !"
   message = 'Unable to create profile'
   
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
        <div style="padding-left:60px;padding-top:10&percnt;;" id="middle">
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
  
        
 """ %(state,head,message)
# Commit your changes in the database
db.commit()
# disconnect from server
db.close()
