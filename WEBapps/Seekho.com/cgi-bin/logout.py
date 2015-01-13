#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb, Cookie, os
cgitb.enable()
def deleteCookie():
	try:
		cookie = Cookie.SimpleCookie()
		cookie['sid'] =0
		cookie['sid']['expires'] =-500
		print cookie	
		print 'Content-Type: text/html\n'
	except:
		return False
	return True
def verifySession(sid):
	try:
		# Open database connection
		db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT username from session where sid='%s'"%(sid)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchone()
		username=results1[0]
		db1.commit()
	except:
		db1.rollback()
		print "Invalid session !"

	db1.close()
	return username

def logOut(username):
	try:
		# Open database connection
		db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="DELETE FROM session where username='%s'"%(username)
		# Execute the SQL command
		cursor1.execute(sql1)
		status=deleteCookie()	
		if status:
			db1.commit()
		else:
			db1.rollback()
		
		db1.close()
		
	except:
		
		db1.rollback()
		db1.close()
		print "Invalid session !"
		
	
	return 

#Loading sid from cookie
cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
cookie.load(string_cookie)
sid = cookie['sid'].value
temp=verifySession(sid)
username=str(temp)

if username !="":
	logOut(username)
	print  "<SCRIPT type='text/javascript'>window.location.href='/cgi-bin/index.py';</SCRIPT>"
else:
	print "Invalid Session"	
