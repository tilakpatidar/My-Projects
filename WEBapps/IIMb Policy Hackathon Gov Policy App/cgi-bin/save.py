#!/usr/bin/python
import cgi, os,MySQLdb
import cgitb
print "Content-Type: text/html\r\n\r\n"
#cgitb.enable()
form = cgi.FieldStorage()
# A nested FieldStorage instance holds the file
fileitem = form['file']
def update(pid,ptitle,pdesc):
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","iimb" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		sql="INSERT into main (pid,ptitle,pdesc) VALUES ('%s','%s','%s');"%(pid,ptitle,pdesc)
		# Execute the SQL command
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
		print "Unable to update the database !"
	db.close()
# Test if the file was uploaded
if fileitem.filename:
	# strip leading path from file name to avoid directory traversal attacks
	fn = os.path.basename(fileitem.filename)
	open('/var/www/cgi-bin/files/' + fn, 'wb').write(fileitem.file.read())
	message = 'The file "' + fn + '" was uploaded successfully' 
else:
	message = 'No file was uploaded'
import csv
l=[]
with open('/var/www/cgi-bin/files/' + fn, 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=r';', quotechar='|')
	for row in spamreader:
		', '.join(row)
		update(row[0],row[1],row[2])
print """
<html><body>
<p>%s</p>
</body></html>
""" % (message,)
print "Please wait 5 seconds Redirecting"
print r"""
<meta HTTP-EQUIV="REFRESH" content="5; url=/vote">"""
