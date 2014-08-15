#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()


form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('/usr/lib/cgi-bin/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
print "Content-Type: text/html\r\n\r\n"
import csv
with open(fn, 'rb') as csvfile:
 spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
 for row in spamreader:
  ', '.join(row)

row=row[0]
x=row.split(",")
print "Content-Type: text/html\r\n\r\n"
import con
cur=con.cur
db=con.db


cur.execute("INSERT INTO `%s` VALUES(%d,'%s','%s','%s','%s','%s','%s','%s','%s',%d,%d,'%s','%s','%s','%s','%s')" %(x[0],int(x[1]),x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],int(x[10]),int(x[11]),x[12],x[13],x[14],x[15],x[16]))	
db.commit()
print """
<html><body>
<p>%s</p>
</body></html>
""" % (message,)


