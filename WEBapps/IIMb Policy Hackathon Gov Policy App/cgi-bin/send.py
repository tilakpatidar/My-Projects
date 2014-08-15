#!/usr/bin/python
import cgi, os,MySQLdb
import cgitb,urllib2
print "Content-Type: text/html\r\n\r\n"
#cgitb.enable()
form = cgi.FieldStorage()
pid=form.getvalue('pid')
a=urllib2.urlopen("http://www.srmsearchengine.in/gsa/c.py?q="+pid)

