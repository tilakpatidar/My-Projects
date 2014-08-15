#!/usr/bin/python -v3
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,hashlib,sha, time, Cookie, os
cgitb.enable()		
from datetime import datetime
print 'Content-Type: text/html\n'

def messageSeen(u,f):
	try:
		# Open database connection
		db3 = MySQLdb.connect("localhost","root","1","mem_info" )
		# prepare a cursor object using cursor() method
		cursor3 = db3.cursor()
		# execute SQL query using execute() method.
		sql3="UPDATE messages SET seen=1 WHERE msg_to='%s' AND msg_from='%s'"%(u,f)
		# Execute the SQL command
		cursor3.execute(sql3)
		
		db3.commit()
		db3.close()
	except:
		db3.rollback()		
def convertTimeFormat(t):
	d = datetime.strptime(str(t), "%H:%M")
	return d.strftime("%I:%M %p")	

def createRHS(m,t,s):
	
	if s=="0":
		s=""
	elif s=="1":
		
		s="""<span class="glyphicon glyphicon-flag"></span>"""
	
	msg_list="""<li class="alert alert-warning" ><blockquote class="blockquote-reverse" >
                                            <p style="font-size:small;">%s</p>
                                            <div style="float:left;">%s</div><div style="float: right;"><footer>You<br/><p style="font-size: smaller;">%s</p></footer>
                                            </div> </blockquote></li>
					"""%(m,s,t)
	return msg_list



def createLHS(m,f,t,s):
	
	
	s=""
	
	
	temp="""  <li class="alert alert-success" style="background-color:#ffff99;"><blockquote > <p style="font-size: small;">%s</p><div style="float:right;">%s</div><div style="float: left;"><footer>%s<br/><p style="font-size: smaller;">%s</p></footer>
                                            </div>
                                          </blockquote></li>"""%(m,s,f,t)
	
	return temp


def showMessages(username,msg_to):
	
	try:
		
		# Open database connection
		db2 = MySQLdb.connect("localhost","root","1","mem_info" )
		# prepare a cursor object using cursor() method
		cursor2 = db2.cursor()
		# execute SQL query using execute() method.
		sql2="SELECT msg_from,message,time,seen from messages where (msg_to='%s' AND msg_from='%s') OR (msg_to='%s' AND msg_from='%s') ORDER BY time"%(username,msg_to,msg_to,username)
		
		# Execute the SQL command
		cursor2.execute(sql2)
		
		results2=cursor2.fetchall()
		big_str=""
		
		if not results2 is None:
			
			for val in results2:
				frm=str(val[0])
				msg=str(val[1])
				
				time=str(val[2])
				seen=str(val[3])
				temp=time[10:len(time)-3].strip()
				
				time=convertTimeFormat(temp)
				username=str(username)
				
				if frm == username:
					big_str=big_str+createRHS(msg,time,seen)
				else:
					big_str=big_str+createLHS(msg,frm,time,seen)
					
				
		else:
			results2=""
		
		print big_str
		
		db2.commit()
		
		
	except:
		db2.rollback()
	db2.close()


def reply(uname,to,m):
	
	
	#print m
	if not m is None:
		try:
			# Open database connection
			db2 = MySQLdb.connect("localhost","root","1","mem_info" )
			# prepare a cursor object using cursor() method
			cursor2 = db2.cursor()
			# execute SQL query using execute() method.
			sql2="INSERT INTO messages(msg_to,msg_from,message) VALUES('%s','%s','%s')"%(to,uname,m)
			# Execute the SQL command
			cursor2.execute(sql2)
		
		
			db2.commit()
			showMessages(username,msg_to)
		
		except:
			db2.rollback()
			print "Failed"
			#print "Invalid session !"

		db2.close()
		return "Sent"
	else:
		showMessages(username,msg_to)
	
def verifySession(sid):
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","mem_info" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT username from session where sid='%s'"%(sid)
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchone()
		if not results1 is None:
			for val in results1:
				username=val
				break
		else:
			print "Invalid session !"
		
		db1.commit()
		db1.close()
		return username
	except:
		db1.rollback()
		print "Invalid session !"

	db1.close()
	return ""

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

msg_to  =form.getvalue('msg_to')
#username and msg_from are same
msg  =form.getvalue('msg')

#Loading sid from cookie
cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
if string_cookie is None:
	print  "<SCRIPT type='text/javascript'>window.location.href='/';</SCRIPT>"
else:
	cookie.load(string_cookie)
	sid = cookie['sid'].value
	username=verifySession(sid)
	

	if username !="":
		reply(username,msg_to,msg)
		messageSeen(username,msg_to)
		
	else:
		print "Invalid Session"	


