#!/usr/bin/python -v3
# Import modules for CGI handling 
print 'Content-Type: text/html\n'
import cgi, cgitb,MySQLdb,hashlib,sha, time, Cookie, os

cgitb.enable()
#Loading sid from cookie
cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')

if string_cookie is None:
	print  "<SCRIPT type='text/javascript'>window.location.href='/logIn.html';</SCRIPT>"
else:
	print  "<SCRIPT type='text/javascript'>window.location.href='UserProfile.py';</SCRIPT>"


