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
		<title>seekho.com</title>
		<link rel="shortcut icon" href="/images/fav.ico">
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="/css/index.css">
		<link rel="stylesheet" href="/css/error.css">
		<link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">
		<script type="text/javascript" src="/js/jQuery/jQuery.js"></script>
	      <script type="text/javascript" src="/bootstrap/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="/js/index.js"></script> 
	    </head>
	    
	    <body>
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
		            <a class="navbar-brand" target="blank" href="/">    <img src="/images/logo.png" width="20" height="20"/> Seekho.com</a>
		        </div>
		        <div class="navbar-right">
		             <a class="navbar-brand" target="blank" href="#">Contact Us</a>
		              <a class="navbar-brand" target="blank" href="#">Help</a>
		        </div>
	   
		    </div>
		</div>
	</body>
	    <!--Scripts at the end-->
	     
	</html>"""%(t,b)

