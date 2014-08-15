#!/usr/bin/python
import cgi, os,MySQLdb
import cgitb
print "Content-Type: text/html\r\n\r\n"
#cgitb.enable()
form = cgi.FieldStorage()
def fetch():
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","iimb" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		#1 for gov and 0 for suggested
		sql="SELECT pid,ptitle,pdesc,time from main where status='1' ORDER BY time DESC"
		# Execute the SQL command
		cursor.execute(sql)
		results=cursor.fetchall()
		temp=""
		fresult=""
		if not results is None:
			for r in results:
				for rr in r:
					temp+=str(rr)+"||"
				fresult+=temp+";;"
				temp=""
		db.close()
		return fresult
	except:
		print "Unable to update the database !"
a=fetch()
if not a is None:
	print a
