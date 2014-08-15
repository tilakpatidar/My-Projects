import thread,threading,re,os
from urlparse import urljoin
import time
import urllib2
start_time = time.time()
links=[]
website="http://dir.yahoo.com/"


def setProxy():
	import urllib2
	proxy_handler = urllib2.ProxyHandler()
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)


def getLinks(url):
	try:
		html = urllib2.urlopen(str(url))
		links=re.findall('<a href="?\'?([^"\'>]*)',str(html.read()))
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
	return url



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
						ab=Crawl(str(temp))
						ab.start()
						print "--- %s seconds ---" %(time.time() - start_time)
		except TypeError:
			#Raised when obj is None Type
			pass

#setProxy()
foo=open("crawl.txt","a")
thread1=Crawl(website)
thread1.start()

