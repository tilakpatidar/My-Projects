#!/usr/bin/python
# Import modules for CGI handling 
import cgi,verify,error,MySQLdb#, cgitb
def genratePage(data):
	fname, lname, email,dob,sex,username,college=data
	name=fname+" "+lname
	print 'Content-Type: text/html\n'
	print """ <!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>Seekho.com</title>
        <link rel="shortcut icon" href="/images/fav.ico">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <link rel="stylesheet" href="/css/index.css">
         <link rel="stylesheet" href="/css/user.css">
        <link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">
        <script type="text/javascript" src="/js/jQuery/jQuery.js"></script>
      <script type="text/javascript" src="/bootstrap/js/bootstrap.min.js"></script> 
         <script type="text/javascript" src="/js/index.js"></script>
         <script type="text/javascript" src="/js/user.js"></script>
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
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-user"></span>&nbsp;%s <span class="caret"></span></a>
          <ul class="dropdown-menu" role="menu">
            <li><a href="#">Account Settings</a></li>
            <li class="divider"></li>
            <li><a href="/cgi-bin/logout.py">Log Out</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
        <div id="ajax_area" style="background-color: #28b62c;">
        <div class="container" style="margin:0px;" id="dash">
    <div class="row feature">
        <div id='code' class="col-md-3">
            <div>
               <img class="center-block"  src="/images/code.png" width="320" height="150" alt='code'/>
                <span class="glyphdash_text text-center">Code</span>
                
            </div>
        </div>

        <div id='phy' class="col-md-3">
            <div>
                <img class="center-block"  src="/images/phy.png" width="320" height="150" alt='code'/>
                <span class="glyphdash_text text-center">Physics</span>
                
            </div>
        </div>

        <div id='chem' class="col-md-3">
            <div>
                <img class="center-block"  src="/images/chem.png" width="180" height="150" alt='code'/>
                <span class="glyphdash_text text-center">Chemistry</span>
               
                
            </div>
        </div>
        <div id='math' class="col-md-3">
            <div>
                <img class="center-block"  src="/images/math.png" width="320" height="150" alt='code'/>
                <span class="glyphdash_text text-center">Mathematics</span>
               
                
            </div>
        </div>
    </div>
</div>
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="jumbotron" style="background-color: rgba(0,0,0,0.1);">
                        <div class="row">
                            <div class="col-lg-9" style="color: white;">
                                <h1>%s</h1>
                            </div>
                            <div class="col-xs-6 col-md-3">
                                <a href="#" class="thumbnail">
                                    <img data-src="holder.js/100&percnt;x180" alt="...">
                                  </a>
                            </div>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
        </div>
        <div class="container">
    <div class="row" >
        <div class="col-sm-3 col-md-3">
            <div class="panel-group" id="accordion" >
                <div class="panel panel-default" >
                    <div class="panel-heading">
                        <h4 class="panel-title">
                            <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne"><span class="glyphicon glyphicon-user"></span> Profile</a>
                        </h4>
                    </div>
                    <div id="collapseOne" class="panel-collapse collapse " >
                        <ul class="list-group" >
                            <li class="list-group-item"><span class="glyphicon glyphicon-pencil text-primary"></span> <a id="show_profile">Show Profile</a>
                                <!--ul class="list-group">
                                    <li class="list-group-item"><span class="glyphicon glyphicon-minus text-primary"></span> <a>Edit Blog</a></li>
                                    <li class="list-group-item"><span class="glyphicon glyphicon-minus text-success"></span> <a>Publish Blog</a></li>
                                    <li class="list-group-item"><span class="glyphicon glyphicon-minus text-warning"></span> <a>Delete Blog</a></li>
                                </ul-->
                            
                        </ul>
                    </div>
                    
                </div>
            </div>
             <div class="panel-group" id="accordion2" >
                <div class="panel panel-default" >
                    <div class="panel-heading">
                        <h4 class="panel-title">
                            <a data-toggle="collapse" data-parent="#accordion" href="#collapseThree"><span class="glyphicon glyphicon-tasks"></span> Courses</a>
                        </h4>
                    </div>
                    <div id="collapseThree" class="panel-collapse collapse" >
                        <ul class="list-group" >
                            <li class="list-group-item"><span class="glyphicon glyphicon-pencil text-primary"></span> Manage Courses
                                <ul class="list-group">
                                <li class="list-group-item"><span class="glyphicon glyphicon-minus text-primary"></span> <a id="join_course">Joined Courses</a></li>
                                    <li class="list-group-item"><span class="glyphicon glyphicon-minus text-primary"></span> <a>Edit Course(Under Construction)</a></li>
                                    <li class="list-group-item"><span class="glyphicon glyphicon-minus text-success"></span> <a id="create_course">Publish Course</a></li>
                                    <li class="list-group-item"><span class="glyphicon glyphicon-minus text-warning"></span> <a>Delete Course(Under Construction)</a></li>
                                </ul>
                            </li>
                          
                        </ul>
                    </div>
                    
                </div>
            </div>
             <div class="panel-group" id="accordion1" >
                <div class="panel panel-default" >
                    <div class="panel-heading">
                        <h4 class="panel-title">
                            <a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo"><span class="glyphicon glyphicon-hdd"></span> Files</a>
                        </h4>
                    </div>
                    <div id="collapseTwo" class="panel-collapse collapse" >
                        <ul class="list-group" >
                            <li class="list-group-item"><span class="glyphicon glyphicon-pencil text-primary"></span> <a>Blogs</a>
                                <ul class="list-group">
                                    <li class="list-group-item"><span class="glyphicon glyphicon-minus text-primary"></span> <a>Under Construction</a></li>
                                    <li class="list-group-item"><span class="glyphicon glyphicon-minus text-success"></span> <a>Under Construction</a></li>
                                    <li class="list-group-item"><span class="glyphicon glyphicon-minus text-warning"></span> <a>Under Construction</a></li>
                                </ul>
                            </li>
                             
                        </ul>
                    </div>
                    
                </div>
            </div>
            
        </div>
       
        <div class="col-sm-9 col-md-9 col-lg-9">
            <div class="panel panel-default">
                <div class="panel-body" id="user_body"                    
                    <div class="container">
    <div class="row">
        <div class="col-lg-6">
            
                        <h2 style="text-decoration:underline;">%s</h2>
                        <p><strong>Username: </strong>%s </p>
                        <p><strong>Email address: </strong>%s </p>
                        <p><strong>Date of Birth: </strong>%s</p>
                        <p><strong>Sex: </strong>%s </p>
                        <p><strong>College: </strong>%s </p>
                                   
           
        
    </div>
</div>
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
</div>

<!-- /.add course modal -->
<div id="content_modal" class="modal fade" >
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title">Choose Content Type</h4>
      </div>
      <div class="modal-body">
        <div class="container" style="margin:0px;width:100&percnt;;">
    <div class="row feature">
        <div id='text' class="col-md-4">
            <div>
               <span class="glyphicon glyphicon-pencil glyph_course_text"></span>
                <span class="course_text text-center">Text</span>
                
            </div>
        </div>

        <div id='file' class="col-md-4">
            <div>
                <span class="glyphicon glyphicon-file glyph_course_text"></span>
                <span class="course_text text-center">Document File</span>
                
            </div>
        </div>

        <div id='video' class="col-md-4">
            <div>
                <span class="glyphicon glyphicon-film glyph_course_text"></span>
                <span class="course_text text-center">Video</span>
               
                
            </div>
        </div>
        
    </div>
</div>
      </div>
     
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


<!-- /.Text modal -->
<div class="modal fade" id="text_modal">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title">Text material for the course</h4>
      </div>
      <div class="modal-body">
        <div class="container" style="width:100&percnt;;">
        <div class="row">
        <div class="col-lg-12">
        <input type="text" id="text_title" style="width:100&percnt;;" placeholder="Title"/>
        <input type="text" id="text_description" style="width:100&percnt;;" placeholder="Description"/>
        <textarea id="text_save" style="width:100&percnt;;height:300px;" placeholder="HTML formatting is allowed." col=12 row=36></textarea>
        </div>
        </div>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button type="button" id="text_save_btn" class="btn btn-primary">Save changes</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->




<!-- /.Video modal -->
<div class="modal fade" id="video_modal">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title">Video material for the course</h4>
      </div>
      <div class="modal-body">
        <div class="container" style="width:100&percnt;;">
        <div class="row">
        <div class="col-lg-12">
        <textarea id="video_save" style="width:100&percnt;;" placeholder="Enter youtube video url" col=12 row=36></textarea>
        </div>
        </div>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button type="button" id="video_save_btn" class="btn btn-primary">Save changes</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


<!-- /.File modal -->
<div class="modal fade" id="file_modal">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title">Text material for the course</h4>
      </div>
      <div class="modal-body">
        <div class="container" style="width:100&percnt;;">
        <div class="row">
        <div class="col-lg-12">
        <input type="text" id="file_title" style="width:100&percnt;;" placeholder="Title"/>
        <input type="text" id="file_description" style="width:100&percnt;;" placeholder="Description"/>
        <textarea id="file_save" style="width:100&percnt;;height:300px;" placeholder="Enter your google doc embed code." col=12 row=36></textarea>
        </div>
        </div>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button type="button" id="file_save_btn" class="btn btn-primary">Save changes</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


</div>
    </body>
     <!--Scripts at the end-->
     
</html>"""%(name,name,name,username,email,dob,sex,college)

res=verify.verifySession()
if res[0]:
	def getData(username):
		results=""
		try:
			db1 = MySQLdb.connect("fdb13.runhosting.com","1780205_seekho","tilak05051995","1780205_seekho" )
			cursor1 = db1.cursor()
			sql1="SELECT fname, lname, email,dob,sex,username,college FROM info where username='%s'"%(str(username))
			
			cursor1.execute(sql1)
			results=cursor1.fetchone()
			db1.commit()
		except Exception as e:
			db1.rollback()
			print 'Content-Type: text/html\n'
			error.errorMessage('Invalid Login Attempt!','Try clearing your cookie data.')
			return ""
		db1.close()
		return results
	
	if str(res[1])!="":
		data=getData(res[1])
		genratePage(data)
	else:
		print 'Content-Type: text/html\n'
		error.errorMessage('Invalid Login Attempt!','Try clearing your cookie data.')
else:
	print 'Content-Type: text/html\n'
	error.errorMessage('Invalid Login Attempt!','Try clearing your cookie data.')

