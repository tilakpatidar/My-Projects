#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb
print "Content-type:text/html\r\n\r\n"

# Get countries
db1 = MySQLdb.connect("localhost","root","1","member" )
sql1="SELECT country_name FROM country ORDER BY country_name --"
cursor1 = db1.cursor()
try:
   cursor1.execute(sql1)
except:
   print"Unable to fetch country code"


results1 = cursor1.fetchall()



for row1 in results1:
	print row1[0];

db1.close()
