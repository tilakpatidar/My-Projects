#!/usr/bin/python
import cgi, os,MySQLdb
import cgitb
print "Content-Type: text/html\r\n\r\n"
cgitb.enable()
form = cgi.FieldStorage()
pid=form.getvalue('pid')
comment=form.getvalue('comment')
def comment(comment,pid):
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","iimb" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		sql="UPDATE `main` SET `comment`=CONCAT(CONCAT(`comment`,';;'),'%s')where `pid`='%s'"%(comment,pid)
		# Execute the SQL command
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
		print "Unable to update the database !"
	db.close()
comment(comment,pid)

