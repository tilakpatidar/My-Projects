#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,faculty,verify,time,error
cgitb.enable()
t=verify.verifySession()
if t[0] and str(t[2])[:1]=='3':
	faculty.getClasses(t[1],t[2])
elif (str(t[2])[:1]=='1' or str(t[2])[:1]=='2'):
	error.errorMessage("Invalid Login Attempt!","You are already logged in as a student.")
else:
	error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
