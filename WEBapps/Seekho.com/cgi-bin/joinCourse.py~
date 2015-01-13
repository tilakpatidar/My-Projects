#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,verify,time,error,json
cgitb.enable()
li=[]
form = cgi.FieldStorage()
def getUsers(idd):
	db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
	try:
		# Open database connection
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT `course_users` FROM `courses` WHERE `course_id`='%s'"%(idd)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		results1=cursor1.fetchone()
		if results1[0]=="":
			return []
		else:
			return eval(results1[0])
		db1.commit()
	except Exception as e:
		db1.rollback()
		print 'Content-Type: text/html\n'
		print "Invalid session !"
		return ""
	db1.close()
	
def getCourses(username):
	db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
	try:
		# Open database connection
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT `courses` FROM `info` WHERE `username`='%s'"%(username)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		results1=cursor1.fetchone()
		if results1[0]=="":
			return []
		else:
			return eval(results1[0])
		db1.commit()
	except Exception as e:
		db1.rollback()
		print 'Content-Type: text/html\n'
		print "Invalid session !"
		return ""
	db1.close()
q = form.getvalue('id',"#123None#").strip()
t=verify.verifySession()
if q !="#123None#":
	if t[0] and t[1]!="":
		a=getCourses(t[1])
		if q in a:
			print 'Content-Type: text/html\n'
			print "already"
		else:
			a.append(q)
			b=getUsers(q)
			b.append(t[1])
			db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
			try:
				# Open database connection
				# prepare a cursor object using cursor() method
				cursor1 = db1.cursor()
				# execute SQL query using execute() method.
				sql1="UPDATE `info` SET `courses`='%s' where `username`='%s'"%(MySQLdb.escape_string(str(a)),t[1])
				sql2="UPDATE `courses` SET `course_users`='%s' where `course_id`='%s'"%(MySQLdb.escape_string(str(b)),q)
				# Execute the SQL command
				cursor1.execute(sql1)
				cursor1.execute(sql2)
				db1.commit()
				print 'Content-Type: text/html\n'
				print "done"
				print "<username>"+t[1]+"</username>"
			except Exception as e:
				db1.rollback()
				print 'Content-Type: text/html\n'
				print "Invalid session !"
			db1.close()
			
	
	else:
		print 'Content-Type: text/html\n'
		error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
else:
	print 'Content-Type: text/html\n'
	error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
