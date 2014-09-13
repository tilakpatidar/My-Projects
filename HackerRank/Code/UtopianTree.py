t=int(raw_input())
n=[]
for i in range(t):
	n.append(int(raw_input()))
for j in n:
	h=1
	switch=0
	for l in range(j):
		if switch==0:
			h*=2
			switch=1
		elif switch==1:
			h+=1
			switch=0
	print h
