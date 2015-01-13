#!/usr/bin/python
# Import modules for CGI handling 
import cgi,MySQLdb,hashlib,sha, time, Cookie, os,math,error
def printIndex():
	print 'Content-Type: text/html\n'
	print"""
	<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>seekho.com</title>
        <link rel="shortcut icon" href="/images/fav.ico"/>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <link rel="stylesheet" href="/css/index.css">
        <link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">
        <script type="text/javascript" src="/js/jQuery/jQuery.js"></script>
      <script type="text/javascript" src="/bootstrap/js/bootstrap.min.js"></script> 
         <script type="text/javascript" src="/js/index.js"></script>
    </head>
    <body>
     <div class="alert alert-danger" id="warning"><strong>Oh Snap !</strong> This website works on JavaScript ! Please enable it !</div>    
   <nav id="nav_top" class="navbar navbar-default" role="navigation">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
        <a class="navbar-brand" href="#" style="padding: 5px !important;"><img src="/images/logo.png" width="80" height="45" alt="Logo image"/></a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="/cgi-bin/index.py">Home<span class="sr-only">(current)</span></a></li>
        <li><a id='subjects'>Subjects</a></li>
      </ul>
       
            <div class="navbar-form navbar-left input-group" role="search" style="width:50&percnt;;">
                <input id="search" type="text" class="form-control" autocomplete="off" style="width:100&percnt;;" placeholder="Examples : nodejs code algebra"/>
            <span class="input-group-addon glyphicon glyphicon-search"></span>
          </div>
        
        
     
      <ul class="nav navbar-nav navbar-right">
          <li> <a href="" data-toggle="modal" data-target="#signup_modal">Sign Up</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-user"></span>&nbsp;user <span class="caret"></span></a>
          <ul class="dropdown-menu" role="menu">
              <li><a href="#"><i>Not logged in yet !</i></a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
 <div id="ajax_area">
  <div class="container" style="margin:0px;" id="dash">
    <div class="row feature">
        <div id='code' class="col-md-3">
            <div>
               <img class="center-block"  src="/images/code.png" width="320" height="150" alt='code'/>
                <span class="glyphdash_text text-center">Code</span>
                <!--a href="#" class="btn btn-success lower">See Feature details</a-->
            </div>
        </div>

        <div id='phy' class="col-md-3">
            <div>
                <img class="center-block"  src="/images/phy.png" width="320" height="150" alt='code'/>
                <span class="glyphdash_text text-center">Physics</span>
                <!--a href="#" class="btn btn-success lower">See Feature details</a-->
            </div>
        </div>

        <div id='chem' class="col-md-3">
            <div>
                <img class="center-block"  src="/images/chem.png" width="180" height="150" alt='code'/>
                <span class="glyphdash_text text-center">Chemistry</span>
               
                <!--a href="#" class="btn btn-success lower">See Feature details</a-->
            </div>
        </div>
        <div id='math' class="col-md-3">
            <div>
                <img class="center-block"  src="/images/math.png" width="320" height="150" alt='code'/>
                <span class="glyphdash_text text-center">Mathematics</span>
               
                <!--a href="#" class="btn btn-success lower">See Feature details</a-->
            </div>
        </div>
    </div>
</div>
      
        <!--main body-->
        <div id="main_body" class="row">
            <a href="#here"></a>
            <div class="well-lg" id="banner">
                <div class="container" style="padding-top: 20px !important; ;width:100&percnt;;height:100&percnt;;">
                    <div class="row" style="height:100&percnt;;background-color:rgba(0,0,0,0.2);">
                        <div class="col-lg-8 col-md-8 col-sm-12 col-xs-12" style="border-right-style:solid;border-radius: 2px;border-right-width:thick;border-right-color:whitesmoke;height:100&percnt;;">
                            <!--img class="center-block"  src="/images/logo.png" width="420" height="260" alt='code'/-->
                            <span class="glyphdash_text">Our mission is to provide a free, world class education for anyone, anywhere.</span>
                        </div>
                        <div class="col-lg-4 col-md-4 col-sm-4 hidden-xs" style="height:100&percnt;;">
                            <div  style="height:100&percnt;;width:100&percnt;;">
                                <div class="container" style="height:100&percnt;;width:100&percnt;;">
                                    <div class="row" style="padding-top:40px;height:25&percnt;;width:100&percnt;;">
                                        <div class="text-center" style="font-size: 30px;color:white;font:calibri;" >
                                            Login for free courses
                                        </div>
                                        
                                    </div>
                                    
                                    <div class="row" style="height:80&percnt;;width:100&percnt;;">
                                        <div class="center-block" style="height: 80&percnt;;width: 100&percnt;;">
                                            <form id="login_frm" method="POST" action="/cgi-bin/auth.py">
                                            <div>
                                                <label class="label label-primary">Username</label> <input id="uname" name="username" class="form-control" type="text" placeholder="Username"/>
                                            </div>
                                            <div>
                                                <label class="label label-primary">Password</label> <input id="pswd" name="pswd" class="form-control" type="password" placeholder="Password"/>
                                            </div>
                                            <div class="text-center checkbox" style='padding-top: 10px;color:white;'>
                                                <label>
                                                    <input name="chk" type="checkbox"/>Keep me logged in.
                                                </label>
                                            </div>
                                            <div class="text-center" style='padding-top: 10px;'>
                                                <a style="color:white;" href="#">Do't have a account sign up now !</a>
                                            </div>
                                            <div class="text-center" style='padding-top: 10px;'>
                                                <a style="color:white;" href="#">Trouble logging in ?</a>
                                            </div>
                                             <div class="text-center form-group-lg" style='padding-top: 10px;'>
                                                 <input type="submit" style='width: 60&percnt;;' class="btn btn-success" value="Login"/>
                                            </div>
                                             <div class="text-center form-group-lg" style='padding-top: 10px;'>
                                                 <input type="reset" style='width: 60&percnt;;' class="btn btn-danger" value="Cancel"/>
                                            </div>
                                           </form>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Feature List - START -->
<div class="container" id="cnt1">
    <div class="row feature">
        <div class="col-md-4">
            <div>
               <span class="glyphicon glyphicon-list-alt"></span>
                <h2>Join Courses</h2>
                <!--a href="#" class="btn btn-success lower">See Feature details</a-->
            </div>
        </div>

        <div class="col-md-4">
            <div>
                <span class="glyphicon glyphicon-check"></span>
                <h2>Create Courses</h2>
                <!--a href="#" class="btn btn-success lower">See Feature details</a-->
            </div>
        </div>

        <div class="col-md-4">
            <div>
                <span class="text-center glyphicon glyphicon-share-alt"></span>
                <h2>Share Courses</h2>
               
                <!--a href="#" class="btn btn-success lower">See Feature details</a-->
            </div>
        </div>
    </div>
</div>
                
            </div>
       
        <!--bottom navbar-->
        <nav id="nav_btm" class="navbar">
            <div class="container" style="padding-top: 10px !important;">
                <div class="row">
                    <div class="col-lg-4 col-md-12 col-xs-12 col-sm-12">
                        <ul class="list-group">
                            <li class="list-group-item">About</li>
                            <li class="list-group-item"><a href="/about">Our Mission</a></li>
                            <li class="list-group-item"><a href="/about/the-team">Our Team</a></li>
                            <li class="list-group-item"><a href="/about/our-board">Our Board</a></li>
                        </ul>
                    </div>
                    <div class="col-lg-4 col-md-12 col-xs-12 col-sm-12">
                            <ul class="list-group">
                                <li class="list-group-item">Support</li>
                                <li class="list-group-item"><a href="/help">Help center</a></li>
                                <li class="list-group-item"><a href="#"  data-toggle="modal" data-target="#contact_modal">Contact</a></li>
                                <li class="list-group-item"><a href="/press">Press</a></li>
                             </ul>
                    </div>
                    <div class="col-lg-4 col-md-12 col-xs-12 col-sm-12">
                            <ul class="list-group">
                                <li class="list-group-item">Careers</li>
                                <li class="list-group-item"><a href="/careers">Full Time</a></li>
                                <li class="list-group-item"><a href="/careers/interns">Internships</a></li>
                                <li class="list-group-item"><a href="/contribute">Volunteer</a></li>
                            </ul>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-12">
                        <div class="center-block" style="width: 160px;">
                            <img alt="Seekho logo" width="160" height="90" src="/images/logo.png">
                            <hr>
                            <div class="text-center" style="width: 160px;">
                                &copy; 2014 Seekho.com <br/> All rights reserved.
                            </div>
                            
                        
                   
                    
                     
                    
            
                </div>
            </div>
               
        </nav>
<div id="signup_modal" class="modal fade">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title">Sign Up</h4>
      </div>
      <div class="modal-body">
          <form id="signup" class="form-horizontal" method="POST" action="/cgi-bin/register.py">
  <fieldset>
    <div class="form-group">
      <label for="inputEmail" class="col-lg-2 control-label">Email</label>
      <div class="col-lg-10">
          <input type="text" name="email" class="form-control" id="inputEmail" placeholder="Email"/>
      </div>
    </div>
    <div class="form-group">
      <label for="inputPassword" class="col-lg-2 control-label">Password</label>
      <div class="col-lg-10">
        <input type="password"  class="form-control" id="inputPassword" placeholder="Password"/>
      </div>
    </div>
      <div class="form-group">
      <label for="rePassword" class="col-lg-2 control-label">Confirm Password</label>
      <div class="col-lg-10">
        <input type="password" name="pswd" class="form-control" id="rePassword" placeholder="Confirm Password"/>
      </div>
    </div>
    <div class="form-group">
      <label for="inputUserName" class="col-lg-2 control-label">User Name</label>
      <div class="col-lg-10">
        <input type="text" name="username" class="form-control" id="inputUserName" placeholder="User Name"/>
      </div>
    </div>
      <div class="form-group">
      <label for="inputfname" class="col-lg-2 control-label">First Name</label>
      <div class="col-lg-10">
        <input type="text" name="fname" class="form-control" id="inputfname" placeholder="First Name"/>
      </div>
    </div>
      <div class="form-group">
      <label for="inputlname" class="col-lg-2 control-label">Last Name</label>
      <div class="col-lg-10">
        <input type="text" name="lname" class="form-control" id="inputlname" placeholder="Last Name"/>
      </div>
    </div>
      <div class="form-group">
      <label for="inputdob" class="col-lg-2 control-label">Date of Birth</label>
      <div class="col-lg-10">
        <input type="date" name="dob"  class="form-control" id="inputdob"/>
      </div>
    </div>
      <div class="form-group">
      <label for="inputcollege" class="col-lg-2 control-label">College</label>
      <div class="col-lg-10">
        <input type="text" name="college" class="form-control" id="inputcollege" placeholder="College/University"/>
      </div>
    </div>
    <div class="form-group">
      <label class="col-lg-2 control-label">Sex</label>
      <div class="col-lg-10">
        <div class="radio">
          <label>
            <input type="radio" name="sex" id="optionsRadios1" value="male" checked=""/>
            Male
          </label>
        </div>
        <div class="radio">
          <label>
            <input type="radio" name="sex" id="optionsRadios2" value="female"/>
            Female
          </label>
        </div>
      </div>
    </div>
      <div class="checkbox-inline">
          <label>
              <input id="accept" type ="checkbox"/><span>By submiting this form,I accept the license and terms.</span>
          </label>
      </div>
    <div class="form-group">
      <div class="col-lg-10 col-lg-offset-2">
        <button class="btn btn-default" data-dismiss="modal">Cancel</button>
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
    </div>
  </fieldset>
</form>
      </div>
      
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->

<div id="contact_modal" class="modal fade">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title">Contact Us </h4>
      </div>
      <div class="modal-body">
         <div class="well well-sm">
                <form class="form-horizontal" method="post">
                    <fieldset>

                        <div class="form-group">
                            <div class="col-md-12">
                                <input id="fname" name="name" type="text" placeholder="First Name" class="form-control">
                            </div>
                        </div>
                        <div class="form-group">
                            <div class="col-md-12">
                                <input id="lname" name="name" type="text" placeholder="Last Name" class="form-control">
                            </div>
                        </div>

                        <div class="form-group">
                           <div class="col-md-12">
                                <input id="email" name="email" type="text" placeholder="Email Address" class="form-control">
                            </div>
                        </div>

                        <div class="form-group">
                            <div class="col-md-12">
                                <input id="phone" name="phone" type="text" placeholder="Phone" class="form-control">
                            </div>
                        </div>

                        <div class="form-group">
                            <div class="col-md-12">
                                <textarea class="form-control" id="message" name="message" placeholder="Enter your massage for us here. We will get back to you within 2 business days." rows="7"></textarea>
                            </div>
                        </div>

                        <div class="form-group">
                            <div class="col-md-12 text-center">
                                <button type="submit" class="btn btn-primary btn-lg">Submit</button>
                            </div>
                        </div>
                    </fieldset>
                </form>
            </div>
      </div>
      
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->
</div>
</body>
    <!--Scripts at the end-->
     
         
</html>

	"""
def verifySession(sid):
	try:
		# Open database connection
		db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
		# prepare a cursor object using cursor() method
		cursor1 = db1.cursor()
		# execute SQL query using execute() method.
		sql1="SELECT username from session where sid='%s'"%(sid)
		#print sql1
		# Execute the SQL command
		cursor1.execute(sql1)
		username=""
		results1=cursor1.fetchone()
		username=results1[0]
		db1.commit()
	except:
		db1.rollback()
		error.errorMessage("Problem in session creation","Invalid username and password combination or try clearing your cookie data.")

	db1.close()
	return username

#Loading sid from cookie
cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
if string_cookie is None:
	printIndex()
else:
	cookie.load(string_cookie)
	sid = cookie['sid'].value
	temp=verifySession(sid)
	username=str(temp)
	if username !="":
		print 'Content-Type: text/html\n'
		print  "<SCRIPT type='text/javascript'>window.location.href='/cgi-bin/user.py';</SCRIPT>"
	else:
		#clear all cookie data see to it
		error.errorMessage("Problem in session creation","Invalid username and password combination or try clearing your cookie data.")
	
