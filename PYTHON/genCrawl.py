import threading
website="http://www.kubuntu.com/"
Pool=[]
links=[]
def setProxy():
	import urllib2
	proxy_handler = urllib2.ProxyHandler({'http':'172.16.0.19:8080'})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)


def getLinks(url):
	try:
		t=[]
		from bs4 import BeautifulSoup
		import urllib2
		html = urllib2.urlopen(str(url))
		temp=html.read()
		soup=BeautifulSoup(temp)
		links=soup.findAll("a")
		for l in links:
			t.append(l['href'])
		return t
	except Exception as e:
		print e
		return None
		

def cleanUp(parent,url):
	from urlparse import urljoin
	import os
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
def addLinks(b):
	import threading
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

def Crawl(url):
	"""Run method of the thread"""
	import threading
	obj=getLinks(url)
	if obj is None:
		return
	#getting all anchor tags
	for a in obj:
		#getting clean links
		temp=cleanUp(url,a)
		if temp!="":
			if addLinks(temp):
				print temp
				#first creating a lock
				try:
					lock1 = threading.Lock()
					lock1.acquire()
				except:
					#if lock is unsuccessfull return
					return
				try:
					Pool.append(str(temp))
					lock1.release()
				except:
					lock1.release()

setProxy()#Comment it if no proxy
foo=open("Links.txt","a")
Crawl(website)
i=0
while True:
	while threading.activeCount()<20:
		try:
			a=threading.Thread(target=Crawl,args=(Pool[i],))
			a.start()
			i+=1
		except IndexError:
			Crawl(website)
			continue
		
