#!/usr/bin/python
import hashlib,sha,sys
def hashPassword(key):
	#Step 1 conversion of input to md5
	m = hashlib.md5()
	m.update(key)
	s1=m.hexdigest()
	print str(s1)
	#print 'Step 1 md5 ',s1
	#Step 2 Conversion of s1 to salt
	#By adding salt from 2 places from right as well left
	salt=r'tilak@Google05-05-1995#IndiaSal$100000$'
	l=len(s1)
	mid=s1[2:-2]
	s2=str(s1[0]+s1[1]+salt+mid+salt+s1[-2]+s1[-1])
	#print 's2  ',s2
	#Step 3
	#Converting salt version to md5 again
	m=hashlib.md5()
	m.update(s2)
	s3=m.hexdigest()
	#print 's3  ',s3
	#Step 4 
	#Replacement algorithm
	#replacing 9 by 1
	temp=s3.replace('9','1')
	#replacing 0 by 5
	temp=temp.replace('0','5')
	#replacing a by t
	temp=temp.replace('a','t')
	
hashPassword(sys.argv[0])
