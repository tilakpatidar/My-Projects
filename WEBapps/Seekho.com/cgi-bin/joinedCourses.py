#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,verify,time,error,json
cgitb.enable()
li=[]
form = cgi.FieldStorage()
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
		print e
		print "Invalid session !"
		return ""
	db1.close()
t=verify.verifySession()
if t[0] and t[1]!="":
	a=getCourses(t[1])
	if a!=[]:
		db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
		try:
			ids=tuple(a)
			# Open database connection
			# prepare a cursor object using cursor() method
			cursor1 = db1.cursor()
			# execute SQL query using execute() method.
			sql1="SELECT `course_id`, `course_title`, `course_desc`, `course_author`, `course_content`, `course_category` from courses where `course_id` IN %s;"%(str(ids))
			#print sql1
			# Execute the SQL command
			cursor1.execute(sql1)
			results1=cursor1.fetchall()
			if results1 is not None:
				for row in results1:
					li.append("""<li class="list-group-item"">
					<h2 style="">%s</h2>
		               <p><strong>Course id: </strong>%s </p>
		               <p><strong>Description: </strong>%s</p>
		               <p><strong>Category: </strong>%s </p>
		               <p><strong>Author: </strong>%s </p>
		               <p>
		               <a href="/cgi-bin/showCourse.py?id=%s" class="glyphicon glyphicon-th-list btn btn-primary">&nbsp;View Contents</a>
		                </p>
		                </li>
					"""%(row[1],row[0],row[2],row[5],row[3],row[0]))
			db1.commit()
			ans="""<div class="container" style="width:100&percnt;;">
		<div class="row">
		<div class="col-lg-12">
		<ul class="list-group">
		%s
		</ul>
		</div>
		</div>
		</div>
	      </div>"""%(''.join(li))
			print 'Content-Type: text/html\n'
			print ans
		except Exception as e:
			db1.rollback()
			print 'Content-Type: text/html\n'
			print e
			print "Invalid session !"
		db1.close()
	else:
		print 'Content-Type: text/html\n'
		print "<strong>No courses enrolled!</strong>"
	
else:
	print 'Content-Type: text/html\n'
	error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
