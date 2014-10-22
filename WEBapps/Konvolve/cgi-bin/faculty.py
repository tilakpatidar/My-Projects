#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,verify,error
from threading import Thread
cgitb.enable()
def createPortal(username):
	fname=""
	lname=""
	regno=""
	branch=""
	sec=""
	year=""
	typee=""
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","SRM" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT faculty.regno,faculty.fname,faculty.lname,faculty.type,dept.dept_name from faculty,dept where faculty.regno='%s' and faculty.dept_id=dept.dept_id"%(username)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchone()
		#print results1
		regno=results1[0]
		fname=results1[1]
		lname=results1[2]
		typee=results1[3]#Not using
		branch=results1[4]
		db1.commit()
	except Exception as e:
		db1.rollback()
		print e
		print error.errorMessage('Unable to login !','Please contact ITKM.')

	db1.close()
	print """<!DOCTYPE html>
	<!--
	To change this license header, choose License Headers in Project Properties.
	To change this template file, choose Tools | Templates
	and open the template in the editor.
	-->
	<html>
	    <head>
		<title>SRM OD Portal</title>
		<link rel="shortcut icon" href="/images/fav.ico">
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		 <link rel="stylesheet" href="/css/faculty.css">
		<link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">
	    </head>
	    <body>
	       
		<div id="main">
		    <div class="container" >
		            
		                        <nav class="navbar navbar-default" role="navigation">
		                            <div class="container-fluid">
		                              <!-- Brand and toggle get grouped for better mobile display -->
		                              <div class="navbar-header">
		                                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
		                                  <span class="sr-only">Toggle navigation</span>
		                                  <span class="icon-bar"></span>
		                                  <span class="icon-bar"></span>
		                                  <span class="icon-bar"></span>
		                                </button>
		                                <a class="navbar-brand">Faculty Portal</a>
		                              </div>

		                            <!-- Collect the nav links, forms, and other content for toggling -->
		                            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
		                              
		                              <ul class="nav navbar-nav navbar-right">
		                               
		                                <li class="dropdown">
		                                  <a href="#" class="dropdown-toggle" data-toggle="dropdown">%s<span class="caret"></span></a>
		                                  <ul class="dropdown-menu" role="menu">
		                                    <li><a href="#">Account Settings</a></li>
		                                    <li><a href="#">Report Problem</a></li>
		                                    <li class="divider"></li>
		                                    <li><a href="/cgi-bin/logout.py">LogOut</a></li>
		                                  </ul>
		                                </li>
		                              </ul>
		                            </div><!-- /.navbar-collapse -->
		                          </div><!-- /.container-fluid -->
	</nav>
		        <div class="row">
		            <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12" style="height: 40&percnt;;">
		                     <ul class="nav nav-pills nav-stacked">
		                         <li><a id="home" class="tabs" href="/cgi-bin/faculty.py">Home</a></li>
		                    <li><a class="tabs" id="attendance">Update Attendance</a></li>
		                    <li><a class="tabs" id="od">Apply for OD</a></li>
		                    <li><a class="tabs" id="ml">Apply for ML</a></li>
		                </ul>
		            </div>
		            <div  class="col-lg-9 col-md-9 col-sm-12 col-xs-12" style="height: 100&percnt;;" >
		                <div id="mainArea" class="jumbotron" style="height: 100&percnt;;">
		                <div class="row" style="height: 100&percnt;;">
		                        <div class="col-xs-12 col-md-3 col-lg-3 col-sm-12">
		                          <a  class="thumbnail">
		                            <img data-src="holder.js/100&percnt;x180" alt="...">
		                          </a>
		                        </div>
		                        <div  class="col-lg-9 col-md-9 col-xs-12 col-sm-12">
		                        <form class="form-horizontal">
		                                    <fieldset>
		                                         <legend>Faculty Details</legend>
		                                            <div class="form-group">
		                                              <label for="inputFname" class="col-lg-2 control-label">First Name</label>
		                                              <div class="col-lg-10">
		                                                  <input type="text" disabled class="form-control" id="inputFname" placeholder="First Name" value="%s">
		                                              </div>
		                                            </div>
		                                            <div class="form-group">
		                                              <label for="inputLname" class="col-lg-2 control-label">Last Name</label>
		                                              <div class="col-lg-10">
		                                                  <input type="text" disabled class="form-control" id="inputLname" placeholder="Last Name" value="%s">
		                                              </div>
		                                            </div>
		                                            <div class="form-group">
		                                              <label for="inputRegNo" class="col-lg-2 control-label">Registration Number</label>
		                                              <div class="col-lg-10">
		                                                  <input type="text" disabled class="form-control" id="inputRegNo" placeholder="Registration Number" value="%s">
		                                              </div>
		                                            </div>
		                                        
                                                       <div class="form-group">
		                                              <label for="inputBranch" class="col-lg-2 control-label">Branch</label>
		                                              <div class="col-lg-10">
		                                                  <input type="text" disabled class="form-control" id="inputBranch" placeholder="Branch" value="%s">
		                                              </div>
		                                              </div>
		                                    </fieldset>
		                                </form>
		                        </div>
		                        </div>
		                </div>
		            </div>
		               
		        </div>
		    </div>
		</div>
		    <div  class="navbar-default navbar-fixed-bottom">
		        <div class="navbar-header">
		            <a class="navbar-brand" target="blank" href="http://www.srmuniv.ac.in">    <img src="/images/logo.png" width="20" height="20"/> SRM University</a>
		        </div>
		        <div class="navbar-right">
		            <a class="navbar-brand" target="blank" href="http://evarsity.srmuniv.ac.in/srmswi/usermanager/youLogin.jsp">Evarsity</a>
		             <a class="navbar-brand" target="blank" href="#">Contact Us</a>
		              <a class="navbar-brand" target="blank" href="#">Help</a>
		        </div>
	   
		    </div>
		<div class="modal hide" style="z-index:99;background-color:white;opacity:0.6;" id="pleaseWaitDialog" data-backdrop="static" data-keyboard="false"><div class="modal-body" >    <h1>Processing... <img src="/images/wait.gif"/ width=100 height=100>  </h1>          </div>    </div>'
	</body>
	    <!--Scripts at the end-->
	     <script type="text/javascript" src="/js/jQuery/jQuery.js"></script>
	      <script type="text/javascript" src="/bootstrap/js/bootstrap.min.js"></script> 
		 <script type="text/javascript" src="/js/faculty.js"></script>
		 
	</html>"""%(str(fname+" "+lname),fname,lname,regno,branch)
def refreshPortal():
	pass
def loadStudents(username,typee,c):
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","SRM" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT members from class where classid='%s'"%(c)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchall()
		temp=""""""
		if not results1 is None:
			for r in results1:
				exec('mem=%s'%(r[0]))
			for m in mem:
				temp+="""<div class="checkbox">
          <label>
            <input type="checkbox" name="%s"> %s
          </label>
        </div>"""%(m,m)
		print """  <div class="form-group">
      <div class="col-lg-10">
       
        %s
      </div>
    </div>"""%(temp)
		db1.commit()
	except Exception as e:
		db1.rollback()
		#print e
		#print error.errorMessage('Unable to login !','Please contact ITKM.')

	db1.close()
def getClasses(username,typee):
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","SRM" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT class.sec,(SELECT dept.dept_name from dept where dept.dept_id IN(SUBSTRING(class.type,2))),class.year,class.classid,class.type from class where class.classid IN(SELECT sub.class from sub where sub.regno='%s')"%(username)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchall()
		#print results1
		temp=[]
		if not results1 is None:
			for r in results1:
				course=""
				x=str(r[4])[:1]
				if x=='1':
					course="BTech"
				elif x=='2':
					course="MTech"
				temp.append("<option>"+r[1]+"  "+r[0]+"  "+course+" Year : "+str(r[2])+" Class ID :"+str(r[3])+"</option>")
		print ''.join(temp)
		db1.commit()
	except Exception as e:
		db1.rollback()
		#print e
		#print error.errorMessage('Unable to login !','Please contact ITKM.')

	db1.close()
def getSub(username,typee,q):
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","SRM" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT class from sub where regno='%s' and class LIKE '%s;"%(username,q)+"%'"
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchall()
		temp=[]
		if not results1 is None:
			for r in results1:
				temp.append("<option>"+r[0].split(';')[1]+"</option>")
		print ''.join(temp)
		db1.commit()
	except Exception as e:
		db1.rollback()
		print e
		#print error.errorMessage('Unable to login !','Please contact ITKM.')

	db1.close()
def refreshAttendance(username,typee):
	def cAttendance(i):
		pass
			
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","SRM" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT `sub`,`desc` ,`max`,`attended`,`absent`,`avg`,`od_avg`,`total_avg`,`info` from `%s`"%(username)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		results1=cursor1.fetchall()
		strr=""
		avg=0
		t_avg=0
		od_avg=0
		count=0
		if not results1 is None:
			for r in results1:
				count+=1
				s="""<tr><td>%s</td>
		                            <td>%s</td>
		                            <td>%s</td>
		                            <td>%s</td>
		                            <td>%s</td>
		                            <td>%s</td>
		                            <td>%s</td>
		                            <td>%s</td></tr>"""%(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7])
				strr=strr+s
				avg+=float(r[5])
				od_avg+=float(r[6])
				t_avg+=float(r[7])
				cAttendance(r[8])
		#exec('dic=%s'%())
		temp="""      <div class="table-responsive">
                          <table class="table table-bordered">
                              
                              <thead>COURSEWISE ATTENDANCE</thead>
                              <tbody>
                                  <tr style="background-color:white;">
                                  <th>Code</th>
                                  <th>Description</th>
                                  <th>Max. Hours</th>
                                  <th>Attended Hours</th>
                                  <th>Absent Hours</th>
                                  <th>Average &percnt;</th>
                                  <th>OD/ML &percnt;</th>
                                  <th>Total &percnt;</th>
                              </tr>
                              %s
                              <tr style="background-color: white;">
                                  <td colspan="5" style="text-align:center;">Total</td>
                                  <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                              </tr>
                          </tbody>
                            </table>
                                <table class="table table-bordered">
                              
                              <thead >CUMULATIVE ATTENDANCE (IN HOURS)</thead>
                              <tbody>
                                  <tr style="background-color:white;">
                                  <th>Month/Year</th>
                                  <th>Present</th>
                                  <th>Absent</th>
                                  <th>OD(Present)</th>
                                  <th>OD(Absent)</th>
                                  <th>ML</th>
                              </tr>
                              <tr>
                                  <td>Jul-2014</td>
                                    <td>148</td>
                                    <td>1</td>
                                    <td>0</td>
                                    <td>0</td>
                                    <td>0</td>
                              </tr>
                            
                          </tbody>
                            </table>
                                     <table class="table table-bordered">
                              
                              <thead >LEGEND</thead>
                              <tbody>
                                  <tr style="background-color:white;">
                                  <th>Type</th>
                                  <th>Description</th>
                              </tr>
                              <tr>
                                  <td>OD-Present</td>
                                    <td>NCC,NSS (Annual Camp),NSS (Blood Donation),Campus Recruitment Programs,
Competitive Examinations,Sports Activity,Equivalent Assignment Decided by HOD</td>
                                   
                              </tr>
                              <tr>
                              <td>OD-Absent</td>
                              <td>Seminar,Conference,Cultural Actitivity,Intra Department Activity</td>
                              </tr>
                              <tr>
                                  <td>ML</td>
                                  <td>Medical Leave</td>
                              </tr>
                          </tbody>
                            </table>
                                  <table class="table table-bordered">
                              
                              <thead >OD / ML Calculation details</thead>
                              <tbody>
                                  <tr style="background-color:white;">
                                  <th>Percentage</th>
                                  <th>Description</th>
                              </tr>
                              <tr>
                                  <td>
                                      0&percnt; to 64.99&percnt;
                                  </td>
                                  <td>No applicable for OD / ML</td>
                              </tr>
                              <tr>
                                   <td>
                                      65&percnt; to 74.99&percnt;
                                  </td>
                                  <td>Eligible for OD / ML maximum of 10&percnt; added to Actual percentage and make upto 
75 &percnt; only</td>
                              </tr>
                              <tr>
                                  <td>75&percnt; to 100&percnt;</td>
                                    <td>Eligible for OD / ML maximum of 25&percnt;</td>
                                   
                              </tr>
                              <tr>
                              <td>OD-Absent</td>
                              <td>Seminar,Conference,Cultural Actitivity,Intra Department Activity</td>
                              </tr>
                              <tr>
                                  <td>ML</td>
                                  <td>Medical Leave</td>
                              </tr>
                          </tbody>
                            </table>
                            </div>"""%(strr,str(avg/count),str(od_avg/count),str(t_avg/count))
                print temp
	except Exception as e:
		print e
		db1.rollback()
		print "Invalid session !"

	db1.close()
def updateAttendance(temp):
	username,sub,d,dod,status=temp
	try:
		# Open database connection
		db1 = MySQLdb.connect("localhost","root","1","SRM" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT `info`,`max`,`attended`,`absent`,`avg`,`od_avg`,`total_avg` from `%s` where sub='%s'"%(username,sub)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		results1=cursor1.fetchone()
		#print results1	
		if str(results1[0])=="":
			info={}
			maxx=float(results1[1])
			attended=float(results1[2])
			absent=float(results1[3])
			avg=float(results1[4])
			od_avg=float(results1[5])
			total_avg=float(results1[6])
			for dd in dod.split(';'):
				if not d+';'+dd in info:
					info[d+';'+dd]=status
					maxx+=1
					if status=='1':
						attended+=1
					elif status=='0':
						absent+=1
					avg=float((attended/maxx)*100)
					total_avg=float(avg+od_avg)
		else:
			maxx=float(results1[1])
			attended=float(results1[2])
			absent=float(results1[3])
			avg=float(results1[4])
			od_avg=float(results1[5])
			total_avg=float(results1[6])
			exec("info=%s"%(results1[0]))
			for dd in dod.split(';'):
				if not d+';'+dd in info:
					info[d+';'+dd]=status
					maxx+=1
					if status=='1':
						attended+=1
					elif status=='0':
						absent+=1
					avg=float((attended/maxx)*100)
					total_avg=float(avg+od_avg)
		sql2="UPDATE `%s` SET `info`='%s',`max`='%s',`attended`='%s',`absent`='%s',`avg`='%s',`od_avg`='%s',`total_avg`='%s' WHERE `sub`='%s'"%(username,str(MySQLdb.escape_string(str(info))),str(maxx),str(attended),str(absent),str(avg),str(od_avg),str(total_avg),sub)
		#print sql2
		cursor1.execute(sql2)
		db1.commit()
		db1.close()
		return True
	except Exception as e:
		db1.rollback()
		db1.close()
		return False
	db1.close()
if __name__=="__main__":
	t=verify.verifySession()
	if (str(t[2])[:1]=='1'or str(t[2])[:1]=='2'):
		error.errorMessage("Invalid Login Attempt!","You are already logged in as a student.")
	elif t[0] and str(t[2])[:1]=='3':
		createPortal(t[1])
	else:
		error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
