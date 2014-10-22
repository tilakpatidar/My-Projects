def checkScheme(u):
	"""Checks the scheme part of url like http or https"""
	#Special Cases first
	if u.find('http')==0:
		if u.find('https')==0:
			temp=u.replace('https','',1)
			if temp.find(':')==0:
				temp=temp.replace(':','',1)
				if temp.find('/')==0:
					temp=temp.replace('/','',1)
					if temp.find('/')==0:
						return u
					else:
						return u.replace('https:/','https://',1)
				else:
					u=u.replace('https:','https:/',1)
					temp=u.replace('https:/','',1)
					if temp.find('/')==0:
						return u
					else:
						return u.replace('https:/','https://',1)
			else:
				u=u.replace('https','https:',1)
				temp=u.replace('https:','',1)
				if temp.find('/')==0:
					temp=temp.replace('/','',1)
					if temp.find('/')==0:
						return u
					else:
						return u.replace('https:/','https://',1)
				else:
					u=u.replace('https:','https:/',1)
					temp=u.replace('https:/','',1)
					if temp.find('/')==0:
						return u
					else:
						return u.replace('https:/','https://',1)
		else:
			temp=u.replace('http','',1)
			if temp.find(':')==0:
				temp=temp.replace(':','',1)
				if temp.find('/')==0:
					temp=temp.replace('/','',1)
					if temp.find('/')==0:
						return u
					else:
						return u.replace('http:/','http://',1)
				else:
					u=u.replace('http:','http:/',1)
					temp=u.replace('http:/','',1)
					if temp.find('/')==0:
						return u
					else:
						return u.replace('http:/','http://',1)
			else:
				u=u.replace('http','http:',1)
				temp=u.replace('http:','',1)
				if temp.find('/')==0:
					temp=temp.replace('/','',1)
					if temp.find('/')==0:
						return u
					else:
						return u.replace('http:/','http://',1)
				else:
					u=u.replace('http:','http:/',1)
					temp=u.replace('http:/','',1)
					if temp.find('/')==0:
						return u
					else:
						return u.replace('http:/','http://',1)
	else:
		#try for other famous schemes Not done yet
		famousScheme=["ftp","ssh","geo","info","magnet","mailto"]
		u='http'+u
		temp=u.replace('http','',1)
		if temp.find(':')==0:
			temp=temp.replace(':','',1)
			if temp.find('/')==0:
				temp=temp.replace('/','',1)
				if temp.find('/')==0:
					return u
				else:
					return u.replace('http:/','http://',1)
			else:
				u=u.replace('http:','http:/',1)
				temp=u.replace('http:/','',1)
				if temp.find('/')==0:
					return u
				else:
					return u.replace('http:/','http://',1)
		else:
			u=u.replace('http','http:',1)
			temp=u.replace('http:','',1)
			if temp.find('/')==0:
				temp=temp.replace('/','',1)
				if temp.find('/')==0:
					return u
				else:
					return u.replace('http:/','http://',1)
			else:
				u=u.replace('http:','http:/',1)
				temp=u.replace('http:/','',1)
				if temp.find('/')==0:
					return u
				else:
					return u.replace('http:/','http://',1)

def checkHostName(u):
	"""Checks host name"""
	try:
		#Obvious Case 'www'
		li=u.split("://")
		temp=li[1].split('.',1)
		host=temp[0]
		#print host
		if host=="www":
			return u
		#Need other popular like www
		elif host=="localhost":
			return u
		else:
			return u.replace(host,"www")

		#Will check from file if Host valid
	except IndexError as e:
		print "Failed repairs from checkScheme"
		
def checkTopLevelDomain(u):
	#Split the top level domain
	a=u.split("://")
	temp=a[1].split('.')
	tld=temp[len(temp)-1]
	validTLD=["com","org","net","int","edu","gov","mil"]
	if tld in validTLD:
		return u
	else:
		file1=open("validTLD")
		li1=file1.read().splitlines()
		if tld in li1:
			return u
		else:
			#NO matches found repairing with ".com"
			return u.replace(tld,"com")

		
def main(url):
	"""Passing url among various checkFunctions"""
	url=checkScheme(url)
	url=checkHostName(url)
	url=checkTopLevelDomain(url)
	print url
	#url=checkPath(url)
