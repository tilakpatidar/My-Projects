#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,hashlib,sha, time, Cookie, os,math
cgitb.enable()
print 'Content-Type: text/html\n'
def verifySession():
	# Create instance of FieldStorage 
	cookie = Cookie.SimpleCookie()
	string_cookie = os.environ.get('HTTP_COOKIE')
	if string_cookie is None:
		return False,False,False
		#errorMessage.message("Invalid Session")
	else:
		try:
			cookie.load(string_cookie)
			sid = cookie['sid'].value
			# Open database connection
			db1 = MySQLdb.connect("localhost","root","1","SRM" )
			# prepare a cursor object using cursor() method
			cursor1 = db1.cursor()
			# execute SQL query using execute() method.
			sql1="SELECT regno,type from session where sid='%s'"%(sid)
			#print sql1
			# Execute the SQL command
			cursor1.execute(sql1)
			username=""
			results1=cursor1.fetchone()
			username=results1[0]
			typee=results1[1]
			db1.commit()
			if username !="":
				db1.close()
				return True,username,typee
			else:
				db1.close()
				return False,False,False
		except Exception as e:
			db1.rollback()
			print e
			#errorMessage.message("Invalid Session")
			return False,False,False
			db1.close()
