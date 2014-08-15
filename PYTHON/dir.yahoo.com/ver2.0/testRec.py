import re,os
from bs4 import BeautifulSoup
from urlparse import urljoin
from urllib2 import urlopen
import time
start_time = time.time()
links=[]
website="http://dir.yahoo.com/Arts"

def getLinks(url):
	try:
		html = urlopen(str(url))
		html=html.read()
		links=re.findall('<a href="?\'?([^"\'>]*)',str(html))
		base=re.findall('<base href="?\'?([^"\'>]*)',str(html))
		for i,a in enumerate(links):
			if not 'http' in a:
				if not base:
					base[0]="//dir.yahoo.com"
				links[i]="http:"+urljoin(base[0],a)
		return links
	except Exception as e:
		print e
		

def cleanUp(parent,url):
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



def addLinks(b):
	"""Adds url and returns True to continue to dwnld"""
	try:
		global links
		global foo
		if not str(b) in links:
			links.append(str(b))
			foo.write(str(b)+"\n")
			return True
		return False
	except:
		return False

def Crawl(url):
	obj=getLinks(url)
	#getting all anchor tags
	try:
		for a in obj:
			#getting clean links
			temp=cleanUp(url,a)
			if temp!="":
				if addLinks(temp):
					print temp
					print "--- %s seconds ---" %(time.time() - start_time)
					Crawl(str(temp))
	except Exception as a:
		print a
		return

foo=open("crawl.txt","a")
Crawl(website)

