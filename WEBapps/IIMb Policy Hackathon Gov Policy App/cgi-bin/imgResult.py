#!/usr/bin/python
import cgi,cgitb,MySQLdb,hashlib,os
cgitb.enable()
print "Content-type:text/html\r\n\r\n"
def fetchImages():
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","test" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		sql="SELECT * FROM img;"
		# Execute the SQL command
		cursor.execute(sql)
		results=cursor.fetchall()
		if not results is None:
			for r in results:
				print r[0]+";;"
		db.commit()
	except:
		db.rollback()
	db.close()
fetchImages()
