import Browser as b
people=[]
def parseResults():
	global people
	return people
def init(details):
	x=raw_input("is your facebook logged in? y/n")
	if x=="n":
		global people
		d=details.copy()
		del d["Keywords"]
		del d["Gender"]
		print "[INFO] Starting Fb Engine"
		source=b.open('https://www.facebook.com/search.php?q='+" ".join(d.values()))
		print "[INFO]Starting Parsing"
		from bs4 import BeautifulSoup as bs
		divs=bs(source).find("div",{"id":"pagelet_search_results"}).findAll("div",{"class":"clearfix"})
		print "[INFO] Found "+str(len(divs))+" profiles"
		i=1
		for d in divs:
			print "[INFO] Grabbing "+str(i)+" profile"
			try:
				temp={}
				#print d
				temp["name"]=d.find("div",{"class":"instant_search_title"}).text
				#temp["Institution"]=d.find("div",{"class":"q0a axa"}).text
				#temp["User_ids"]=d.find("a",{"class":"R9a Kra LXa AIa ob"})["href"].replace("/","")
				temp["images"]=d.find("img",{"class":"img"})["src"]
				temp["profile_url"]=d.find("div",{"class":"instant_search_title"}).find("a")["href"]
				temp["friends"]=[]
				temp["tags"]=[]
				#Trying to grab all basic info
				try:
		
					s=bs(str(d).replace("</"," </")).findAll("span",{"class":"fbProfileBylineFragment"})
					for ss in s:
						temp["tags"]=temp["tags"]+ss.text.lower().split()
					temp["tags"]=list(set([str(x) for x in list(set(temp["tags"]))]))
					print "[INFO] got some basic info for "+str(i)
				except:
					print "[INFO] no basic info for "+str(i)
			except:
				pass
			i+=1
			people.append(temp)
	elif x=="y":
		global people
		d=details.copy()
		del d["Keywords"]
		del d["Gender"]
		print "[INFO] Starting Fb Engine"
		from selenium import webdriver
		print "[INFO] Runnning Ghost !"
		print "[INFO] Ghost started !"
		driver = webdriver.Chrome("/home/tilak/chromedriver")
		driver.get("https://www.facebook.com/TilakPatidarBhopal")
		inputEmail = driver.find_element_by_id("email")
		inputEmail.send_keys("tilakpatidar@gmail.com")
		inputPass = driver.find_element_by_id("pass")
		inputPass.send_keys("hacker524891")
		inputPass.submit()
		inputQuery=driver.find_element_by_name("q")
		driver.get('https://www.facebook.com/search/str/'+" ".join(d.values())+'/keywords_users')
		print "[INFO]Starting Parsing"
		from bs4 import BeautifulSoup as bs
		source=driver.page_source
		divs=bs(source).findAll("div",{"class":"_3u1 _gli _ajr"})
		print "[INFO] Found "+str(len(divs))+" profiles"
		i=1
		for d in divs:
			print "[INFO] Grabbing "+str(i)+" profile"
			try:
				k=d.find("div",{"class":"_gll"})
				temp={}
				#print d
				temp["name"]=k.find("div",{"class":"_5d-5"}).text
				#temp["Institution"]=d.find("div",{"class":"q0a axa"}).text
				#temp["User_ids"]=d.find("a",{"class":"R9a Kra LXa AIa ob"})["href"].replace("/","")
				temp["images"]=d.find("img",{"class":"img"})["src"]
				temp["profile_url"]=k.find("a")["href"]
				if "profile.php" in temp["profile_url"]:
					print "[INFO] Cannot scrap the profile"
					continue
				print "herrree",temp["profile_url"]
				temp["friends"]=[]
				temp["tags"]=d.find("div",{"class":"_glo"}).text.split(" ")
				#Trying to grab all basic info
			except Exception as e:
				print e
			try:
				if "?" in temp["profile_url"]:
					temp["profile_url"]=temp["profile_url"].split("?")[0]
					driver.get(temp["profile_url"]+"/friends")
				else:
					driver.get(temp["profile_url"]+"/friends")
				li=bs(driver.page_source).findAll("li",{"class":"_698"})
				for l in li:
					t={}
					t["profile"]=str(l.find("div",{"class":"fsl fwb fcb"}).find("a")["href"])
					t["name"]=str(l.find("div",{"class":"fsl fwb fcb"}).find("a").text).split("?")[0]
					temp["friends"].append(t)
			except:
				pass
			try:
				misc={}
				if "?" in temp["profile_url"]:
					temp["profile_url"]=temp["profile_url"].split("?")[0]
					driver.get(temp["profile_url"]+"/about?section=contact-info")
				else:
					driver.get(temp["profile_url"]+"/about?section=contact-info")
				li=bs(driver.page_source).findAll("li",{"class":"_3pw9 _2pi4 _2ge8"})
				for l in li:
					t=l.findAll("span")
					da=t[1].text
					try:
						if da.lower().index("ask")>=0:
							if not temp.has_key("misc"):
								temp["misc"]={}
					except Exception as e:
						misc[t[0].text.lower().strip()]=da
					temp["misc"]=misc
			except Exception as e:
				print e
				temp["misc"]={}
			i+=1
			people.append(temp)
def insertData():
	import MySQLdb
	for p in people:
		if not p.has_key("misc"):
			p["misc"]={}
		# Open database connection
		db = MySQLdb.connect("localhost","root","1","people" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		sql="INSERT IGNORE into facebook VALUES('%s','%s','%s','%s','%s','%s')"%(MySQLdb.escape_string(str(p["profile_url"]).replace("u'","'")),MySQLdb.escape_string(str(p["images"]).replace("u'","'")),MySQLdb.escape_string(str(p["name"]).replace("u'","'")),MySQLdb.escape_string(str(p["tags"]).replace("u'","'")),MySQLdb.escape_string(str(p["friends"]).replace("u'","'")),MySQLdb.escape_string(str(p["misc"])))
		# Execute the SQL command
		#print sql
		cursor.execute(sql)
		db.commit()
		db.close()
	
