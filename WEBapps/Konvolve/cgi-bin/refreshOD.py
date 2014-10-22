#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,student,verify,time,error
cgitb.enable()
t=verify.verifySession()
if t[0] and (str(t[2])[:1]=='1' or str(t[2])[:1]=='2'):
	student.refreshOD(t[1],t[2])
elif str(t[2])[:1]=='3':
	error.errorMessage("Invalid Login Attempt!","You are already logged in as a faculty.")
else:
	error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
