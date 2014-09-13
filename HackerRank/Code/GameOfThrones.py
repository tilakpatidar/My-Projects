def possible_anagrams(word):
        '''given a word, return a list of possible anagrams for that word'''
        if len(word) == 1:
           yield word
 
        for i, letter in enumerate(word):
            for s in possible_anagrams(word[i+1:] + word[:i]):
                yield '%s%s' % (letter, s)
strr=str(raw_input())
a=possible_anagrams(strr)
flag=0
while True:
	try:
		temp=str(a.next())
		if str(temp)==str(temp)[::-1]:
			print "YES"
			flag=1
			break
	except:
		break
if flag==0:
	print "NO"
