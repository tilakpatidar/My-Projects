#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,verify,time,error,urllib2
cgitb.enable()
form = cgi.FieldStorage() 
# Get data from fields
comments=""
def getComments(idd):
	global comments
	db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
	try:
		# Open database connection
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT `comment_user`, `comment_desc`, `comment_time`,`comment_id` FROM `comment` WHERE `comment_course`='%s'"%(idd)
		# Execute the SQL command
		cursor1.execute(sql1)
		results=cursor1.fetchall()
		if results:
			for row in results:
				comments+="""<div class="row" style="width:100&percnt;;">
<div class="col-lg-12" style="width:100&percnt;;">
<div class="well">
                    <h5>%s</h5>
                    <form role="form">
                        <div class="form-group">
                            <label class="label" style="font-size:20px;color:black;">%s</label>
                        </div>
                        <label class="label"style="font-size:14px;color:black;">Commented on</label><label style="font-size:10px;color:black;" class="label">%s</label>
                        <button class="like btn btn-primary glyphicon glyphicon-thumbs-up" name="%s"> Like</button>
                        
                    </form>
                </div>
</div>
</div>"""%(row[0],row[1],row[2],row[3])
		else:
			comments="""<div class="row" id="no_comment" style="width:100&percnt;;">
<div class="col-lg-12" style="width:100&percnt;;">
<div class="well">
                    <h5><i>No comments yet</i></h5>
                </div>
</div>
</div>"""
		db1.commit()
	except Exception as e:
		db1.rollback()
		print 'Content-Type: text/html\n'
		error.errorMessage("Problem in session creation",e)
	db1.close()
def updateComment(text,idd):
	db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
	try:
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1 = "INSERT INTO `comment`(`comment_user`, `comment_desc`,`comment_course`) VALUES ('%s','%s','%s');"%(t[1],text,idd)
		cursor1.execute(sql1)
		results=cursor1.fetchone()
		db1.commit()
		return True
	except Exception as e:
		db1.rollback()
		print 'Content-Type: text/html\n'
		error.errorMessage("Problem in session creation",e)
	return False
	db1.close()





q = form.getvalue('query',"#123None#").strip()
q=urllib2.unquote(q)
idd = form.getvalue('id',"#123None#").strip()
idd=urllib2.unquote(idd)
if q !="#123None#":
	t=verify.verifySession()
	if t[0] and t[1]!="":
		if updateComment(q,idd):
			getComments(idd)
			print 'Content-Type: text/html\n'
			print "###success###"
			print comments
			comments=""
	else:
		print 'Content-Type: text/html\n'
		print "###not logged in###"
