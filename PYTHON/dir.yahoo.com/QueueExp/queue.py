import thread
import threading
from Queue import Queue
ThreadList=[]
class do(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		print "Hey"
		for i in range(50):
			ThreadList.append(do())
			#print dir(self)
			#do().start()
def t1():
	try:
		while True:
			if q.qsize()==10:
				for i in range(10):
					q.get().start()
	except Exception as e:
		print e
def t():
	try:
		rng=10
		while True:
			if len(ThreadList)>10 and q.qsize()==0:
				print "Start"
				for i in range(rng-10,rng):
					q.put(ThreadList[i])
				print len(ThreadList)
				rng+=10
	except Exception as e:
		print e
			
q=Queue(maxsize=10)
thread.start_new_thread(t,())
thread.start_new_thread(t1,())
do().start()
#q.put(do())
#Create a list structure and store instances of classes
#In a new thread create a function which only takes 10 ThreadListects at a time 


