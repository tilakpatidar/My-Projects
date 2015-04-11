import Browser as b
people=[]
def parseResults():
	global people
	return people
def init(details):
	global people
	d=details.copy()
	del d["Keywords"]
	del d["Gender"]
	print "[INFO] Starting Twitter Engine"
	source=b.open('https://twitter.com/search?q='+" ".join(d.values())+'&src=typd&mode=users')
	print "[INFO]Starting Parsing"
	from bs4 import BeautifulSoup as bs
	#source=open("googleDummy","r").read()
	div=bs(source).find("ol",{"class":"stream-items js-navigable-stream"})
	divs=div.findAll("li")
	print "[INFO] Found "+str(len(divs))+" profiles"
	i=1
	for d in divs:
		print "[INFO] Grabbing "+str(i)+" profile"
		temp={}
		temp["name"]=d.find("strong",{"class":"fullname js-action-profile-name"}).text
		temp["info"]=d.find("p",{"class":"bio "}).text
		temp["twitter_name"]=str(filter(lambda x:ord(x)>31 and ord(x)<128,d.find("span",{"class":"username js-action-profile-name"}).text))
		temp["image"]=d.find("img")["src"]
		temp["profile_url"]="https://twitter.com/"+temp["twitter_name"].replace("@","")
		i+=1
		people.append(temp)
def insertData():
	import MySQLdb
	for p in people:
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","people" )
		try:
			print p
			# prepare a cursor object using cursor() method
			cursor = db.cursor()
			# execute SQL query using execute() method.
			sql="INSERT into twitter VALUES('%s','%s','%s','%s','%s')"%(MySQLdb.escape_string(str(p["twitter_name"])),MySQLdb.escape_string(str(p["profile_url"])),MySQLdb.escape_string(str(p["name"])),MySQLdb.escape_string(str(p["info"])),MySQLdb.escape_string(str(p["image"])))
			# Execute the SQL command
			#print sql
			cursor.execute(sql)
			db.commit()
		except Exception as e:
			db.rollback()
			print e
			print "Something Went Wrong"
		db.close()
