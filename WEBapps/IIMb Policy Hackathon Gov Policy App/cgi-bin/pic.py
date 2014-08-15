#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
def uploadPic(fn):
	uploaded=False
	try:
		open('/var/www/SRMSE/public_html/images/' + fn, 'wb').write(fileitem.file.read())
		uploaded=True
	except Exception as e:
		print e
	if uploaded:
		try:
		
			# Open database connection
			db = MySQLdb.connect("localhost","root","1","test" )
			# prepare a cursor object using cursor() method
			cursor = db.cursor()
			# execute SQL query using execute() method.
			sql="INSERT INTO img VALUES('%s')"%(fn)
			# Execute the SQL command
			cursor.execute(sql)
			db.commit()
		
		except:
			db.rollback()
			os.remove('/var/www/SRMSE/public_html/images/'+fn)
		db.close()
		
import cgi,cgitb,MySQLdb,hashlib,os
try: # Windows needs stdio set for binary mode for uploading file.
    	import msvcrt
    	msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    	msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    	pass
#cgitb.enable()
form = cgi.FieldStorage()
fileitem=form['file']
if not fileitem is None:
	uploadPic(fileitem.name)
