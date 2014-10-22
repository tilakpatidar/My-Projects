def psplit(body,num):
    body=list(body.lower().split())
    d=[]
    for word in body:
        if (body.index(word)!=len(body)-num):
            for i in xrange(1,3):
                kword=str(" ".join(body[body.index(word):body.index(word)+i]).lower())
                if len(kword)<31:
                    if kword not in d:
                        d.append(kword)
        else:
            kword=word           
            if len(kword)<31:
                if kword not in d:
                    d.append(kword)
    return d



def m3(line):
    extrakey=line.replace(" ","")
    import MySQLdb
    import time
    test=set()
    db=MySQLdb.connect("localhost","root","song","SRMSE")
    cursor=db.cursor()
    st=time.time()
    comb=psplit(line,2)
    sql="SELECT `map` FROM `wordtable3` WHERE `keyword`='%s'"%extrakey
    cursor.execute(sql)
    try:
       second=cursor.fetchone()[0]
    except:
       second=""
    sql="SELECT `map` FROM `wordtable3` WHERE `keyword`='%s'"%comb[0]
    cursor.execute(sql)
    ans=cursor.fetchone()
    #print second
    if ans:
        ans=set(ans[0].split(','))
        comb=comb[1:]
	print comb
    else:
	return second
    for part in comb:
        sql="SELECT `map` FROM `wordtable3` WHERE `keyword`='%s'"%part
        cursor.execute(sql)
        b=cursor.fetchone()
        if not ans:
            return second
        else:
            if b:
                ans=set(ans&set(b[0].split(',')))
            else:
                return second
    if len(list(ans))>1:
	 print len(list(ans))
	 return list(ans)
    else:
	 return second    

def m2(line):
	import MySQLdb
	import time as t
	db=MySQLdb.connect("localhost","root","song","SRMSE")
	cur=db.cursor()
	st=t.time()
	lis=psplit(line,2)
	ans=[]
	ans2=[]
	for s in lis:
		try:
			sql="select map from wordtable2 where keyword='%s'"%(s)
			cur.execute(sql)
			b=cur.fetchone()
			#print s,b
			if ' ' in s:
				if len(s.split())==2:
					ans2.append(set(b[0].split(',')))
			
			ans.append(set(b[0].split(',')))
		except Exception:
			abd=0
	

	try:
		
		"""ans3=[]
		i=0

		while i<len(ans2):
			j=i+1
			while j<len(ans2):

				ans3.append(ans[i]&ans[j])
				j+=1
			i+=1
		"""	
		if len(ans2)==0:
			ans=set.intersection(*ans)
		else:		
			ans3=set.intersection(*ans2)
			ans=set.intersection(*ans)
			ans=ans&ans3
		
	except Exception:
		ans=set()
	print t.time()-st
	return list(ans)


def m1(line):
	import MySQLdb
	import time as t
	db=MySQLdb.connect("localhost","root","song","SRMSE")
	cur=db.cursor()
	st=t.time()
	lis=psplit(line,1)
	ans=[]
	ans2=[]
	for s in lis:
		try:
			sql="select map from wordtable1 where keyword='%s'"%(s)
			cur.execute(sql)
			b=cur.fetchone()
			#print s,b
			if ' ' in s:
				if len(s.split())==2:
					ans2.append(set(b[0].split(',')))
			
			ans.append(set(b[0].split(',')))
		except Exception:
			abd=0
	

	try:
		
		"""ans3=[]
		i=0
		while i<len(ans2):
			j=i+1
			while j<len(ans2):
				ans3.append(ans[i]&ans[j])
				j+=1
			i+=1
		"""	
		if len(ans2)==0:
			ans=set.intersection(*ans)
		else:		
			ans3=set.intersection(*ans2)
			ans=set.intersection(*ans)
			ans=ans&ans3
		
	except Exception:
		ans=set()
	print t.time()-st
	return list(ans)



def m20(line):
    comb=psplit(line,2)
    print comb

