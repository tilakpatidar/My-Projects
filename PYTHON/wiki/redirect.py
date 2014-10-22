from multiprocessing import Pool 
def cleanhtml(raw_html):
  import re
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  re=None
  return cleantext
def insertDB(idd,redirect):
	import MySQLdb
	db = MySQLdb.connect("localhost","root","song","SRMSE" )
	cursor = db.cursor()
	sql = "UPDATE source1 SET redirect='%s' WHERE id='%s'" % (redirect,idd)
	try:
	  cursor.execute(sql)
	  #print x
	  db.commit()
	except:
	  print "Error: unable to insert data"
	  db.rollback()
	db.close()
	MySQLdb=None
	
	#foo=open("redirectData")
	#foo.write(idd+";"+redirect+"\n")
	#foo.close()
def fetchDB(ilim,flim):
	import MySQLdb
	db = MySQLdb.connect("localhost","root","song","SRMSE" )
	cursor = db.cursor()
	sql = "SELECT id,title FROM source1 WHERE redirect IS NULL LIMIT %s,%s " % (ilim,flim)
	try:
	   cursor.execute(sql)
	   results = cursor.fetchall()
	   #print results
	   temp=[]
	   if not results is None:
		   for row in results:
		      temp.append((row[0],row[1]))
		   return temp
	except:
	   print "Error: unable to fetCh data"
	db.close()
	MySQLdb=None
def ret(x):
	from bs4 import BeautifulSoup 
	try:
		idd,title=x
		import urllib2
		url="http://en.wikipedia.org/w/index.php?title=%s&action=info"%(str(title.replace(' ','_')))
		#print idd
		#print url 
		code=urllib2.urlopen(url)
		code=code.read()
		soup=BeautifulSoup(code)
		table=soup.find("table",{'class':'wikitable mw-page-info'})
		soup=BeautifulSoup(str(table))
		td=soup.findAll("td")
		redirect=0
		for t in td:
			try:
				if str(cleanhtml(str(t)))=='Number of redirects to this page':
					redirect=int(cleanhtml(str(td[td.index(t)+1])))
					break
			except ValueError as e:
				print e
				redirect=0
		#print redirect
		insertDB(idd,redirect)
	except Exception as e:
		print url
		print e
	urllib2=None
	BeautifulSoup=None
def pop1(l,t):
	print l,t
i=0
j=0
while True:
	try:
		li=fetchDB(i,j)
		#print len(li)
		p=Pool(150)
		p.map(ret,li)
		j+=1000
		i+=1000
	except Exception as x:
		print x
		#print i
		j+=1000
		i+=1000
		continue
#foo.close()

