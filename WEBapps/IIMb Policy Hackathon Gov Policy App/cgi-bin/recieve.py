#!/usr/bin/python
import urllib2,cgi
import cgitb; cgitb.enable()
import re
page= urllib2.urlopen("http://srmsearchengine.in/gsa/b.py")
source = page.read()
content=re.findall('<p>(.*)</p>',source)[0]
tupl = eval(content)
#current id is 121
tupl=list(tupl)
xc=tupl
tupl=tupl[-1]
tupl=list(tupl)
print "Content-Type:text/html\r\n\r\n"
#print tupl
for i in tupl:
	if i=='x':
		print "1"
