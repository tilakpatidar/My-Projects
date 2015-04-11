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
	print "[INFO] Starting Google+ Engine"
	source=b.open('https://plus.google.com/s/'+" ".join(d.values())+'/people')
	print "[INFO]Starting Parsing"
	from bs4 import BeautifulSoup as bs
	#source=open("googleDummy","r").read()
	divs=bs(source).findAll("div",{"class":"Osd Hfb"})
	print "[INFO] Found "+str(len(divs))+" profiles"
	i=1
	for d in divs:
		print "[INFO] Grabbing "+str(i)+" profile"
		temp={}
		temp["name"]=d.find("a",{"class":"R9a Kra LXa AIa ob"}).text
		temp["institution"]=d.find("div",{"class":"q0a axa"}).text
		temp["user_ids"]=d.find("a",{"class":"R9a Kra LXa AIa ob"})["href"].replace("/","")
		temp["images"]=d.find("img",{"class":"we"})["src"]
		temp["profile_url"]="https://plus.google.com/"+temp["user_ids"]
		abt_us=b.open(temp["profile_url"]+"/about")
		abt_us=str(filter(lambda x:ord(x)>31 and ord(x)<128,abt_us))
		temp["friends"]=[]
		temp["tags"]=[]
		#Trying to grab friends
		try:
			t=abt_us.split("ob tv Ub")[1:]
			v=t[len(t)-1]
			index=t[len(t)-1].find("</a>")
			t.pop()
			d=''.join(t)+v[:index]
			a=bs(d)
			aas=[]
			a=a.findAll("div",{"class":"KfV4Rd Zqc"})
			for j in a:
				aas.append(j.find("a").text)
			temp["friends"]=list(set(aas))
			print "[INFO] got friends for "+str(i)
		except:
			print "[INFO] no friends for "+str(i)+" what a looner"
		#Trying to grab all basic info
		try:
		
			s=bs(abt_us.replace("</"," </")).findAll("div",{"class":"Uia"})
			for ss in s:
				temp["tags"]=temp["tags"]+ss.text.lower().split()
			temp["tags"]=[str(x).strip() for x in list(set(temp["tags"]))]
			temp["email"]=""
			temp["mobile"]=""
			if temp["tags"].index("male")>=0:
				temp["gender"]="male"
			elif temp["tags"].index("female")>=0:
				temp["gender"]="female"
			import re
			for f in temp["tags"]:
				if len(re.findall(".*@.*",f))>=1:
					temp["email"]=f
				if len(re.findall("\d{10}",f))>=1:
					temp["mobile"]=f
			print "[INFO] got some basic info for "+str(i)
		except Exception as e:
			print e
			print "[INFO] no basic info for "+str(i)
		
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
			sql="INSERT into google VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(MySQLdb.escape_string(str(p["user_ids"])),MySQLdb.escape_string(str(p["name"])),MySQLdb.escape_string(str(p["tags"])),MySQLdb.escape_string(str(p["images"])),MySQLdb.escape_string(str(p["profile_url"])),MySQLdb.escape_string(str(p["institution"])),MySQLdb.escape_string(str(p["gender"])),MySQLdb.escape_string(str(p["mobile"])),MySQLdb.escape_string(str(p["email"])),MySQLdb.escape_string(str(p["friends"])))
			# Execute the SQL command
			#print sql
			cursor.execute(sql)
			db.commit()
		except Exception as e:
			db.rollback()
			print e
			print "Something Went Wrong"
		db.close()
