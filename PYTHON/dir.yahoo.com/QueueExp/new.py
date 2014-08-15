import re,os,sys,MySQLdb,thread,threading
from bs4 import BeautifulSoup
from urlparse import urljoin
from urllib2 import urlopen
import time
from Queue import Queue
start_time = time.time()
links=[]
fileid="0"
website="http://dir.yahoo.com/arts"
sys.setrecursionlimit(999999999)
ThreadList=[]
cont=1
def checkDuplicate(url):
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","tester" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		sql="SELECT `link` FROM `DirYahooCom` WHERE `link`='%s';"%(str(MySQLdb.escape_string(url)))
		# Execute the SQL command
		cursor.execute(sql)
		results=cursor.fetchall()
		db.commit()
		db.close()
		if len(results)==0:
			return True
		return False
	except Exception as e:
		print e
		print "error in checkDuplicate()"
		return False
		db.rollback()
def t1():
	try:
		global cont
		temp=[]
		while True:
			if (q.qsize()==10) and (cont==0):
				for i in range(10):
					temp.append(q.get())
					temp[i].start()
				#print(threading.active_count())
				for i in range(10):
					temp[i].join()
					if temp[i] in ThreadList:
						#print "t"
						del ThreadList[ThreadList.index(temp[i])]
						#del temp[i]
				#print "10 completed"
				#print time.time()-start_time
				cont=1
				temp=[]
	except Exception as e:
		print e
		print "t1()"

def t():
	try:
		global cont
		rng=10
		while True:
			if (len(ThreadList)>rng and q.qsize()==0)and(cont==1):
				#print "Start"
				for i in range(rng-10,rng):
					q.put(ThreadList[i])
				cont=0
				#print len(ThreadList)
				rng+=10
	except Exception as e:
		print "t()",rng
		print e
		
def cleanhtml(raw_html):
	try:
		cleanr =re.compile('<.*?>')
		cleantext = re.sub(cleanr,'', raw_html)
		return cleantext
	except Exception as e:
		print e
		print "Error in cleanhtml()"
		return None
def addURL(url,filename):
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","tester" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		sql="INSERT INTO `DirYahooCom`(`filename`,`link`) VALUES ('%s','%s');"%(str(MySQLdb.escape_string(filename)),str(MySQLdb.escape_string(url)))
		# Execute the SQL command
		cursor.execute(sql)
		db.commit()
		db.close()
	except Exception as e:
		print "Error in addURL() class"
		print e
		db.rollback()
class createFile(threading.Thread):
	url=""
	code=""
	filename=""
	def __init__(self,url,code,filename):
		threading.Thread.__init__(self)
		self.url=url
		self.code=code
		self.filename=filename
	def run(self):
		try:
			fo=open(self.filename,'a')
			fo.write(str(self.code))
			fo.close()
		except Exception as e:
			print "Error in createFile class"
			print e
	def __del__(self):
        	#print "deleted"
		pass
def getLinks(url):
	try:
		html = urlopen(str(url))
		html=html.read()
		#print html
		links=re.findall('<a href="?\'?([^"\'>]*)',str(html))
		base=re.findall('<base href="?\'?([^"\'>]*)',str(html))
		newlinks=[]
		for i,a in enumerate(links):
			if not 'http' in a:
				if not base:
					base.append("//dir.yahoo.com")
				newlinks.append(str("http:"+urljoin(base[0],a)))
		return newlinks,html
	except Exception as e:
		print "Error in getLinks()"
		print e
		return None
		

def cleanUp(url):
	"""Cleans up url before adding to database"""
	try:
		if not 'dir.yahoo.com' in url:
			return ""
		#do not send file links for crawling
		fileName, fileExtension = os.path.splitext(str(url))
		if fileExtension!="":
			return ""
		#check for # paths
		if "#" in str(url):
			return ""
		#replace ../
		if r"../" in str(url):
			url=url.replace(r"../","")
		#replace // to /
		if r"//" in str(url[8:]):
			if not r"http" in str(url[8:]):
				url=url[:8]+url[8:].replace(r"//","/",)
		return url
	except Exception as e:
		print "Error in cleanUp()"	
		print e
		return None
class newThread(threading.Thread):
	url=""
	code=""
	def __init__(self,url,code):
		threading.Thread.__init__(self)
		self.url=url
		self.code=code
	def __del__(self):
        	#print "deleted"
		pass
	def run(self):
		"""Thread to fsetch LinksDescTitle from dwnld souce code"""
		def getLinksAndDesc(code):
			try:
				description=[]
				links_href=[]
				title=[]
				soup = BeautifulSoup(code)
				div = soup.find("div", { "class" : "st" })
				soup = BeautifulSoup(str(div))
				alinks = soup.findAll("a")
				soup = BeautifulSoup(str(div))
				li=soup.findAll("li")
				for l in li:
					soup= BeautifulSoup(str(l))
					font=soup.find('font')
					temp=str(l)
					ahref=soup.find("a")
					temp=temp.replace(str(font),"")
					temp=temp.replace(str(ahref),"")
					#print temp
					cleantext = cleanhtml(str(temp))
					alinks =ahref.attrs['href']
					tl=ahref.text
					#print tl
					if 'http' in str(alinks):
						links_href.append(alinks)
						description.append(cleantext.strip())
						title.append(tl)
				if len(description)==len(links_href):
					return links_href,description,title
				else:
					return None
			except Exception as e:
				print e
				return None
		def addLinkDescTitleYlink(url,desc,title,link):
			"""Adds url and desc to db"""
			try:
				# Open database connection
				db3 = MySQLdb.connect("localhost","root","1","tester" )
				# prepare a cursor object using cursor() method
				cursor3 = db3.cursor()
				# execute SQL query using execute() method.
				sql3="INSERT INTO `PopularLinks`(`link`, `title`, `description`, `yahooLink`) VALUES ('%s','%s','%s','%s');"%(str(MySQLdb.escape_string(url)),str(MySQLdb.escape_string(title)),str(MySQLdb.escape_string(desc)),str(MySQLdb.escape_string(link)))
				# Execute the SQL command
				cursor3.execute(sql3)
				db3.commit()
				db3.close()
			except Exception as e:
				print "Error in addLinkDescTitleYlink(url,desc,title,link) class newThread"
				print e
				db3.rollback()
		LinksDescTitle=getLinksAndDesc(self.code)
		if  not LinksDescTitle is None:
			Links=[]
			Desc=[]
			Title=[]
			ylink=""
			Links=LinksDescTitle[0]
			Desc=LinksDescTitle[1]
			Title=LinksDescTitle[2]
			ylink=str(self.url)
			for i in range(0,len(Links)):
				try:
					addLinkDescTitleYlink(Links[i],Desc[i],Title[i],ylink)
					#addLinkDescTitleYlink(Links[i],Desc[i],Title[i],ylink)
				except Exception as e:
					print e
					print "Dfg3"
					continue
	def __del__(self):
        	#print "deleted"
		pass
def Crawl(url):
	try:
		if not url is None:
			url=url.strip('/')
			global fileid
			if checkDuplicate(url):
				r=getLinks(url)
				#print r
				if not r is None:
					fileid=str(int(fileid)+1)
					addURL(url,str(fileid)+'.html')
					obj=r[0]
					code=str(r[1])
					try:
						ThreadList.append(createFile(url,code,str(fileid)+'.html'))
						ThreadList.append(newThread(str(url),str(code)))
					except Exception as e:
						print "Error in one of the threads"
						print e
					if not obj is None:
						#getting all anchor tags
						for a in obj:
							#getting clean links
							try:
								temp=cleanUp(a)
								if temp!="":
									Crawl(str(temp))	
							except Exception as e:
								print e
								print "Error in crawl(str(temp))"
								continue
				else:
					return
	except Exception as a:
		print a
		print "Error in main crawl()"
		#return
print "Process is Running . . . Do not Interrupt !"
print "Tilak says 'Valar Morghulis'"
q=Queue(maxsize=10)
thread.start_new_thread(t,())
thread.start_new_thread(t1,())
Crawl(website)
print "No one replied 'Valar Dohaires'"
print "--- %s seconds ---" %(time.time() - start_time)

