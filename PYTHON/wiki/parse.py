import os,MySQLdb
from multiprocessing import Pool
from urlparse import urljoin
import time
from bs4 import BeautifulSoup
import urllib2
start_time = time.time()
print "Do not exit running . . ."
def parser(f):
	def addDB(data):
		# Open database connection
		db = MySQLdb.connect("localhost","root","song","wiki" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# Prepare SQL query to INSERT a record into the database.
		sql = """INSERT INTO xmlDump(`id`,`url`,`title`,`text`) VALUES(concat('102',values(id)),'%s','%s','%s')"""%(str(MySQLdb.escape_string(data[0])),str(MySQLdb.escape_string(data[1])),str(MySQLdb.escape_string(data[2])))
		try:
	   		# Execute the SQL command
			   cursor.execute(sql)
			   # Commit your changes in the database
			   db.commit()
		except Exception as e:
		   # Rollback in case there is any error
		   db.rollback()
		   print e

		# disconnect from server
		db.close()
	def parse(obj):
		try:
			for data in obj:
				try:
				  title=str(data.find("title").contents[0].encode("UTF-8"))#title
				  url=str("http://en.wikipedia.org/wiki/"+title).encode("UTF-8")#url
				  desc=str(data.find("text").contents[0].encode("UTF-8"))#desc
				  #print url
				  t=(url,title,desc)
				  #print t
				  addDB(t)
                                except:
                                  continue
		except Exception as e:
			print e

	def externalPages(code):
		soup = BeautifulSoup(code)
		exPage = soup.findAll("page")
		#print exPage
		return exPage
        if not os.path.isdir(f):
	 foo=open(f)
	 exPages=externalPages(str(foo.read()))
	 parse(exPages)
         t="mv ./"+f+" ./done/"
         print t
         os.system(t)
	 #print exPages
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]
files=os.listdir(".")
print len(files)
p = Pool(processes=50)
p.map(parser,files)
p.join()
