#!/usr/bin/python
# Import modules for CGI handling 
import cgi#, cgitb
#print 'Content-Type: text/html\n'
def errorMessage(t,b):
	print """
	<!DOCTYPE html>
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
		 <link rel="stylesheet" href="/css/login.css">
		<link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">
	    </head>
	    <body>
		<div id="top">
		    
		</div>
		<div id="main" style="padding-top:8&percnt;;padding-bottom:8&percnt;;">
		   <div class="container">
		   <div>
		   <legend >%s</legend>
		   </div>
		   <div class="row">
		   <div class="col-lg-12" style="">
		   %s
		   </div>
		   </div>
		   </div>
		    </div>
		</div>
		<div id="footer">
		    <div  class="navbar-default">
		        <div class="navbar-header">
		            <a class="navbar-brand" target="blank" href="http://www.srmuniv.ac.in">    <img src="/images/logo.png" width="20" height="20"/> SRM University</a>
		        </div>
		        <div class="navbar-right">
		            <a class="navbar-brand" target="blank" href="http://evarsity.srmuniv.ac.in/srmswi/usermanager/youLogin.jsp">Evarsity</a>
		             <a class="navbar-brand" target="blank" href="#">Contact Us</a>
		              <a class="navbar-brand" target="blank" href="#">Help</a>
		        </div>
	   
		    </div>
		</div>
	</body>
	    <!--Scripts at the end-->
	     <script type="text/javascript" src="/js/jQuery/jQuery.js"></script>
	      <script type="text/javascript" src="/bootstrap/js/bootstrap.min.js"></script> 
		 <script type="text/javascript" src="/js/login.js"></script>
		 
	</html>"""%(t,b)

