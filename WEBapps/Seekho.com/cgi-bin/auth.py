#!/usr/bin/python
# Import modules for CGI handling 
import cgi,MySQLdb,hashlib,sha, time, Cookie, os,math,error,cgitb
def hashPassword(key):
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
	return str(temp)
def newSession(sid,username):
	try:
		# Open database connection
		db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="INSERT into session(sid,username) VALUES('%s','%s')"%(sid,username)
		# Execute the SQL command
		cursor1.execute(sql1)
		db1.commit()
	except Exception as e:
		db1.rollback()
		print 'Content-Type: text/html\n'
		error.errorMessage("Problem in session creation",e)
		return False
	db1.close()
	return True
def authenticate(username,password):
	try:
		# Open database connection
		db = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )

		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		# execute SQL query using execute() method.
		sql="SELECT pswd from auth where username='%s'"%(username)
		# Execute the SQL command
		cursor.execute(sql)
		# Fetch all the rows in a list of lists.
		results=cursor.fetchone()
		pswd=str(results[0])
		if pswd.strip()==password.strip():
		
			if chk=="on":
				# If new session
				if not string_cookie:
				   
				   # The sid will be a hash of the server time
				   sid = sha.new(repr(time.time())).hexdigest()
				   # Set the sid in the cookie
				   cookie['sid'] = sid
				   #cookie['sid']['path']="/cookie"
				   # Will expire in a 2days
				   
				   cookie['sid']['expires'] =2 * 24 * 60 * 60
				  
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
			if newSession(sid,username):
					print cookie	
					print 'Content-Type: text/html\n'
					print "<script type='text/javascript'>window.location='/cgi-bin/user.py';</script>"
			else:
				print ""
		else:
			print 'Content-Type: text/html\n'
			error.errorMessage("Problem in session creation","Invalid username and password combination")
		db.commit()
	except Exception as e:
		db.rollback()
		print 'Content-Type: text/html\n'
		error.errorMessage("Problem in session creation","Invalid username and password combination")

	
	db.close()

cgitb.enable()
cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
form = cgi.FieldStorage()
username = form.getvalue('username',"#123None#").strip()
password  =form.getvalue('pswd',"#123None#").strip()
chk=str(form.getvalue('chk',"#123None#"))#Chk true=on #Chk false=#123None#
sid=''
if username=="#123None#" or password=="#123None#":
	print "No input"
password=hashPassword(str(password))
authenticate(username,password)
