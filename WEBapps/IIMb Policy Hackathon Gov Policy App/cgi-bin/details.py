#!/usr/bin/python
import MySQLdb
import random
import cgitb
cgitb.enable()
print "Content-Type:text/html\r\n\r\n"
con=MySQLdb.connect("127.0.0.1","root","1","test")
cur=con.cursor()
sql="SELECT * FROM business_2 limit 0,100"
cur.execute(sql)
result=cur.fetchall()
value=""""""
for row in result:
	bid=row[0]
	name=str(row[1])
	location=str(row[4])
	r=random.randint(100,255)
	g=random.randint(100,255)
	b=random.randint(100,255)
	value+=("""
		<div class="panel-group" id="accordion"  style='width:30&percnt;'>
  <div class="panel panel-default">
   
        <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne">
          <div class="data container" id="%s %s" style="background-color:rgb(%s,%s,%s)">
			<div class="row">
				<div class="col-md-12" id="details">
					<span>%s</span><span><h5><i>%s</i></h5></span>
				</div>
			</div>
			<div class="row">
				<div id="%d" class="col-md-6 pull-right">
					<button class="like btn btn-primary" style="color:black">like</button>
					<button class="post btn btn-info" style="color:black">post</button>
				</div>
			</div>
			<div class="row">
				<div class="friends" style="margin-left:10px">
				</div>
			</div>
		
        </a>
      
    </div>
    <div id="collapseOne" class="panel-collapse collapse in">
      <div class="panel-body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
      </div>
    </div>
  </div>
  

</div>
		
		"""%(name,location,r,g,b,name,location,bid))
print value
