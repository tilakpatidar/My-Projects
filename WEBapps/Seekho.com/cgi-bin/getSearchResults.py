#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,verify,time,error,json
cgitb.enable()
form = cgi.FieldStorage()
def main(url):
	try:
		# Open database connection
		db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT `course_id`, `course_title`, `course_desc`, `course_author`, `course_duration`,`course_content`, `course_category`,`course_users` from courses where `course_title` LIKE '%s' OR `course_desc` LIKE '%s' OR `course_author` LIKE '%s' OR `course_category` LIKE '%s';"%(q,q,q,q)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		results1=cursor1.fetchall()
		li=[]
		base=""
		if results1==():
			print 'Content-Type: text/html\n'
			print "no"
		elif results1 is not None:
			for row in results1:
				if url=="##":
					if row[7]!="":
						li=eval(row[7])
						if t[1] in li:
							idd=str(row[0])	
							b="glyphicon glyphicon-ok btn btn-success\">&nbsp;Course Joined"
							a="javascript:alert('Already joined the course');"
						else:
							idd=str(row[0])	
							b="join glyphicon glyphicon-plus btn btn-primary\">&nbsp;Join Course"
							a="#"
					else:
						idd=str(row[0])	
						b="join glyphicon glyphicon-plus btn btn-primary\">&nbsp;Join Course"
						a="#"
				else:
					a=url
					idd=a
					b=""
				li.append("""<li class="list-group-item"">
				<h2 style="">%s</h2>
                       <p><strong>Course id: </strong>%s </p>
                       <p><strong>Description: </strong>%s</p>
                       <p><strong>Category: </strong>%s </p>
                       <p><strong>Duration: </strong>%s min </p>
                       <p><strong>Author: </strong>%s </p>
                       <p>
                       <a href="/cgi-bin/showCourse.py?id=%s" class="glyphicon glyphicon-th-list btn btn-primary">&nbsp;View Contents</a>
                        <a name="%s" href="%s" class="%s</a>
                        </p>
                        </li>
				"""%(row[1],row[0],row[2],row[6],row[4],row[3],row[0],idd,a,b))
			base=""" <div class="container" style="width:100&percnt;;">
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
			print base
		db1.commit()
	except Exception as e:
		db1.rollback()
		print 'Content-Type: text/html\n'
		print "Invalid session !"
	db1.close()
q = form.getvalue('query',"#123None#").strip()
if q !="#123None#":
	q="%"+q+"%"
	t=verify.verifySession()
	if t[0] and t[1]!="":
		url="##"
		main(url)
	else:
		url="javascript:alert('Please login to join the course');"
		main(url)
else:
	print 'Content-Type: text/html\n'
	error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
