import re,os,sys,MySQLdb,thread,threading,hashlib,sha
from bs4 import BeautifulSoup
from multiprocessing import Process,Lock
from urlparse import urljoin
from urllib2 import urlopen
import time
from Queue import Queue
start_time = time.time()
links=[]
website="http://dir.yahoo.com/arts"
sys.setrecursionlimit(999999999)
ThreadList=[]
pcont=1
def checkDuplicate(filename):
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","tester" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		sql="SELECT `link` FROM `DirYahooCom` WHERE `filename`='%s';"%(str(MySQLdb.escape_string(filename)))
		# Execute the SQL command
		cursor.execute(sql)
		results=cursor.fetchall()
		db.commit()
		db.close()
		if len(results)==0:
			return True
		else:
			return False
	except Exception as e:
		print e
		print "error in checkDuplicate()"
		return False
		db.rollback()
class pt(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		try:
			global pcont,ThreadList,pq
			prng=20
			while True:
				#print len(ThreadList)
				if len(ThreadList)>prng and pq.qsize()==0 and pcont==1:
					for i in range(prng-20,prng):
						try:
							pq.put(ThreadList[i])
						except Exception as e:
							pq.put(None)
					print "Process added to Queue"
					prng+=20
					pcont=0
		except Exception as e:
			print "pt()",prng
			print e
class pt1(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		try:
			global pcont,ThreadList,pq
			ptemp=[]
			while True:
				#print pcont,"  ",pq.qsize()
				if pcont==0 and pq.qsize()==20:
					#print "In"
					for i in range(20):
						temp=pq.get()
						if not temp is None:
							ptemp.append(temp)
							ptemp[i].start()
					for i in range(20):
						if not ptemp[i] is None:
							ptemp[i].join()
							#print "stop"
							if ptemp[i] in ThreadList:
									ThreadList[ThreadList.index(ptemp[i])]=None
					print "Queue cleared"
					pcont=1
					ptemp=[]
					running=[]
		except Exception as e:
			print e
			print "pt1()"
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
		return True
	except MySQLdb.IntegrityError as a:
		return False
		db.rollback()
	except Exception as e:
		print "Error in addURL() class"
		print e
		return False
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
				except Exception as e:
					print e
					print "Dfg3"
					continue
	def __del__(self):
        	#print "deleted"
		pass
class Crawl(threading.Thread):
	url=""
	fileid=""
	def __init__(self,url,fileid):
		threading.Thread.__init__(self)
		self.url=url
		self.fileid=fileid
	def run(self):
		try:
			global ThreadList
			#print url
			if not self.url is None:
				self.url=self.url.strip('/')
				if addURL(self.url,str(self.fileid)+'.html'):
					r=getLinks(self.url)
					if not r is None:
						obj=r[0]
						code=str(r[1])
						lock = threading.Lock()
						lock.acquire()
						try:
							ThreadList.append(createFile(self.url,code,str(self.fileid)+'.html'))
							ThreadList.append(newThread(str(self.url),str(code)))
						except Exception as e:
							print "Error in one of the threads"
							print e
							lock.release()
						finally:
							lock.release()
						if not obj is None:
							#getting all anchor tags
							for a in obj:
								#getting clean links
								try:
									temp=cleanUp(a)
									if temp!="":
										#Convert url to hash
										key=str(temp)
										m=hashlib.md5()
										m.update(key)
										s1=m.hexdigest()
										tup=(str(temp),str(s1))
										lock = threading.Lock()
										lock.acquire()
										try:
											ThreadList.append(Crawl(temp,str(s1)))
										finally:
											lock.release()
								except Exception as e:
									print e
									print "Error in crawl(str(temp))"
									continue
		except Exception as a:
			print a
			print "Error in main crawl()"
			#return
print "Process is Running . . . Do not Interrupt !"
print "Tilak says 'Valar Morghulis'"
pq=Queue(maxsize=20)
#Start pt()
mainp=pt()
mainp.start()
#Start pt1()
mainp1=pt1()
mainp1.start()
#Convert url to hash
key=str(website)
m=hashlib.md5()
m.update(key)
s1=m.hexdigest()
#Call to Crawl() function
Crawl(website,str(s1)).start()
#Waiting for threads to exit
mainp.join()
mainp1.join()
print "No one replied 'Valar Dohaires'"
print "--- %s seconds ---" %(time.time() - start_time)

