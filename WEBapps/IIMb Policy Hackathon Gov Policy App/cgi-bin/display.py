#!/usr/bin/python
import cgi,cgitb
form = cgi.FieldStorage()
f = form.getvalue("f")
import MySQLdb
import calculate
print "Content-type:text/html\r\n\r\n"
db = MySQLdb.connect("127.0.0.1","root","1","analytics")
cursor = db.cursor()
sql = "SELECT `name`,`upvote`,`downvote` FROM `"+f+"`;"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
	calculate.evaluate(row[0],row[1],row[2],f)
	break
	

