#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,hashlib,os
cgitb.enable()
# Create instance of FieldStorage 
form = cgi.FieldStorage()
def recordResponse(name,email,subject,message):
	foo=open('feedback.txt')
	foo.write("##name##"+name+"##email##"+email+"##subject##"+subject+"##message##"+message+"##newline##")
#get data from html form
try:
	name=str(form.getvalue('name'))
	email=str(form.getvalue('email'))
	subject=str(form.getvalue('subject'))
	message=str(form.getvalue('message'))
	recordResponse(name,email,subject,message)
	print """
	<!DOCTYPE html>
	<!--
	To change this license header, choose License Headers in Project Properties.
	To change this template file, choose Tools | Templates
	and open the template in the editor.
	-->
	<html>
	    <head>
		<title>TODO supply a title</title>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script type="text/javascript" src="/jQuery/jQuery.js"></script>
		 <script type="text/javascript" src="/modernizr/modernizr.custom.21219.js"></script>
		 <link rel="stylesheet" href="/css/index.css">
		 <link rel="stylesheet" href="/bootstrap/css/bootstrap.css">
		<link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">
		
		 <script type="text/javascript" src="/bootstrap/js/bootstrap.js"></script> 
		 <script type="text/javascript" src="/bootstrap/js/bootstrap.min.js"></script> 
		 <script type="text/javascript" src="/bootstrap/js/bootswatch.js"></script> 
		 
		 
		 
		 <script type="text/javascript" src="/js/index.js"></script>
		 <link rel='stylesheet' href='css/style.css'>
		 <link href="/css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
	       <script type="text/javascript" >
		   
		$(document).ready(function(){
		 $("#warning1").attr("class","alert alert-success");
	 	document.getElementById("warning1").innerHTML="Response recorded successfully !";
		$("#warning1").show().hide(10000);
			
			$("#warning").hide();
			
		        $('.popover-dismiss').popover({
	  trigger: 'focus'
	})
		});    		
		

	</script> 
	    </head>
	    <body>
	<div class="alert alert-danger" id="warning1"><strong>Oh Snap !</strong> This website works on JavaScript ! Please enable it !</div>
		<div class="modal fade" id="myModal">
		<div class="modal-dialog">
		  <div class="modal-content">
		    <div class="modal-header">
		      <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
		      <h4 class="modal-title">Log In to gain access</h4>
		    </div>
		    <div class="modal-body">
		        <input type="text" class="form-control" placeholder="Email Address"/>
		    </div>
		    <div class="modal-footer">
		      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
		      <button type="button" class="btn btn-success">Login</button>
		    </div>
		  </div><!-- /.modal-content -->
		</div><!-- /.modal-dialog -->
	      </div><!-- /.modal -->
	<div class="page">
		<div id="myGallery">
		    <img src="/images/1.jpg" class="active" alt="" />
		    <img src="/images/2.jpg" alt="" />
		     <img src="/images/3.jpg" alt="" />
		    <img src="/images/4.jpg" alt="" />
		    <img src="/images/5.jpg" alt="" />
		</div>
	    <div  style="height: 30&percnt;;width: 100&percnt;; "> 
		<div style="width: 100&percnt;;height: 100&percnt;; margin-left: auto;margin-right: auto;" >
		    <div id="left_circle" style='width: 30&percnt;;height: 50&percnt;;float:left;'>
		        <a id="lcircle" class="" href="#">
		        <div id='left_circle_back'>
		        
		                <div id="abt_us">



		                </div>
		                
		        </div>
		             </a>
		    </div>
		    <div id="big_circle" style='width: 40&percnt;;float:left;'>
		        <a id="bcircle" href="#">
		         <div id='big_circle_back'>
		         
		        <div id="logo"></div>
		        
		         </div>
		             </a>
		    </div>
		     <div id="right_circle" style='width: 30&percnt;;height: 50&percnt;;float:right;'>
		          <a id="rcircle"  href="#">
		        <div id='right_circle_back'>
		       
		                <div id="team">



		                </div>
		                
		        </div>
		               </a>
		    </div>
		</div>
	    </div>
	    <div style="height: 73&percnt;;">
	    </div >
	    <div>
		<div style="width: 85&percnt;; position: absolute;bottom: 18px;" >
		    <label class="label "> Copyright &COPY; 2014 SRM SE. All rights reserved. </label>
		</div>
	    <div style="width: 12&percnt;;height: 24&percnt;;position: absolute; right: 0px; bottom: 18px;background-image: url('images/srm-logo.png');background-repeat: no-repeat;background-size: contain,contain;">
		    
		</div>
	    </div>
	   
	</div>
	    
	      <div class="page">
		  
	   

	    <div class="section" id="about"><h1>ABOUT</h1><hr></div>

	    <div class="container">
	      <div class="row">
		<div class="col-md-4">
		  <div class="well">
		    <a href="/images/team.jpg" target="_blank"><img src="/images/team.jpg" style="height:100&percnt;; width:100&percnt;" alt="Srm-search engine team"></a>
		  </div>
		</div>
		<div class="col-md-8">
		  <div class="well">
		    <h3><u>What SRM Search Engine is....</u></h3>
		    <p>SRM-Search Engine is an initiative of SRM University, which aims to build a search engine for educational purposes and provide better searches and apt results for the queries of its users. The project started on September 1, 2012. The project got funded by the National Internet Exchange of India, Department of Electronics and Information Technology, on September 8, 2013. SRM university provides all the necessary help to establish the laboratory and to design and develop the Search Engine.</p>
		    <p><a id="contact_us" href="" class="btn btn-default">Contact Us</a></p>
		  </div>
		</div>
	      </div><!--/.row-->
	    </div><!--/.container-->

	    
	 
	 
	    
	    
	      </div>
	<div class="page">
	      <div class="section" id="what-i-do">
	     <h1>How search works</h1><hr></div>
	 
	  <div class="container">
	      <div class="row">
		<div class="col-md-6">
		  <div class="well">
		    <h3>INFRASTRUCTURE</h3>
		    <p align="justify">The project is sustained by a 20MBPS leased line which is protected by a 100D fortigate fire wall. A node from the high performance computing cluster of SRM University has also been allotted. The main server boasts 64 GB of RAM, 6TB of storage and a 32 core Xeon processor. Also, the lab is equipped with 15 workstations comprising 4th generation i5 processors. The whole network adds up to a pooled storage of 13.5TB and 92 cores of processing power. the same can be virtualized to 550 cores using open stack. The lab is also well equipped with the necessary network peripherals such as switch, router, etc.</p>
	<!--/.col-6-->
		    </div>
		  </div>
		
		<div class="col-md-6">
		  <div class="well">
		    <h3>DEVELOPMENT</h3>
		    <p>The main crawler, which is pretty much the heart of the project has already reached a capacity of being able to crawl 1 crore webpages in about 50 hours. the crawling amounts to an approximate data of 500 GB in the speculated time(50 hours). The same data is reduced by the use of distributed computing/hadoop to index the data frequently(every 50 hours). The other key part has been the development of the knowledge data set for different domains such as Government, Sports, Automobiles, Finance, Wealth, Education, etc. The collected domains are again divided into four categories:-<br />
				<ul>
				<li>Static</li>
				<li>Static with Location</li>
				<li>Dynamic</li>
				<li>Dynamic with Location</li>
				</ul>

		  </div>
		</div>
	      </div><!--/.row-->
	    </div><!--/.container-->

	  </div>
	      <div class="page">
		  <div class="section" id="what-i-do"><h1>The Team</h1><hr></div>

	   
	    <div class="work visible-lg" style="height:250px !important;">
		<div class="container" style="padding-top: 2&percnt;;">
		<div class="row">
	
		  <div class="col-md-3">
		      <a href="#" style="text-decoration: none;"><h3><i class="glyphicon glyphicon-user"></i>&nbsp;Hardware and Networks</h3></a>
		    
		  </div>
		  <div class="col-md-3">
		   <a href="#" style="text-decoration: none;"> <h3><i class="glyphicon glyphicon-user"></i>&nbsp;User Experience</h3></a>
		    
		  </div>
		  <div class="col-md-3">
		   <a href="#" style="text-decoration: none;"> <h3><i class="glyphicon glyphicon-user"></i>&nbsp;Information Systems</h3></a>
		   
		  </div>
		  <div class="col-md-3">
		   <a href="#" style="text-decoration: none;"> <h3><i class="glyphicon glyphicon-user"></i>&nbsp;Knowledge Database </h3></a>
		   
		  </div>
		
		
		
		</div><!--/.row-->
		<div class="row">
		      <div class="col-md-12">
		              <a href="#"  style="text-decoration: none;"> <h3><i class="glyphicon glyphicon-user"></i>&nbsp;Indexing and Query Handling</h3></a>
		    
		  </div>
		</div>
	      </div><!--/.container-->
	    </div><!--/.work-->
	    <br/>
	    <br/>
	    <div style="margin-left: auto;margin-right: auto; width: 15&percnt;;">
		<button type="button" class="btn btn-lg btn-default popover-dismiss" data-toggle="popover" title="" data-content="Under Construction !">See all our members</button>
	    </div>
	      </div>
	  <div class="page">
	      <div class="section" id="work"><h1>RECENT WORK</h1><hr></div>

	    <div class="container">
	      <div class="row">
		<div class="col-md-6">
		  <div class="well">
		    
	     
		    
		    <div class="spacer"></div><div class="spacer"></div>
		  </div>
		</div>
		<div class="col-md-6">
		  <div class="well">
		    
		    <h3></h3>
		    <p></p>
		    <div class="spacer"></div>
		    <div class="spacer"></div>
		  </div>
		</div>
	      </div><!--/.row-->
	    </div><!--/.container-->

	  </div>
	      <div class="page" id="lpage">
	      <!--<div class="hidden-xs"><div class="work-together" id="contact">LETS WORK TOGETHER</div></div>-->
	    <div class="section" id="contact"><h1>CONTACT US</h1><hr></div>
	<div class="alert alert-danger" id="warning"><strong>Oh Snap !</strong> This website works on JavaScript ! Please enable it !</div>
	    <div class="work-together">
	      <div class="container">
		<div class="row">
		  <div class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
		    <h3>Send us a message</h3>
		    <div class="spacer"></div>
		    <form class="form-horizontal" role="form" id="form" action="/cgi-bin/response.py" method="post">
		      <div class="form-group">
		        <label for="name" class="col-sm-2 control-label">Name</label>
		        <div class="col-sm-10">
		          <input type="text" class="contact form-control" name="name" id="name" placeholder="Name">
		        </div>
		      </div>
		      <div class="form-group">
		        <label for="email" class="col-sm-2 control-label">Email</label>
		        <div class="col-sm-10">
		          <input type="email" class="contact form-control" name="email" id="email" placeholder="Email">
		        </div>
		      </div>
		      <div class="form-group">
		        <label for="subject" class="col-sm-2 control-label">Subject</label>
		        <div class="col-sm-10">
		          <input type="text" class="contact form-control" name="subject" id="subject" placeholder="Subject">
		        </div>
		      </div>
		      <div class="form-group">
		        <label for="message" class="col-sm-2 control-label">Message</label>
		        <div class="col-sm-10">
		          <textarea class="contact form-control" rows="3" name="message" id="message" placeholder="Message"></textarea>
		        </div>
		      </div>
		      <div class="form-group">
		        <div class="col-sm-offset-2 col-sm-10">
		          <input type="submit" value="Send" class="btn btn-default" name="submit">
		        </div>
		      </div>
		    </form>
		  </div><!--/.col-->
		  <div class="col-lg-4 col-md-4 hidden-sm hidden-xs">
		    <h3>Contact Details</h3><div class="spacer"></div>
		    <p class="lead" style="margin-bottom:0px;"><i class="fa fa-map-marker"></i>&nbsp; Room No. 29, 4th Floor,University Block,SRM University</p><p class="lead" style="text-indent:24px">Chennai-603203 Tamil nadu</p>
		    <p class="lead"><i class="fa fa-phone"></i>&nbsp;0xxxxx-xxxxx </p>
		    <p class="lead"><i class="fa fa-envelope"></i>&nbsp; www.xyz@abc.com</p>
		  </div>
		</div><!--/.row-->
	      </div><!--/.container-->
	      <div class="container hidden-sm hidden-xs"><div class="spacer"></div><div class="spacer"></div><footer><p class="pull-right">&copySRM-SE</p></footer></div>
	    </div><!--/.work-together-->
	 
	  </div>
	      
	   
	    </body>
	</html>
	"""
except:
	print """
<!DOCTYPE html>
	<!--
	To change this license header, choose License Headers in Project Properties.
	To change this template file, choose Tools | Templates
	and open the template in the editor.
	-->
	<html>
	    <head>
		<title>TODO supply a title</title>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script type="text/javascript" src="/jQuery/jQuery.js"></script>
		 <script type="text/javascript" src="/modernizr/modernizr.custom.21219.js"></script>
		 <link rel="stylesheet" href="/css/index.css">
		 <link rel="stylesheet" href="/bootstrap/css/bootstrap.css">
		<link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">
		
		 <script type="text/javascript" src="/bootstrap/js/bootstrap.js"></script> 
		 <script type="text/javascript" src="/bootstrap/js/bootstrap.min.js"></script> 
		 <script type="text/javascript" src="/bootstrap/js/bootswatch.js"></script> 
		 
		 
		 
		 <script type="text/javascript" src="/js/index.js"></script>
		 <link rel='stylesheet' href='css/style.css'>
		 <link href="/css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
	       <script type="text/javascript" >
		   
		$(document).ready(function(){
		 $("#warning1").attr("class","alert alert-danger");
	 	document.getElementById("warning1").innerHTML="Something went wrong !";
		$("#warning1").show().hide(10000);
			
			$("#warning").hide();
			
		        $('.popover-dismiss').popover({
	  trigger: 'focus'
	})
		});    		
		

	</script> 
	    </head>
	    <body>
	<div class="alert alert-danger" id="warning1"><strong>Oh Snap !</strong> This website works on JavaScript ! Please enable it !</div>
		<div class="modal fade" id="myModal">
		<div class="modal-dialog">
		  <div class="modal-content">
		    <div class="modal-header">
		      <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
		      <h4 class="modal-title">Log In to gain access</h4>
		    </div>
		    <div class="modal-body">
		        <input type="text" class="form-control" placeholder="Email Address"/>
		    </div>
		    <div class="modal-footer">
		      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
		      <button type="button" class="btn btn-success">Login</button>
		    </div>
		  </div><!-- /.modal-content -->
		</div><!-- /.modal-dialog -->
	      </div><!-- /.modal -->
	<div class="page">
		<div id="myGallery">
		    <img src="/images/1.jpg" class="active" alt="" />
		    <img src="/images/2.jpg" alt="" />
		     <img src="/images/3.jpg" alt="" />
		    <img src="/images/4.jpg" alt="" />
		    <img src="/images/5.jpg" alt="" />
		</div>
	    <div  style="height: 30&percnt;;width: 100&percnt;; "> 
		<div style="width: 100&percnt;;height: 100&percnt;; margin-left: auto;margin-right: auto;" >
		    <div id="left_circle" style='width: 30&percnt;;height: 50&percnt;;float:left;'>
		        <a id="lcircle" class="" href="#">
		        <div id='left_circle_back'>
		        
		                <div id="abt_us">



		                </div>
		                
		        </div>
		             </a>
		    </div>
		    <div id="big_circle" style='width: 40&percnt;;float:left;'>
		        <a id="bcircle" href="#">
		         <div id='big_circle_back'>
		         
		        <div id="logo"></div>
		        
		         </div>
		             </a>
		    </div>
		     <div id="right_circle" style='width: 30&percnt;;height: 50&percnt;;float:right;'>
		          <a id="rcircle"  href="#">
		        <div id='right_circle_back'>
		       
		                <div id="team">



		                </div>
		                
		        </div>
		               </a>
		    </div>
		</div>
	    </div>
	    <div style="height: 73&percnt;;">
	    </div >
	    <div>
		<div style="width: 85&percnt;; position: absolute;bottom: 18px;" >
		    <label class="label "> Copyright &COPY; 2014 SRM SE. All rights reserved. </label>
		</div>
	    <div style="width: 12&percnt;;height: 24&percnt;;position: absolute; right: 0px; bottom: 18px;background-image: url('images/srm-logo.png');background-repeat: no-repeat;background-size: contain,contain;">
		    
		</div>
	    </div>
	   
	</div>
	    
	      <div class="page">
		  
	   

	    <div class="section" id="about"><h1>ABOUT</h1><hr></div>

	    <div class="container">
	      <div class="row">
		<div class="col-md-4">
		  <div class="well">
		    <a href="/images/team.jpg" target="_blank"><img src="/images/team.jpg" style="height:100&percnt;; width:100&percnt;" alt="Srm-search engine team"></a>
		  </div>
		</div>
		<div class="col-md-8">
		  <div class="well">
		    <h3><u>What SRM Search Engine is....</u></h3>
		    <p>SRM-Search Engine is an initiative of SRM University, which aims to build a search engine for educational purposes and provide better searches and apt results for the queries of its users. The project started on September 1, 2012. The project got funded by the National Internet Exchange of India, Department of Electronics and Information Technology, on September 8, 2013. SRM university provides all the necessary help to establish the laboratory and to design and develop the Search Engine.</p>
		    <p><a id="contact_us" href="" class="btn btn-default">Contact Us</a></p>
		  </div>
		</div>
	      </div><!--/.row-->
	    </div><!--/.container-->

	    
	 
	 
	    
	    
	      </div>
	<div class="page">
	      <div class="section" id="what-i-do">
	     <h1>How search works</h1><hr></div>
	 
	  <div class="container">
	      <div class="row">
		<div class="col-md-6">
		  <div class="well">
		    <h3>INFRASTRUCTURE</h3>
		    <p align="justify">The project is sustained by a 20MBPS leased line which is protected by a 100D fortigate fire wall. A node from the high performance computing cluster of SRM University has also been allotted. The main server boasts 64 GB of RAM, 6TB of storage and a 32 core Xeon processor. Also, the lab is equipped with 15 workstations comprising 4th generation i5 processors. The whole network adds up to a pooled storage of 13.5TB and 92 cores of processing power. the same can be virtualized to 550 cores using open stack. The lab is also well equipped with the necessary network peripherals such as switch, router, etc.</p>
	<!--/.col-6-->
		    </div>
		  </div>
		
		<div class="col-md-6">
		  <div class="well">
		    <h3>DEVELOPMENT</h3>
		    <p>The main crawler, which is pretty much the heart of the project has already reached a capacity of being able to crawl 1 crore webpages in about 50 hours. the crawling amounts to an approximate data of 500 GB in the speculated time(50 hours). The same data is reduced by the use of distributed computing/hadoop to index the data frequently(every 50 hours). The other key part has been the development of the knowledge data set for different domains such as Government, Sports, Automobiles, Finance, Wealth, Education, etc. The collected domains are again divided into four categories:-<br />
				<ul>
				<li>Static</li>
				<li>Static with Location</li>
				<li>Dynamic</li>
				<li>Dynamic with Location</li>
				</ul>

		  </div>
		</div>
	      </div><!--/.row-->
	    </div><!--/.container-->

	  </div>
	      <div class="page">
		  <div class="section" id="what-i-do"><h1>The Team</h1><hr></div>

	   
	    <div class="work visible-lg" style="height:250px !important;">
		<div class="container" style="padding-top: 2&percnt;;">
		<div class="row">
	
		  <div class="col-md-3">
		      <a href="#" style="text-decoration: none;"><h3><i class="glyphicon glyphicon-user"></i>&nbsp;Hardware and Networks</h3></a>
		    
		  </div>
		  <div class="col-md-3">
		   <a href="#" style="text-decoration: none;"> <h3><i class="glyphicon glyphicon-user"></i>&nbsp;User Experience</h3></a>
		    
		  </div>
		  <div class="col-md-3">
		   <a href="#" style="text-decoration: none;"> <h3><i class="glyphicon glyphicon-user"></i>&nbsp;Information Systems</h3></a>
		   
		  </div>
		  <div class="col-md-3">
		   <a href="#" style="text-decoration: none;"> <h3><i class="glyphicon glyphicon-user"></i>&nbsp;Knowledge Database </h3></a>
		   
		  </div>
		
		
		
		</div><!--/.row-->
		<div class="row">
		      <div class="col-md-12">
		              <a href="#"  style="text-decoration: none;"> <h3><i class="glyphicon glyphicon-user"></i>&nbsp;Indexing and Query Handling</h3></a>
		    
		  </div>
		</div>
	      </div><!--/.container-->
	    </div><!--/.work-->
	    <br/>
	    <br/>
	    <div style="margin-left: auto;margin-right: auto; width: 15&percnt;;">
		<button type="button" class="btn btn-lg btn-default popover-dismiss" data-toggle="popover" title="" data-content="Under Construction !">See all our members</button>
	    </div>
	      </div>
	  <div class="page">
	      <div class="section" id="work"><h1>RECENT WORK</h1><hr></div>

	    <div class="container">
	      <div class="row">
		<div class="col-md-6">
		  <div class="well">
		    
	     
		    
		    <div class="spacer"></div><div class="spacer"></div>
		  </div>
		</div>
		<div class="col-md-6">
		  <div class="well">
		    
		    <h3></h3>
		    <p></p>
		    <div class="spacer"></div>
		    <div class="spacer"></div>
		  </div>
		</div>
	      </div><!--/.row-->
	    </div><!--/.container-->

	  </div>
	      <div class="page" id="lpage">
	      <!--<div class="hidden-xs"><div class="work-together" id="contact">LETS WORK TOGETHER</div></div>-->
	    <div class="section" id="contact"><h1>CONTACT US</h1><hr></div>
	<div class="alert alert-danger" id="warning"><strong>Oh Snap !</strong> This website works on JavaScript ! Please enable it !</div>
	    <div class="work-together">
	      <div class="container">
		<div class="row">
		  <div class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
		    <h3>Send us a message</h3>
		    <div class="spacer"></div>
		    <form class="form-horizontal" role="form" id="form" action="/cgi-bin/response.py" method="post">
		      <div class="form-group">
		        <label for="name" class="col-sm-2 control-label">Name</label>
		        <div class="col-sm-10">
		          <input type="text" class="contact form-control" name="name" id="name" placeholder="Name">
		        </div>
		      </div>
		      <div class="form-group">
		        <label for="email" class="col-sm-2 control-label">Email</label>
		        <div class="col-sm-10">
		          <input type="email" class="contact form-control" name="email" id="email" placeholder="Email">
		        </div>
		      </div>
		      <div class="form-group">
		        <label for="subject" class="col-sm-2 control-label">Subject</label>
		        <div class="col-sm-10">
		          <input type="text" class="contact form-control" name="subject" id="subject" placeholder="Subject">
		        </div>
		      </div>
		      <div class="form-group">
		        <label for="message" class="col-sm-2 control-label">Message</label>
		        <div class="col-sm-10">
		          <textarea class="contact form-control" rows="3" name="message" id="message" placeholder="Message"></textarea>
		        </div>
		      </div>
		      <div class="form-group">
		        <div class="col-sm-offset-2 col-sm-10">
		          <input type="submit" value="Send" class="btn btn-default" name="submit">
		        </div>
		      </div>
		    </form>
		  </div><!--/.col-->
		  <div class="col-lg-4 col-md-4 hidden-sm hidden-xs">
		    <h3>Contact Details</h3><div class="spacer"></div>
		    <p class="lead" style="margin-bottom:0px;"><i class="fa fa-map-marker"></i>&nbsp; Room No. 29, 4th Floor,University Block,SRM University</p><p class="lead" style="text-indent:24px">Chennai-603203 Tamil nadu</p>
		    <p class="lead"><i class="fa fa-phone"></i>&nbsp;0xxxxx-xxxxx </p>
		    <p class="lead"><i class="fa fa-envelope"></i>&nbsp; www.xyz@abc.com</p>
		  </div>
		</div><!--/.row-->
	      </div><!--/.container-->
	      <div class="container hidden-sm hidden-xs"><div class="spacer"></div><div class="spacer"></div><footer><p class="pull-right">&copySRM-SE</p></footer></div>
	    </div><!--/.work-together-->
	 
	  </div>
	      
	   
	    </body>
	</html>
"""
