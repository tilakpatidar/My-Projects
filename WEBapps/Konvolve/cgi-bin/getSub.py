#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,faculty,verify,time,error
#cgitb.enable()
form = cgi.FieldStorage() 
# Get data from fields
q = form.getvalue('q',"#123None#").strip()
if q !="#123None#":
	t=verify.verifySession()
	if t[0] and str(t[2])[:1]=='3':
		faculty.getSub(t[1],t[2],q)
	elif (str(t[2])[:1]=='1' or str(t[2])[:1]=='2'):
		error.errorMessage("Invalid Login Attempt!","You are already logged in as a student.")
	else:
		error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
