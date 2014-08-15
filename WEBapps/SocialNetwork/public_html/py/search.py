#!/usr/bin/python -v3
# Import modules for CGI handling 
import cgi, cgitb,MySQLdb,hashlib,sha, time, Cookie, os
cgitb.enable()
print "Content-type:text/html\r\n\r\n"
def queryBuilder(cols,value,op,cond,init,total):
	queryStr="SELECT  DISTINCT fname,lname,profile_pic,username,year,vertical,category,regno from info WHERE"; 
	l=len(cols)
	i=0
	while i<l:
		col_name=str(cols[i])
		val_name=str("'"+value[i].strip()+"'")
		if i==(l-1):
			queryStr=queryStr+" "+col_name+" "+op+' '+val_name+" LIMIT "+str(init)+","+str(total)
		else:
			queryStr=queryStr+" "+col_name+" "+op+' '+val_name+" "+cond
		i=i+1
	return queryStr



def webPage(code,user_query,result):
	print"""
<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->

<html>
    <head>
        <title>www.blah.com</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width">
        
         <script type="text/javascript" src="/js/jQuery.js"></script>
      
         <link type="text/css" href="/css/memberSearch.css" rel="stylesheet"/>
         <script type="text/javascript" src="/js/memberSearch.js"></script>
	<script type="text/javascript">
		$(document).ready(function(){
			$("#search").val('%s');
			});
		%s
	</script>
           
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap.min.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.css.map" rel="stylesheet" media="screen">
       <link href="/bootstrap-3.1.1-dist/css/bootstrap-theme.min.css" rel="stylesheet" media="screen">
       <script type="text/javascript" src="/js/jquery-1.9.1.min.js"></script>
       
<script type="text/javascript" src="/js/jquery-ui.min.js"></script>
  <link rel="stylesheet" href="/css/jquery-ui.min.css" type="text/css" /> 
  <link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.4/themes/base/jquery-ui.css">


  <script type="text/javascript" src="/js/jquery.ui.autocomplete.html.js"></script>
    </head>
    <body  id="body" >
              <div id="fb-root"></div>
            <script>(function(d, s, id) {
              var js, fjs = d.getElementsByTagName(s)[0];
              if (d.getElementById(id)) return;
              js = d.createElement(s); js.id = id;
              js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.0";
              fjs.parentNode.insertBefore(js, fjs);
            }(document, 'script', 'facebook-jssdk'));</script>
        
        <div class="alert alert-danger" id="warning"><strong>Oh Snap !</strong> This website works on JavaScript ! Please enable it !</div> 
        <div id="top" class="row">
        
            <nav id="navbar1"  class="navbar navbar-default navbar-inverse navbar-fixed-top " role="navigation">
                <div id="navbar"  class="container-fluid">
                    <a id="home" class="navbar-brand glyphicon glyphicon-home" href="/">Home</a>
                    <a id="help" class="navbar-brand glyphicon glyphicon-user  " href="/help.html"> Help</a>
                    <a id="aboutUs" class="navbar-brand glyphicon glyphicon-info-sign" href="/abt_us.html"> AboutUs</a>
                    <a id="signin" class="navbar-brand glyphicon glyphicon-log-in" href="/index.html"> SignIn</a>
                    
                </div>
                </nav>
        
        </div>
        <div class="row" id="middle">
        
           
             <div id="upr"> 
                 <div id="tiles" style="float: top;padding-top: 4&percnt;;margin-left: 5&percnt;;margin-right: 5&percnt;;margin-bottom: 0&percnt;;">
                 
                 <div class="row" style="display:inline;" >
                               %s
                 </div>
                     <div style="float: bottom;position: absolute;left: 78&percnt;;bottom: -2&percnt;;">
                         <ul id="pages" class="pagination">
                             <li><a hidden href="javascript:prev();">&laquo;</a></li>
                            <li><a href="javascript:$('#page').val('1'); $('#srch').submit();">1</a></li>
                            <li><a href="javascript:$('#page').val('2');$('#srch').submit();">2</a></li>
                            <li><a href="javascript:$('#page').val('3');$('#srch').submit();">3</a></li>
                            <li><a href="javascript:$('#page').val('4');$('#srch').submit();">4</a></li>
                            <li><a href="javascript:$('#page').val('5');$('#srch').submit();">5</a></li>
                            <li><a href="javascript:next();">&raquo;</a></li></ul>
                     </div>
                </div>
                 
                 
             <br/>
                </div>
                <div id="btm" class="form-inline"> 
                    <form name="srch" id="srch" action="search.py" method="POST">
                        <center>
                            <div class="input-group" id="search_btn">
                            <input id="search" class="form-control" name="search" placeholder="Search by name" type="text">
                            <input hidden type="text" name="page" id="page">
                            <span class="input-group-btn">
                            <button class="btn btn-primary" type="submit"><span class="glyphicon glyphicon-search"></span> </button>
                             </span>
                        </div> </center>
                        
                    </form>
           
                </div>
            
            <br/>
          
        
      
        </div>
     
       
    </body>
</html>
  
        

"""%(user_query,code,result)



# Create instance of FieldStorage 
form = cgi.FieldStorage() 


# Get data from fields
query = form.getvalue('search')
user_query=query
page=form.getvalue('page')


init=(int(page)*5)-5
total=5



cond='OR'
op='LIKE'
arr=query.split(":")
cols=[]
value=[]
l=len(arr)
i=0
#genrate cols
while i<l:
	cols.append(arr[i])
	i=i+2
#print "Cols :",cols

#genrate value
l=len(arr)
i=1
while i<l:
	value.append(arr[i])
	i=i+2
#print "Value :",value


l=len(cols)
i=0
while i<l:
	e=str(str(cols[i]).strip())
	
	if e=="First Name":
		cols[i]="fname"
	elif e=="Last Name":
		cols[i]="lname"
	elif e=="Email Address":
		cols[i]="email"
	elif e=="Vertical":
		cols[i]="vertical"
	elif e=="Category":
		cols[i]="category"
	elif e=="Year":
		cols[i]="year"
	elif e=="Sex":
		cols[i]="sex"
	
	i=i+1
#print "New Cols :",cols
query=queryBuilder(cols,value,op,cond,init,total)
#print query
try:
	# Open database connection
	db = MySQLdb.connect("localhost","root","1","mem_info" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# execute SQL query using execute() method.
	sql=query

	# Execute the SQL command
	cursor.execute(sql)
	
	# Fetch all the rows in a list of lists.
	results=cursor.fetchall()
	db.close()
	result=""
	
	if not results is None:
		for val in results:
			fname=val[0]
			lname=val[1]
			profile_pic=val[2]
			username=val[3]
			year=val[4]
			vertical=val[5]
			category=val[6]
			regno=val[7]
			name=fname+" "+lname
			result=result+"""
<div class="col-sm-6 col-md-4" style="display:inline;width: 20&percnt;;height: 100&percnt;;">
                                          <div class="thumbnail">
 <div class="center-block" style="background-image: url('/images/%s');background-size:contain,cover;background-repeat: no-repeat;width: 140px;height: 120px;">
                                             
                                        </div>
                                         
                                          <div class="text-center">
                                              <h4>%s</h4>
                                              		<span class="label label-default center-block">%s</span><br/>
                                                          <span class="label label-primary">Year</span>
                                                          <span class="label label-default">%s</span><br/>
                                                           <span class="label label-primary">Category</span>
                                                          <span class="label label-default">%s</span><br/>
                                                          <span class="label label-primary">Vertical</span>
                                                          <span class="label label-default">%s</span>
                                                          <br/>
                                                          <span class="label label-primary">Username</span>
                                                          <span class="label label-default">%s</span>
                                                  <br/>
                                                  <br/>
                                              
                                              <p ><a href="#"  class="btn btn-primary center-block" role="button">View Profile</a></p>
                                          </div>
                                          </div>
                                     </div>
"""%(profile_pic,name,regno,year,category,vertical,username)
	else:
		print "Empty result set"
except:
	print "Exception occured"



if result is "":
	code="""$(document).ready(function(){document.getElementById("warning").innerHTML="<strong>Oh!</strong> No more results found !!!.";         
                    $("#warning").show();});"""
	webPage(code,user_query,result)
else:
	code=""
	webPage(code,user_query,result)





#print user_query

