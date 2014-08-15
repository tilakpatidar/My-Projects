#!/usr/bin/python -v3
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,hashlib,sha, time, Cookie, os

def newSession(sid,username):
	try:
		
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","mem_info" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="INSERT into session(sid,username) VALUES('%s','%s')"%(sid,username)
		# Execute the SQL command
		cursor1.execute(sql1)
		db1.commit()
		
	except:
		db1.rollback()
		print "Could not create new session !"
	db1.close()


cgitb.enable()
cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('uname')
password  =form.getvalue('pswd')
chk=str(form.getvalue('chk'))
sid=''
	
key=str(password)
#Step 1 conversion of input to md5

m = hashlib.md5()
m.update(key)
s1=m.hexdigest()
#print 'Step 1 md5 ',s1

#Step 2 Conversion of s1 to salt
#By adding salt from 2 places from right as well left

salt=r'tilak@Google05-05-1995#IndiaSal$100000$'
l=len(s1)
mid=s1[2:-2]

s2=str(s1[0]+s1[1]+salt+mid+salt+s1[-2]+s1[-1])
#print 's2  ',s2
#Step 3
#Converting salt version to md5 again

m=hashlib.md5()
m.update(s2)
s3=m.hexdigest()

#print 's3  ',s3


#Step 4 
#Replacement algorithm
#replacing 9 by 1
temp=s3.replace('9','1')
#replacing 0 by 5
temp=temp.replace('0','5')
#replacing a by t
temp=temp.replace('a','t')

password=temp


# Open database connection
db = MySQLdb.connect("localhost","root","1","mem_info" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
sql="SELECT password from admin where username='%s'"%(username)

# Execute the SQL command
cursor.execute(sql)
# Fetch all the rows in a list of lists.
results=cursor.fetchone()
pswd=results[0]
#print results[0]
#print password
if pswd==password:
	
	if chk=="1":
		# If new session
		if not string_cookie:
		   
		   # The sid will be a hash of the server time
		   sid = sha.new(repr(time.time())).hexdigest()
		   # Set the sid in the cookie
		   cookie['sid'] = sid
		   #cookie['sid']['path']="/cookie"
		   # Will expire in a 7days
		   
		   cookie['sid']['expires'] =7 * 24 * 60 * 60
		  
		else:
		   cookie.load(string_cookie)
		   sid = cookie['sid'].value
		   


	else:
		# If new session
		if not string_cookie:
		   
		   # The sid will be a hash of the server time
		   sid = sha.new(repr(time.time())).hexdigest()
		   # Set the sid in the cookie
		   cookie['sid'] = sid
		   #cookie['sid']['path']="/cookie"
		   # Will expire in a 6h
		   cookie['sid']['expires'] =1 * 6 * 60 * 60 
		   
		else:
		   cookie.load(string_cookie)
		   sid = cookie['sid'].value	  

		
		
        
	print cookie	
	print 'Content-Type: text/html\n'
	print '<html><body>'
	print "Access"
	if string_cookie:
   		print '<p>Already existent session</p>'
		print  "<SCRIPT type='text/javascript'>window.location.href='homePage.py';</SCRIPT>"
	else:
   		newSession(sid,username)
		print  "<SCRIPT type='text/javascript'>window.location.href='homePage.py';</SCRIPT>"
else:
	print "no access"

# disconnect from server
db.close()

