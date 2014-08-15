#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
form=cgi.FieldStorage()
cx=form.getvalue('q')
x= urllib2.urlopen("http://srmsearchengine.in/gsa/c.py?q="+str(ls[0])+"&r=x&s=&t=&u=")  
import urllib2
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
for i in list(tupl):
 if i=="":
  tupl.remove(i)
#print tupl
ls=len(tupl)
while(ls<5):
 page= urllib2.urlopen("http://srmsearchengine.in/gsa/b.py")
 source = page.read()
 content=re.findall('<p>(.*)</p>',source)[0]
 tupl = eval(content)
#current id is 121
 tupl=list(tupl)
 xc=tupl
 tupl=tupl[-1]
 tupl=list(tupl)
 for i in list(tupl):
  if i=="":
   tupl.remove(i)
#print tupl
 ls=len(tupl)
print "Content-Type: text/html\r\n\r\n"
print "done" 
 
