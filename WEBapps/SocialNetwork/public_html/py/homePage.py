#!/usr/bin/python -v3
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,hashlib,sha, time, Cookie, os
cgitb.enable()
def createSession(username):
	print "Home Page",username
	return
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

print 'Content-Type: text/html\n'
#Loading sid from cookie
cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
cookie.load(string_cookie)
sid = cookie['sid'].value
username=verifySession(sid)


if username !="":
	
	createSession(username)
else:
	print "Invalid Session"	


