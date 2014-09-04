import thread,threading,os,MySQLdb
from urlparse import urljoin
import time
from bs4 import BeautifulSoup
import urllib2
start_time = time.time()
def parser(f):
	def addDB(data):
		# Open database connection
		db = MySQLdb.connect("localhost","root","root","tester" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# Prepare SQL query to INSERT a record into the database.
		sql = """INSERT INTO dmozDump VALUES('%s','%s','%s','%s')"""%(str(MySQLdb.escape_string(data[0])),str(MySQLdb.escape_string(data[1])),str(MySQLdb.escape_string(data[2])),str(MySQLdb.escape_string(data[3])))
		try:
	   		# Execute the SQL command
			   cursor.execute(sql)
			   # Commit your changes in the database
			   db.commit()
		except:
		   # Rollback in case there is any error
		   db.rollback()

		# disconnect from server
		db.close()
	def parse(obj):
		try:
			for data in obj:
				url=data.attrs['about'].encode("UTF-8")#url
				title=str(data.find("d:title").contents[0].encode("UTF-8"))#title
				desc=str(data.find("d:description").contents[0].encode("UTF-8"))#desc
				topic=str(data.find("topic").contents[0].encode("UTF-8"))#topic
				t=(topic,url,title,desc)
				#print t
				addDB(t)
		except:
			pass

	def externalPages(code):

		#print "Parsing Now"
		soup = BeautifulSoup(code)
		exPage = soup.findAll("externalpage")
		return exPage
	foo=open(f)
	exPages=externalPages(str(foo.read()))
	parse(exPages)
	#print exPages
files=os.listdir("splits")
#print files
os.chdir("splits")
for f in files:
	parser(str(f))
