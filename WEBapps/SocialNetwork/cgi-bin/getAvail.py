#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb
print "Content-type:text/html\r\n\r\n"


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('username')

# Open database connection
db = MySQLdb.connect("localhost","root","1","mem_info" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
sql="SELECT mem_id from info where username='%s'"%(username,password)



try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   if cursor.rowcount==0:
	print"Available"
   else:
        print "Not Available"
      
      
except:
   print "Error: unable to fecth data"



# disconnect from server
db.close()
print "<HTML><HEAD><TITLE></TITLE></HEAD><BODY></BODY></HTML>"
