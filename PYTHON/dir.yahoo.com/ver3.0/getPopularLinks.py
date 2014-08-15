import re,os
from bs4 import BeautifulSoup
from urlparse import urljoin
import time
import urllib2
start_time = time.time()
links=[]
website="http://dir.yahoo.com/"
oldPopularLinks=[]
fi=open("crawlPopularLinks.txt","a")

def addPopularLinks(url):
	"""gets popular links and adds them"""
	global oldPopularLinks
	a=urllib2.urlopen(str(url))
	a=a.read()
	soup = BeautifulSoup(a)
	links = soup.find("div", { "class" : "st" })
	soup = BeautifulSoup(str(links))
	links = soup.findAll("a")
	for a in links:
		if not a.attrs['href'] in oldPopularLinks:
			oldPopularLinks.append(a.attrs['href'])
			link=cleanPopularLink(url,a.attrs['href'])
			print link
			global fi
			fi.write(str(link)+"\n")
	

def cleanPopularLink(parent,url):
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
					addPopularLinks(temp)
					Crawl(str(temp))
	except Exception as a:
		#Raised when obj is None Type
		print a
		return

foo=open("crawl.txt","a")
Crawl(website)

