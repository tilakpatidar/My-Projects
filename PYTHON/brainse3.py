
def submain():
	  import threading
	  import threading
	  import Queue
	  result = Queue.Queue()
	  import brainse3
	  brainse3.proxnull()
	  toc=[]
	  toc =brainse3.seed()
	  toc=toc[2000:]
	  for url in toc:
              try:
                  thread.start_new_thread(brainse3.gt,(url,))
              except Exception as a:
                  print a               
        


def cont(link):
	"""Returns html code from a webpage url"""
	import urllib2
	try:
		content=urllib2.urlopen(link).read()
	except urllib2.HTTPError, err:
		content="<h1> </h1>"
		return content
	except ValueError:
		content=" <h1> </h1>"
		return content
	except AttributeError:
		content=" <h1> </h1>"
		return content
	except urllib2.URLError:
		content="<h1> </h1>"
	except NameError:
		content=" <h1> </h1>"
		return content

	except Exception:
		content="<h1> </h1>"
		return content
	else:
		content=urllib2.urlopen(link).read()
		return content


def links(url):
        #print url
        import brainse3
	content=brainse3.cont(url)
	#print content
	linkse=[]
	import MySQLdb
	db=MySQLdb.connect(user="root",passwd="brainse110412BRAINSE",db="tester")
	cur=db.cursor()
	while content:
		#finding <a> tags
		x=content.find('<a href=')
		start=content.find('"',x)
		stop=content.find('"',start+1)
		link=content[start+1:stop]
		#print link
		try:
                    if link[0]=='/':
			#making relative links absolute
                        link=url+link[1:]
                                                    
		except IndexError:
                    break
		else:
                    if check(link):
                        linkse.append(link)
                        print link
		content=content[stop:]
	return linkse
	
def grabdata(url):
        title=""
	from bs4 import BeautifulSoup
	import brainse3
	c=brainse3.cont(url)
	try:
            soup=BeautifulSoup(str(c))
        except Exception:
            soup=" "
        else:
            soup=BeautifulSoup(str(c))
	
	try:
                
		ter= soup.find("meta", {"name":"description"})['content']
		  
	except TypeError:
		try:
		    ter= soup.find("meta", {"name":"Description"})['content']
	        except TypeError:
		    ter=" "
		else:
			ter= soup.find("meta", {"name":"Description"})['content']
	except UnicodeEncodeError:
		ter=" "
	except  Exception:
                ter=" "
	else:
                soup=BeautifulSoup(str(c))
		ter= soup.find("meta", {"name":"description"})['content']
					    
	try:
	    tit=soup.title.string
	except TypeError:
		t=" "
    
	except UnicodeEncodeError:
		t=" "
	except AttributeError:
		t= " "
	except Exception:
                t= " "
	else:
	    title=soup.title.string	
	if title:
		para=title+"|"+ ter
	else:
		if ter==" ":
			para = " "
		else:
			para=ter+"|"
	try:
            for node in soup.findAll('p'):
                para=para+''.join(node.findAll(text=True))
        except Exception:
            para=" "
        else:
            for node in soup.findAll('p'):
                para=para+''.join(node.findAll(text=True))
            
	para = para.replace("\n", "")
	para = para.replace("\t", "")
	para = para.replace("\a", "")
	para = para.replace("\r", "")
	para = " ".join(para.split())
	return para,title

def addlinkse(linkse):
    import MySQLdb
    db=MySQLdb.connect(user="root",passwd="brainse110412BRAINSE",db="tester")
    cur=db.cursor()
    for link in linkse:
        try:
            cur.execute("""INSERT INTO link VALUES (%s)""",(link))
            db.commit()
	except:
            db.rollback()
	else:
            cur.execute("""INSERT INTO link VALUES (%s)""",(link))
            db.commit()
    db.close()
        
def submitToServer(url,title,para,keys):
		import urllib,urllib2,brainse3,MySQLdb
		#res=
		import MySQLdb
		db=MySQLdb.connect(user="root",passwd="brainse110412BRAINSE",db="tester")
		cur=db.cursor()
		x=brainse3.rem(url)
		y=brainse3.rem(title)
		z=brainse3.rem(para)
		za=brainse3.rem(keys)
		qw='1'
		try:
                        print "inside SUBMITserver"
                        cur.execute("""INSERT INTO poter VALUES (%s,%s,%s,%s)""",(x,y,z,za))
			db.commit()
			print "inserted into pot"         
                        kkeys = za.split("|")
			for table in kkeys:
				cur.execute("SELECT * FROM information_schema.tables WHERE table_name='%s'" % (table))
				a=cur.fetchone()
				if a:
                                    	cur.execute("INSERT INTO %s(url,para,title,bl) VALUES('%s', '%s', '%s' , 1)" % (table,x, y, z))	
				else:
                                        
                                        print "near creation"
					cur.execute("CREATE TABLE IF NOT EXISTS %s (url VARCHAR(100),para VARCHAR(100),title VARCHAR(100),bl INT,PRIMARY KEY(url))" % (table) )
                                        print "new table created"
			                cur.execute("INSERT INTO %s(url,para,title,bl) VALUES('%s', '%s', '%s' , 1)" % (table,x, y, z))	
 
			
		except:
			db.rollback()
			print "failed to insert values "
		
                   
                    
                        
                db.close()


def rem(z):
		z=z.lower()
		return "".join(filter(lambda x: ord(x)<128, z))

def seed():
		x = open ("seed.txt", "r")
		data=x.read()
		m=data.split("http")
		c=[]
		for u in m:
			c.append("http"+u)
		xd=[]
		xd = c[1:]
		return xd

def a2f(c,name):
		t = open(name, "w")
		str = '\n'.join
		t.write('str')
		print "done"
		
def nl(content):
	linkse=[]
	while content:
		x=content.find('<a href=')
		start=content.find('"',x)
		stop=content.find('"',start+1)
		link=content[start+1:stop]
		print link
		if link[0]=='/':
			link="test"+link
			linkse.append(link)
		else:
			linkse.append(link)
		content=content[stop:]
	return linkse

def gla(para):
	title = ""
	url=""
	discs = ["what ","when ","who ","where ","how "," the "," a "," up "," that "," is ","copyright","rights","copy","copyrights","all rights reserved","reserved"," he "," for "," it "," his "," on "," be "," at "," by "," i "," this "," had "," not "," are "," from "," have "," an "," they "," which "," were "," you "," all "," her "," she "," there "," would "," their "," we "," him "," been "," has "," when "," who "," will "," no "," more "," its "," so "," said "," what "," about "," than "," can "," only "," other "," some "," could "," these "," first "," then "," do "," any "," my "," now "," such "," our "," me "," even "," most "," also "," well "," did "," many "," must "," back "," much "," where "," your "," way "," should "," each "," just "," those "," to "," too "," how "," mr "," very "," still "," get "," here "," never "," know "," while "," us "," himself "," however "," dont "," something "," yet "," why "," given "," among "," john "," things "," thing "," seemed "," although "," perhaps "," itself "," whether "," either "," quite "," taken "," anything "," having "," im "," really "," already "," sure "," themselves "," together "," known "," probably "," whose "," became "," am "," nor "," finally "," kept "," thats ", " against " ," ones "," else "," couldnt "," cant "," simply "," actually "," shown "," indeed "," wasnt "," youre "," ready "," lot "," whom "," yes "," neither "," showed "," throughout "," anyone "," try "," according "," remember "," comes "," maybe "," myself "," wouldnt "," based "," somewhat "," apparently "," herself "," hes "," ive "," oh "," gives "," whatever "," theres "," after"," and "," as "," because "," before "," between "," both "," but "," case "," especially "," if "," in "," into "," like "," made "," make "," of "," or "," order "," over "," particularly "," per "," them "," therefore "," through "," thus "," under "," was "," with "]
	#feel free to add more words in the gla	
	quest=para.lower()
	quest = " " + quest
	i=0
	j=0
	remlist = ['"', "'", "?", '.', "!", ",", ":", ";","-","|",'0','1','_','2','3','4','5','6','7','8','9','$','%','&','*','']
	#remove special characters
	while (i<len(remlist)):
		quest=quest.replace(remlist[i],"")
		i = i+1
		
	#remove discarders
	i=0
	while (i<len(discs)):
		quest=quest.replace(discs[i]," ")
		i = i+1
		qnext = quest[1:].split(" ")
		qlast = []
	#remove repititions
	while (j<len(qnext)):
		if (qlast.count(qnext[j]) < 1):
			qlast.append(qnext[j])
		j = j+1
	str = "|"
	key= str.join(qlast[0:11])
	#u may need to remove that 0:11 part in order to get more key words	
	#keyin = ukey(url)
        #key = keyin+"|"+key
	# the string "key" can probably be ur desired target
	if title:
		return key
	else:
            asa=key.split("|")
            try:
                title=asa[0]+asa[1]+asa[2]
            except IndexError:
                import brainse3
		#title = brainse3.ukey(url)
		#title =""
	    else:
                title=asa[0]+asa[1]+asa[2]
	return key.replace("|"," ")
		
def proxnull():
    import urllib2
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    print "Proxy settings edited as requested by brainse3-bot"


def addproxy(a):
    import urllib2
    proxy_handler = urllib2.ProxyHandler({'http':a})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    print "Proxy settings edited as requested by brainse3-bot"	

def check(link):
	if link[0]=='h' and link[1]=='t' and link[2]=='t' and link[3]=='p':
			return True

def ukey(url):
	var=url.split('.')
	if(url[7:10]=='www'):
		return var[1]
	else:
		qar=var[0].split('//')
		return qar[1]
		
def gt(url):
    import brainse3
    print "jack sparrow"
    linkse= brainse3.links(url)
    para,title=brainse3.grabdata(url)
    keys,title=brainse3.gla(para,title,url)
    brainse3.submitToServer(url,title,para,keys)
	
def linkex(url):
    res=[]
    import brainse3
    import re
    ke=re.findall(r'http:\/\/(?:www\.)?([a-z0-9\-]+)(?:\.[a-z\.]+[\/]?).*',url)
    ke=str(ke)
    if url[-1]!="/":
        url=url+"/"
    s=brainse3.cont(url)
    try:
        links = re.findall(r'href=[\'"]?([^\'" >]+)', s)
        links = str(links)
    except Exception:
        print ""
    else:
        seplinks=links.split(",")
    
    for i in seplinks:
        i=str(i)
        print i
        xc=re.findall(r'http:\/\/(?:www\.)?([a-z0-9\-]+)(?:\.[a-z\.]+[\/]?).*',i) or re.findall(r'https:\/\/(?:www\.)?([a-z0-9\-]+)(?:\.[a-z\.]+[\/]?).*',i) or re.findall(r'www\.?([a-z0-9\-]+)(?:\.[a-z\.]+[\/]?).*',i)
        if xc or len(i.split("."))>2 or "[" in i or "]" in i or "com" in i or "?src" in i or "http" in i or "facebook" in i or "twitter" in i or len(url+i)>120 or "#" in i or "?" in i:
            continue       
        else:
            i=i.replace("'","")
            i=i.strip()
            po=brainse3.lufix(url,i)
            if po not in res:
                print "sdsdsdsdsdsdsdsdsd"
                if dubex(po)==True:
                    res.append(po)
    print len(res)
    return res

def linkexfull(url):
    print "in linkfull"
    seed=[]
    reter=fin=linkex(url)
    print len(reter)
    while(len(fin)>1):
        print "in linkfull loop"
        url=fin.pop()
        if url not in seed:
            print "in linkfull appending"
            seed.append(url)
        else:
            continue
        fin=fin+linkex(url)
        fin=list(set(fin))
        reter=reter+fin
        import brainse3
        reter=list(set(reter))
 	f=open("wertyu.txt",'a')
        for item in reter:
               f.write("%s\n" % item)
                



def urlfix(url):
            if url[-1]!="/":
                url=url+"/"
	    wt=url.split("/")
            w=wt[-1]
            e=w.split(".")
            if len(e)>1:
                wt=wt[:-1]
                url="/".join(wt)
            if url[-1]!="/":
		url=url+"/"
            return url


def lufix(url,i):
        if i[0]=="/":
            i=i[1:]
        try:
            if i[-1]=="/":
                i=i[:-1]
        except IndexError:
            print ""
        else:
            dfdf=2
                       #need to check the function as im not sure whether it will work for folders with a same name
	er=i.split("/")
	import brainse3
	tr=url.split("/")
	iu=tr[-1]
	iusp=iu.split(".")
	if len(iusp)>1:
            wq=tr[:-1]
            url="/".join(wq)
        else:
            wq=tr
	for o in er:
		if o in wq:
			pos=wq.index(o)
			wq=wq[:pos]
			print pos
			print url
			url="/".join(wq)
			#print url
			break
	
	url=brainse3.urlfix(url)
	url=str(url)
	i=str(i)
	return url+i

def lamp(para):
	discs = ["what ","when ","who ","where ","how "," the "," a "," up "," that "," is ","copyright","rights","copy","copyrights","all rights reserved","reserved"," he "," for "," it "," his "," on "," be "," at "," by "," i "," this "," had "," not "," are "," from "," have "," an "," they "," which "," were "," you "," all "," her "," she "," there "," would "," their "," we "," him "," been "," has "," when "," who "," will "," no "," more "," its "," so "," said "," what "," about "," than "," can "," only "," other "," some "," could "," these "," first "," then "," do "," any "," my "," now "," such "," our "," me "," even "," most "," also "," well "," did "," many "," must "," back "," much "," where "," your "," way "," should "," each "," just "," those "," to "," too "," how "," mr "," very "," still "," get "," here "," never "," know "," while "," us "," himself "," however "," dont "," something "," yet "," why "," given "," among "," john "," things "," thing "," seemed "," although "," perhaps "," itself "," whether "," either "," quite "," taken "," anything "," having "," im "," really "," already "," sure "," themselves "," together "," known "," probably "," whose "," became "," am "," nor "," finally "," kept "," thats ", " against " ," ones "," else "," couldnt "," cant "," simply "," actually "," shown "," indeed "," wasnt "," youre "," ready "," lot "," whom "," yes "," neither "," showed "," throughout "," anyone "," try "," according "," remember "," comes "," maybe "," myself "," wouldnt "," based "," somewhat "," apparently "," herself "," hes "," ive "," oh "," gives "," whatever "," theres "," after"," and "," as "," because "," before "," between "," both "," but "," case "," especially "," if "," in "," into "," like "," made "," make "," of "," or "," order "," over "," particularly "," per "," them "," therefore "," through "," thus "," under "," was "," with "]
	#feel free to add more words in the gla	
	quest=para.lower()
	quest = " " + quest
	i=0
	j=0
	remlist = ['"', "'", "?", '.', "!", ",", ":", ";","-","|",'0','1','_','2','3','4','5','6','7','8','9','$','%','&','*','']
	#remove special characters
	while (i<len(remlist)):
		quest=quest.replace(remlist[i],"")
		i = i+1
		
	#remove discarders
	i=0
	while (i<len(discs)):
		quest=quest.replace(discs[i]," ")
		i = i+1
		qnext = quest[1:].split(" ")
		qlast = []
	#remove repititions
	while (j<len(qnext)):
		if (qlast.count(qnext[j]) < 1):
			qlast.append(qnext[j])
		j = j+1
	str = "|"
	key= str.join(qlast[0:11])
	return key


def dubex(i):
	flag=0
	qw=i.split("/")
	for oi in qw:
		if len(oi.split("."))>1:
			flag=flag+1
			print flag
			continue
		#or "|" in i or "(" in i or ":" in i or "~" in i or "&" in i or "%" in i or "^" in i or "`" in i or "," in i	
	if flag>1 or "|" in i or "?" in i or ":" in i:
		return False
	else:
		return True
