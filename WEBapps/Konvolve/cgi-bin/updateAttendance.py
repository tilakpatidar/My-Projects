#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,faculty,verify,time,error
from multiprocessing import Pool
#cgitb.enable()
def getMembers(c):
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","SRM" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT members from class where classid=%s"%(str(c))
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchone()
		#print results1
		if not results1 is None:
			li=eval(results1[0])
			db1.commit()
			db1.close()
			return li
		else:
			db1.commit()
			db1.close()
			return []
		db1.commit()
	except Exception as e:
		db1.rollback()
	db1.close()
form = cgi.FieldStorage() 
# Get data from fields
inputDate = form.getvalue('inputDate',"#123None#").strip()
inputClass = form.getvalue('inputClass',"#123None#").strip()
inputSub = form.getvalue('inputSub',"#123None#").strip()
dod1 = str(form.getvalue('dod1',"#123None#").strip())
dod2 = str(form.getvalue('dod2',"#123None#").strip())
dod3= str(form.getvalue('dod3',"#123None#").strip())
dod4 = str(form.getvalue('dod4',"#123None#").strip())
dod5 = str(form.getvalue('dod5',"#123None#").strip())
t=verify.verifySession()
inputDod=[]
if t[0] and str(t[2])[:1]=='3':
	if dod1=="dod1":
		inputDod.append('1')
	if dod2=="dod2":
		inputDod.append('2')
	if dod3=="dod3":
		inputDod.append('3')
	if dod4=="dod4":
		inputDod.append('4')
	if dod5=="dod5":
		inputDod.append('5')		
	x=str(inputClass.split(':')[-1])
	mem=getMembers(x)
	temp=[]
	for m in mem:
		exec("mem%s= form.getvalue('%s','#123None#').strip()"%(m,m))
		exec("if mem%s=='on':\n\ttemp.append(('%s','%s','%s','%s','1'))\nelse:\n\ttemp.append(('%s','%s','%s','%s','0'))"%(m,m,inputSub,inputDate,str(';'.join(inputDod)),m,inputSub,inputDate,str(';'.join(inputDod))))
	p = Pool(10)
	#print temp
	p.map(faculty.updateAttendance,temp)
	#p.join()
	#faculty.refreshAttendance(t[1],t[2])
elif (str(t[2])[:1]=='1' or str(t[2])[:1]=='2'):
	error.errorMessage("Invalid Login Attempt!","You are already logged in as a student.")
else:
	error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")

