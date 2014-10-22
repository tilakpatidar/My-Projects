import temp,MySQLdb
from multiprocessing import Pool
t="Infobox Officeholder"
def removeEmptyKeys(d):
        return dict((k, v) for k, v in d.iteritems() if v)
def fetch(olim,nlim):
	res=[]
	# Open database connection
	db = MySQLdb.connect("localhost","root","song","wiki")
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = "SELECT id,title,text from xmlDump LIMIT %s,%s"%(olim,nlim)
	# Execute the SQL command
	cursor.execute(sql)
	# Fetch all the rows in a list of lists.
	results = cursor.fetchall()
	for row in results:
	   id = row[0]
	   title = row[1]
	   text = row[2]
	   res.append((id,title,text))
	# disconnect from server
	db.close()
	return res
def main(li):
	def getBox(src):
		return temp.__getTemplate(t,src)
        def setBox(d):
                # Open database connection
                db = MySQLdb.connect("localhost","root","song","wiki" )
                # prepare a cursor object using cursor() method
                cursor = db.cursor()
                # Prepare SQL query to INSERT a record into the database.
                sql = """INSERT INTO smartAns VALUES('%s','%s','%s')"""%(MySQLdb.escape_string(str(li[0])),MySQLdb.escape_string(str(li[1])),MySQLdb.escape_string(str(d)))
                #print sql
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
	dic=getBox(li[2])
	if not dic is None:
	      dic=removeEmptyKeys(dic)
	      setBox(str(dic))
	#print dic
i=0
j=20
while i<13042546:
      try:
	p = Pool(20)
	l=fetch(i,j)
	p.map(main,l)
	i+=20
	j+=20
        print i,j
      except Exception as e:
        print e
        continue
