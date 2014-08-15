#!/usr/bin/python
import cgi, os,MySQLdb
import cgitb
print "Content-Type: text/html\r\n\r\n"
#cgitb.enable()
form = cgi.FieldStorage()
pid=form.getvalue('pid')
temp=""
def fetch(pid):
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","iimb" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		#1 for gov and 0 for suggested
		sql="SELECT pid,ptitle,pdesc from main where pid='%s';"%(pid)
		# Execute the SQL command
		cursor.execute(sql)
		results=cursor.fetchall()
		#print results
		if not results is None:
			for r in results:
				temp=r[0]+";;"+r[1]+";;"+r[2]
		db.close()
		return temp
	except:
		print "Unable to update the database !"
a=fetch(pid)
if not a is None:
	print a
