import re,os,sys,MySQLdb
from bs4 import BeautifulSoup
from urlparse import urljoin
from urllib2 import urlopen
import time
start_time = time.time()
links=[]
fileid="1"
website="http://dir.yahoo.com/Arts"
sys.setrecursionlimit(999999999)
def cleanhtml(raw_html):
	cleanr =re.compile('<.*?>')
	cleantext = re.sub(cleanr,'', raw_html)
	return cleantext
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
		print e
		db3.rollback()
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
		print e
		db3.rollback()	
def createFile(url,code):
	global fileid
	filename=str(fileid)+'.html'
	fo=open(filename,'a')
	fo.write(str(code))
	fo.close()
	fileid=str(int(fileid)+1)
	addURL(url,filename)
def getLinksAndDesc(url,code):
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
def getLinks(url):
	try:
		time.sleep(0.5)
		html = urlopen(str(url))
		html=html.read()
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
		print e
		return
		

def cleanUp(url):
	"""Cleans up url before adding to database"""
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

def Crawl(url):
	try:
		url=url.strip('/')
		global links
		if not str(url) in links:
			r=getLinks(url)
			links.append(str(url))
			obj=r[0]
			code=str(r[1])
			createFile(url,code)
			LinksDescTitle=getLinksAndDesc(url,code)
			Links=[]
			Desc=[]
			Title=[]
			ylink=""
			if  not LinksDescTitle is None:
					Links=LinksDescTitle[0]
					Desc=LinksDescTitle[1]
					Title=LinksDescTitle[2]
					ylink=str(url)
					for i in range(0,len(Links)):
						try:
							addLinkDescTitleYlink(Links[i],Desc[i],Title[i],ylink)
						except Exception as e:
							print e
							continue
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
						continue
			else:
				return
	except Exception as a:
		print a
		return
print "Process is Running . . . Do not Interrupt !"
print "Tilak says 'Valar Morghulis'"
Crawl(website)
print "No one replied 'Valar Dohaires'"
print "--- %s seconds ---" %(time.time() - start_time)

