#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb, time, Cookie, os,math,error
#cgitb.enable()
def verifySession():
	# Create instance of FieldStorage 
	cookie = Cookie.SimpleCookie()
	string_cookie = os.environ.get('HTTP_COOKIE')
	if string_cookie is None:
		return False,""
		error.errorMessage("Invalid Session")
	else:
		try:
			cookie.load(string_cookie)
			sid = cookie['sid'].value
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
			if username !="":
				db1.close()
				return True,username
			else:
				db1.close()
				return False,""
		except Exception as e:
			db1.rollback()
			error.errorMessage("Invalid Session")
			return False,""
			db1.close()
