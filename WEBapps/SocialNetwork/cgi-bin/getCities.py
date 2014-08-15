#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb
print "Content-type:text/html\r\n\r\n"

form = cgi.FieldStorage() 

country = form.getvalue('country')



# Get country code
db1 = MySQLdb.connect("localhost","root","1","member" )
sql1="SELECT cc_fips FROM country WHERE country_name='%s' --"%(country);
cursor1 = db1.cursor()
try:
   cursor1.execute(sql1)
except:
   print"Unable to fetch country code"


results1 = cursor1.fetchone()

country_code=""

for row1 in results1:
	country_code=row1[0];

db1.close()


# Get cities

db2 = MySQLdb.connect("localhost","root","1","member" )
sql2="SELECT full_name_nd FROM world_cities_free WHERE cc_fips='%s' ORDER BY full_name_nd--"%(country)
cursor2 = db2.cursor()
try:
   cursor2.execute(sql2)
except:
   print"Unable to fetch country code"

results2 = cursor2.fetchall()
for row2 in results2:
	print row2[0]

db2.close()
