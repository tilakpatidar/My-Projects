#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,faculty,verify,time,error
#cgitb.enable()
def getHours(username,typee,c,dod,sub):
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","SRM" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT `1`,`2`,`3`,`4`,`5`,`6`,`7` from `%s` where dod=%s"%(str(c),str(dod))
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchone()
		#print results1
		if not results1 is None:
			li=list(results1)
			temp=""
			for index,item in enumerate(li):
				if item==sub:
					a=str(index+1)
					temp+="""<div class="checkbox">
          <label>
          <input type="checkbox" name="dod%s"  id="dod%s" value="dod%s"> %s
          </label>
        </div>"""%(a,a,a,a)
			print temp
		else:
			print 0
		db1.commit()
	except Exception as e:
		db1.rollback()
		print e
		print error.errorMessage('Unable to get request for hours.','Contact ITKM');
		db1.close()
form = cgi.FieldStorage() 
# Get data from fields
c = form.getvalue('c',"#123None#").strip()
dod = form.getvalue('dod',"#123None#").strip()
sub = form.getvalue('sub',"#123None#").strip()
if c!="#123None#" and dod!="#123None#" and sub!="#123None#":
	t=verify.verifySession()
	if t[0] and (str(t[2])[:1]=='3' or str(t[2])[:1]=='1' or str(t[2])[:1]=='2'):
		getHours(t[1],t[2],c,dod,sub)
	else:
		error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
