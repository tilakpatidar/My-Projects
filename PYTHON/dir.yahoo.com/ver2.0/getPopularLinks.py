from bs4 import BeautifulSoup
import re,os
from urlparse import urljoin
from urllib2 import urlopen
import time
start_time = time.time()
links=[]
length=0
count=-1
linksFromFiles=[]
def readLinks():
	# Open a file
	fo = open("crawl.txt", "r+")
	line = fo.read().split('\n')
	global length
	length=len(line)
	return line
def setProxy():
	import urllib2
	proxy_handler = urllib2.ProxyHandler()
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)


def getLinks(url):
	try:
		links_href=[]
		a=urlopen(str(url))
		a=a.read()
		soup = BeautifulSoup(a)
		links = soup.find("div", { "class" : "st" })
		soup = BeautifulSoup(str(links))
		links = soup.findAll("a")
		for a in links:
			links_href.append(a.attrs['href'])
		print links_href
		return links_href
	except Exception as e:
		print e
		return None
		

def cleanUp(parent,url):
	"""Cleans up url before adding to database"""
	#check for relative paths
	if not 'http' in str(url):
		url=urljoin(str(parent),str(url))
	#discarding results from dir.yahoo.com
	if 'dir.yahoo.com' in str(url):
		return ""
	#do not send file links for crawling
	fileName, fileExtension = os.path.splitext(str(url))
	if fileExtension!="":
		return ""
	#check for correct absolute paths
	#if not str(website) in str(url):
	#	return ""
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
	if obj is None:
		return
	#getting all anchor tags
	try:
		for a in obj:
			#getting clean links
			temp=cleanUp(url,a)
			if temp!="":
				if addLinks(temp):
					print temp
					print "--- %s seconds ---" %(time.time() - start_time)
		global count
		count+=1
		Crawl(str(linksFromFiles[count]))
	except Exception:
		#Raised when obj is None Type
		pass

#setProxy()
linksFromFiles=readLinks()
#print linksFromFiles
foo=open("crawlPopularLinks.txt","a")
count+=1
Crawl(linksFromFiles[count])

