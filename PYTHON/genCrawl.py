import thread,threading,re,os
from urlparse import urljoin
import time
from bs4 import BeautifulSoup
import urllib2
start_time = time.time()
links=[]
seedlinks=[]
website="http://www.kubuntu.com/"
Pool=[]
def seedLinks(code):
	soup = BeautifulSoup(code)
	ul = soup.findAll("a")
	for i in ul:
		addSeedLinks(str(i.attrs['href']))
	
	
def setProxy():
	import urllib2
	proxy_handler = urllib2.ProxyHandler({'http':'172.16.0.2:8080'})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)


def getLinks(url):
	try:
		html = urllib2.urlopen(str(url))
		temp=html.read()
		links=re.findall('<a href="?\'?([^"\'>]*)',str(temp))
		seedLinks(temp)
		return links
	except Exception as e:
		print e
		return None
		

def cleanUp(parent,url):
	"""Cleans up url before adding to database"""
	#check for relative paths
	if not 'http' in str(url):
		url=urljoin(str(parent),str(url))
	#do not send file links for crawling
	fileName, fileExtension = os.path.splitext(str(url))
	if fileExtension!="":
		return ""
	#check for correct absolute paths
	if not str(website) in str(url):
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
	if not "http://www.kubuntu.com/" in url:
		return ""
	return url


def addSeedLinks(b):
	"""Adds url and returns True to continue to dwnld"""
	#first creating a lock
	try:
		lock = threading.Lock()
		lock.acquire()
	except:
		#if lock is unsuccessfull return false
		return False
	#no errors above so continue
	try:
		global seedlinks
		global foo1
		if not str(b) in seedlinks:
			seedlinks.append(str(b))
			foo1.write(str(b)+"\n")
			lock.release()
			return True
		return False
	except:
		lock.release()
		return False


def addLinks(b):
	"""Adds url and returns True to continue to dwnld"""
	#first creating a lock
	try:
		lock = threading.Lock()
		lock.acquire()
	except:
		#if lock is unsuccessfull return false
		return False
	#no errors above so continue
	try:
		global links
		global foo
		if not str(b) in links:
			links.append(str(b))
			foo.write(str(b)+"\n")
			lock.release()
			return True
		return False
	except:
		lock.release()
		return False

class Crawl(threading.Thread):
	url=""
	def __init__(self,url):
		threading.Thread.__init__(self)
		self.url=url
	def run(self):
		"""Run method of the thread"""
		obj=getLinks(self.url)
		if obj is None:
			return
		#getting all anchor tags
		try:
			for a in obj:
				#getting clean links
				temp=cleanUp(self.url,a)
				if temp!="":
					if addLinks(temp):
						print temp
						Pool.append(str(temp))
						#ab=Crawl(str(temp))
						#ab.start()
						print "--- %s seconds ---" %(time.time() - start_time)
		except TypeError:
			#Raised when obj is None Type
			pass

setProxy()
foo=open("Links.txt","a")
foo1=open("Arts.txt","a")
thread1=Crawl(website)
thread1.start()
thread1.join()
i=0
while len(Pool)>1:
	while threading.activeCount()<10:
		a=Crawl(Pool[i])
		a.start()
		Pool[i]=None
		i+=1
