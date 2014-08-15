import re,os,sys,MySQLdb,thread,threading,hashlib,sha
from bs4 import BeautifulSoup
from multiprocessing import Process
from urlparse import urljoin
from urllib2 import urlopen
import time
from Queue import Queue
start_time = time.time()
links=[]
website="http://dir.yahoo.com/arts"
sys.setrecursionlimit(999999999)
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
			global ProcessList
			while True:
				temp=ProcessList.get()
				p = Process(target=Crawl,args=(temp[0],temp[1]))
				p.start()
		except Exception as e:
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
def Crawl(url,fileid):
	try:
		#print url
		if not url is None:
			url=url.strip('/')
			if checkDuplicate((fileid)+'.html'):
				r=getLinks(url)
				#print r
				if not r is None:
					addURL(url,str(fileid)+'.html')
					obj=r[0]
					code=str(r[1])
					try:
						a=createFile(url,code,str(fileid)+'.html')
						b=newThread(str(url),str(code))
						a.start()
						b.start()
						a.join()
						b.join()
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
									#Convert url to hash
									key=str(temp)
									m=hashlib.md5()
									m.update(key)
									s1=m.hexdigest()
									tup=(str(temp),str(s1))
									global ProcessList
									ProcessList.put(tuple(tup))
									#print len(ProcessList)
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
ProcessList=Queue(maxsize=20)
#Start pt()
mainp=pt()
mainp.start()
#Convert url to hash
key=str(website)
m=hashlib.md5()
m.update(key)
s1=m.hexdigest()
#Call to Crawl() function
Crawl(website,str(s1))
#Waiting for threads to exit
mainp.join()
print "No one replied 'Valar Dohaires'"
print "--- %s seconds ---" %(time.time() - start_time)

