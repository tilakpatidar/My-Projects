#!/usr/bin/python
# Import modules for CGI handling 
import cgi,MySQLdb,hashlib,sha, time, Cookie, os,math,student,error
#print 'Content-Type: text/html\n'
def verifySession(sid):
	try:
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
	except:
		db1.rollback()
		error.errorMessage("Problem in session creation","Invalid username and password combination or try clearing your cookie data.")

	db1.close()
	return username,typee

#Loading sid from cookie
cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
if string_cookie is None:
	print  "<SCRIPT type='text/javascript'>window.location.href='/login';</SCRIPT>"
else:
	cookie.load(string_cookie)
	sid = cookie['sid'].value
	temp=verifySession(sid)
	username=str(temp[0])
	typee=str(temp[1])
	course=typee[:1]
	if username !="":
		if course=="1" or course=="2":
			#print cookie	
			#print 'Content-Type: text/html\n'
			print  "<SCRIPT type='text/javascript'>window.location.href='/cgi-bin/student.py';</SCRIPT>"
		elif course=="3":
			#print cookie	
			#print 'Content-Type: text/html\n'
			print "<script type='text/javascript'>window.location='/cgi-bin/faculty.py';</script>"
	else:
		#clear all cookie data see to it
		error.errorMessage("Problem in session creation","Invalid username and password combination or try clearing your cookie data.")
	
