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
		sql1="SELECT student.regno,student.fname,student.lname,student.type,class.sec,class.year from student,class where student.regno='%s' and student.classid=class.classid"%(username)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchone()
		#print results1
		regno=results1[0]
		fname=results1[1]
		lname=results1[2]
		typee=results1[3]
		sec=results1[4]
		year=results1[5]
		dept_id=str(typee)[1:]
		sql2="SELECT dept_name FROM dept WHERE dept_id='%s'"%(dept_id)
		cursor2=db1.cursor()
		cursor2.execute(sql2)
		results2=cursor2.fetchone()
		branch=results2[0]
		typee=str(typee)[:1]
		if typee=="1":
			typee="BTech"
		else:
			typee="MTech"
		#print dept_id
		db1.commit()
	except Exception as e:
		db1.rollback()
		print e
		print "Invalid session !"

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
		 <link rel="stylesheet" href="/css/student.css">
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
		                                <a class="navbar-brand">Student Portal</a>
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
		                         <li><a id="home" class="tabs" href="/cgi-bin/student.py">Home</a></li>
		                    <li><a class="tabs" id="attendance">Attendance</a></li>
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
		                                         <legend>Student Details</legend>
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
		                                         <label for="course" class="col-lg-2 control-label">Course</label>
                                                      <div class="col-lg-10">
                                                          <input type="text" disabled class="form-control" id="course" placeholder="Course" value="%s">
                                                      </div>
                                                      </div>
                                                       <div class="form-group">
		                                              <label for="inputBranch" class="col-lg-2 control-label">Branch</label>
		                                              <div class="col-lg-10">
		                                                  <input type="text" disabled class="form-control" id="inputBranch" placeholder="Branch" value="%s">
		                                              </div>
		                                              </div>
		                                               <div class="form-group">
		                                               <label for="inputSection" class="col-lg-2 control-label">Section</label>
		                                                <div class="col-lg-10">
		                                                  <input type="text" disabled class="form-control" id="inputSection" placeholder="Section" value="%s">
		                                              </div>
		                                              </div>
		                                               <div class="form-group">
		                                               <label for="inputYear" class="col-lg-2 control-label">Year</label>
		                                                <div class="col-lg-10">
		                                                  <input type="text" disabled class="form-control" id="inputYear" placeholder="Year" value="%s">
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
		<div class="modal hide" style="z-index:99;background-color:white;opacity:0.6;" id="pleaseWaitDialog" data-backdrop="static" data-keyboard="false"><div class="modal-body" >    <h1>Processing... <img src="/images/wait.gif"/ width=100 height=100>  </h1>          </div>    </div>
		<div class="modal hide" style="z-index:99;background-color:white;" id="webcamDialog" data-backdrop="static" data-keyboard="false"><div class="col-lg-6 col-lg-offset-4" style="opacity:1;"><h1>Capture your image . . .</h1>  <div class="modal-body" id="webcam" ></div><div class="row"><select id="cameraNames"></div><div class="row"></select><button class="btn btn-success" id="camcapture" >Capture</button><button class="btn btn-primary" id="camclose" >Cancel</button></div> </div>    </div>
		<input type="file" id="proof"/>
	</body>
	    <!--Scripts at the end-->
	     <script type="text/javascript" src="/js/jQuery/jQuery.js"></script>
	      <script type="text/javascript" src="/bootstrap/js/bootstrap.min.js"></script> 
		 <script type="text/javascript" src="/js/student.js"></script>
		 <script language="JavaScript" src="//ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js"></script>
		<script language="JavaScript" src="/js/scriptcam/scriptcam.js"></script>
		 
	</html>"""%(str(fname+" "+lname),fname,lname,regno,typee,branch,sec,year)
def refreshPortal():
	pass
def refreshOD(username,typee):
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
		sql1="SELECT student.regno,student.fname,student.lname,student.type,class.sec,class.year,class.sem from student,class where student.regno='%s' and class.classid IN(SELECT student.classid from student where student.regno='%s')"%(username,username)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		results1=cursor1.fetchone()
		regno=results1[0]
		fname=results1[1]
		lname=results1[2]
		typee=results1[3]
		sec=results1[4]
		year=results1[5]
		sem=results1[6]
		dept_id=str(typee)[1:]
		sql2="SELECT dept_name FROM dept WHERE dept_id='%s'"%(dept_id)
		cursor2=db1.cursor()
		cursor2.execute(sql2)
		results2=cursor2.fetchone()
		branch=results2[0]
		typee=str(typee)[:1]
		if typee=="1":
			typee="BTech"
		else:
			typee="MTech"
		db1.commit()
		print """  <form class="form-horizontal">
  <fieldset>
    <legend>OD Application Form</legend>
    <div class="form-group">
      <label for="leave" class="col-lg-4 control-label">Leave Category</label>
      <div class="col-lg-8">
        <input type="text" class="form-control" id="leave" value="OD" disabled="" placeholder="Leave Category">
      </div>
    </div>
     <div class="form-group">
      <label for="prog" class="col-lg-4 control-label">Programme</label>
      <div class="col-lg-8">
        <input type="text" class="form-control" id="prog" value="%s" disabled="" placeholder="Programme">
      </div>
    </div>
    <div class="form-group">
      <label for="fname" class="col-lg-4 control-label">First Name</label>
      <div class="col-lg-8">
        <input type="text" class="form-control" value="%s" id="fname" disabled="" placeholder="First Name">
      </div>
    </div>
    <div class="form-group">
      <label for="lname" class="col-lg-4 control-label">Last Name</label>
      <div class="col-lg-8">
        <input type="text" class="form-control" value="%s" id="lname" disabled="" placeholder="Last Name">
       
      </div>
    </div>
     <div class="form-group">
      <label for="classInfo" class="col-lg-4 control-label">Dept/Branch/Section/Semester</label>
      <div class="col-lg-4">
        <input type="text" class="form-control" value="%s/%s/%s/%s" id="classInfo" disabled="" placeholder="Dept/Branch/Section/Semester">
       
      </div>
    </div>
    <div class="form-group">
      <label for="regno" class="col-lg-4 control-label">Registration No.</label>
      <div class="col-lg-8">
        <input type="text" class="col-lg-4 form-control" value="%s" id="regno" disabled="" placeholder="Registration No.">
       
      </div>
    </div>
    <div class="form-group">
      <label for="from"  class="col-lg-4 control-label">Period of Leave</label>
      <div class="col-lg-4">
        <input type="date" class="form-control" id="from">
        <label for="to"  class="control-label">To</label>
         <input type="date" class="form-control" id="to">
       
      </div>
    </div>
    <div class="form-group">
      <label for="days" class="col-lg-4 control-label">No. of Days</label>
      <div class="col-lg-4">
        <input type="text" class="form-control" disabled="" id="days"  placeholder="No. of Days">
       
      </div>
    </div>
    <div class="form-group">
      <label for="reason" class="col-lg-2 control-label">Reason</label>
      <div class="col-lg-10">
        <textarea class="form-control" rows="3" id="reason"></textarea>
        <span class="help-block">Maximum 200 characters allowed.</span>
      </div>
    </div>
    <div class="form-group">
      <label class="col-lg-2 control-label">Proof Enclosed</label>
      <div class="col-lg-10">
        <div class="radio">
          <label>
            <input type="radio" name="proof" id="proofYes" value="yes">
            Yes
          </label>
        </div>
        <div class="radio">
          <label>
            <input type="radio" name="proof" id="proofNo" value="no" checked="">
            No
          </label>
        </div>
      </div>
    </div>
     <div class="form-group">
      <label class="col-lg-2 control-label">Any test during the leave</label>
      <div class="col-lg-10">
        <div class="radio">
          <label>
            <input type="radio" name="test" id="testYes" value="yes">
            Yes
          </label>
        </div>
        <div class="radio">
          <label>
            <input type="radio" name="test" id="testNo" value="no" checked="">
            No
          </label>
        </div>
      </div>
    </div>
    <div class="form-group">
      <div class="col-lg-10 col-lg-offset-2">
        <button class="btn btn-default">Cancel</button>
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
    </div>
  </fieldset>
</form>"""%(typee,fname,lname,typee,branch,sec,sem,username)
	except Exception as e:
		db1.rollback()
		print e
		print "Invalid session !"

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
if __name__=="__main__":
	t=verify.verifySession()
	if t[0] and (str(t[2])[:1]=='1' or str(t[2])[:1]=='2'):
		createPortal(t[1])
	elif str(t[2])[:1]=='3':
		error.errorMessage("Invalid Login Attempt!","You are already logged in as a faculty.")
	else:
		error.errorMessage("Oops ! Something Went Wrong!","Unable to verify your login attempt.")
