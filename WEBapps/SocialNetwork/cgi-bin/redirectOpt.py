#!/usr/bin/python -v3
# Import modules for CGI handling 
import cgi,cgitb
print "Content-type:text/html\r\n\r\n"
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
key = form.getvalue('opt')
if key is "1":
	#user forgot pswd
	print  "<SCRIPT type='text/javascript'>window.location.href='/frgtPswd.html';</SCRIPT>"
elif key=="2":
	#user forgot user
	print  "<SCRIPT type='text/javascript'>window.location.href='/frgtUser.html';</SCRIPT>"
elif key=="3":
	#technical issue
	print  "<SCRIPT type='text/javascript'>window.location.href='/reportBug.html';</SCRIPT>"
print "<HTML><HEAD><TITLE></TITLE></HEAD><BODY></BODY></HTML>"

