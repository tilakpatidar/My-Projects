import MySQLdb
bigDict={}
def store(key,terms):
	try:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","tester" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		sql="INSERT into treeDMOZ VALUES('%s','%s')"%(MySQLdb.escape_string(key),MySQLdb.escape_string(str(terms)[2:]))
		# Execute the SQL command
		cursor.execute(sql)
		db.commit()
	except Exception as e:
		db.rollback()
		print e
		print "Something Went Wrong"
	db.close()
def fetch():
	try:
		# Open database connection
		db0 = MySQLdb.connect("localhost","root","1","tester" )
		# prepare a cursor object using cursor() method
		cursor0 = db0.cursor()
		# execute SQL query using execute() method.
		sql0="SELECT DISTINCT(topic) from dmozDump"
		# Execute the SQL command
		cursor0.execute(sql0)
		results0=cursor0.fetchall()
		if not results0 is None:
			return results0
	except Exception as e:
		print e
		print "Something Went Wrong"
	db0.close()
urlList=fetch()
newurlList=[]
for i in urlList:
	for j in i:
		#j=j.replace('http://dir.yahoo.com/','')
		j=j.replace('Top','')
		terms=j.split('/')
		try:
			terms.remove('?o=a')
		except:
			pass
		for t in terms:
			key=str(t)
			if bigDict.has_key(key):
				existTerms=str(bigDict[key]).split(',')
				for t1 in terms:
					if t1==key:
						continue
					else:
						if not existTerms.__contains__(t1):
							bigDict[key]=bigDict[key]+','+t1
			else:
				newTerms=""
				for t2 in terms:
					if t2==key:
						continue
					else:
						newTerms=newTerms+','+str(t2)
				bigDict[key]=newTerms
t=bigDict.items()
for i in t:
	key=i[0]
	terms=i[1]
	store(i[0],i[1])
