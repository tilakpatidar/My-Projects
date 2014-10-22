#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,faculty,verify,time,error
#cgitb.enable()
def getDod(username,typee,d):
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","SRM" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT dod.dod from dod where date='%s'"%(str(d))
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchone()
		#print results1
		if not results1 is None:
			date=results1[0]
			print date
		else:
			print 0
		db1.commit()
	except Exception as e:
		db1.rollback()
		print e
		print error.errorMessage('Unable to get request for day orders.','Contact ITKM');

	db1.close()
form = cgi.FieldStorage() 
# Get data from fields
d = form.getvalue('d',"#123None#").strip()
if d!="#123None#":
	t=verify.verifySession()
	if t[0] and (str(t[2])[:1]=='3' or str(t[2])[:1]=='1' or str(t[2])[:1]=='2'):
		getDod(t[1],t[2],d)
	else:
		error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
