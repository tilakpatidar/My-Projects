#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect("127.0.0.1","root","1","iimb")
cursor = db.cursor()


def generate2(years,units,col,vals,val):
	vals = str(vals)
	vals = vals.replace("L","")
	print """
	<script>
	$(function () {
	    $('#container"""+str(val)+"""').highcharts({
		title: {
		    text: 'Changes',
		    x: -20 //center
		},
		xAxis: {
		    categories: """+str(years)+"""
		},
		yAxis: {
		    title: {
		        text: '"""+units+"""'
		    },
		    plotLines: [{
		        value: 0,
		        width: 1,
		        color: '#808080'
		    }]
		},
		legend: {
		    layout: 'vertical',
		    align: 'right',
		    verticalAlign: 'middle',
		    borderWidth: 0
		},
		credits: {
	      enabled: false
	  	},
		series: [{
		    name: '"""+col+"""',
		    data: """+vals+"""
		}]
	    });
	});
	</script>
	"""


def generate(final,parameter,val,area):
	print """
	<script>
	$(function () {
		$('#container"""+str(val)+"""').highcharts({
		    chart: {
		        type: 'column'
		    },
		    title: {
		        text: '"""+parameter+"""'
		    },
		    xAxis: {
		        categories: """+str(area)+"""
		    },
		    credits: {
	      enabled: false
	  },
		    series: """+final+"""
		});
	    });
	</script>
	"""


def counter(upvote,downvote,parameter,val):
	temp = []
	up = {}
	down = {}
	area = []
	for i in upvote:
		sql = "SELECT `"+parameter+"` FROM `users` WHERE `uid`="+str(i)+";"
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			temp.append(row[0])
	temp2 = list(set(temp))
	area.extend(temp2)
	for i in temp2:
		up[i] = temp.count(i)
	temp = []
	for i in downvote:
		sql = "SELECT `"+parameter+"` FROM `users` WHERE `uid`="+str(i)+";"
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			temp.append(row[0])
	temp2 = list(set(temp))
	area.extend(temp2)
	for i in temp2:
		down[i] = temp.count(i)
	area = list(set(area))
	final = "[{name: 'support',data: ["
	for i in area:
		if i in up.keys():
			if(i!=area[len(area)-1]):
		       		final = final+str(up[i])+""", """
			else:
				final = final+str(up[i])
		else:
			if(i!=area[len(area)-1]):
		       		final = final+"""0, """
			else:
				final = final+"""0 """
	final = final+"]},{name: 'oppose',data: ["
	for i in area:
		if i in down.keys():
			if(i!=area[len(area)-1]):
		       		final = final+str(down[i]*(-1))+""", """
			else:
				final = final+str(down[i]*(-1))
		else:
			if(i!=area[len(area)-1]):
		       		final = final+"""0, """
			else:
				final = final+"""0 """
	final = final+"]}]"
	generate(final,parameter,val,area)

def counter2(val,col):
	years = []
	vals = []
	sql = "SELECT `year`,`"+col+"` FROM `"+str(val)+"` ORDER BY `year`;"
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		years.append(row[0])
		vals.append(row[1])
	yield years
	yield vals

def evaluate(name,upvote,downvote,pid):
	print """
	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="utf-8">
	<script language="Javascript" type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.js"></script>"""
	print "<strong>",name,"</strong></br></br>"
	upvote = upvote.split("|")
	upvote.remove("")
	downvote = downvote.split("|")
	downvote.remove("")
	years,vals = counter2(pid,"duration")
	generate2(years,"Days","duration",vals,0)
	years,vals = counter2(pid,"amount")
	generate2(years,"Rupee","amount",vals,1)
	counter(upvote,downvote,"geography",2)
	counter(upvote,downvote,"area",3)
	counter(upvote,downvote,"gender",4)
	counter(upvote,downvote,"caste",5)
	counter(upvote,downvote,"marital",6)
	counter(upvote,downvote,"age",7)
	counter(upvote,downvote,"income",8)
	val = 9
	print """
	</head>
	<body>
	<script language="Javascript" type="text/javascript" src="http://code.highcharts.com/highcharts.js"></script>
	<script language="Javascript" type="text/javascript" src="http://code.highcharts.com/modules/exporting.js"></script>"""
	for i in range(0,val):
		print """
	<div id="container"""+str(i)+"""" style="max-width: 410px; height: 400px; margin: 0 auto"></div>"""
		if(i!=val-1):
			print """
	<hr style="height:3px;border:none;color:#333;background-color:#333;" />
	"""
	print """
	</body>
	</html>
	"""
