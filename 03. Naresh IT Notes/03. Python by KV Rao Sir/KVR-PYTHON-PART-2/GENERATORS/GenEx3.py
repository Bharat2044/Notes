#GenEx3.py
def kvrrange(start,stop=None,step=1):
	if(stop==None):
		stop=start
		start=0
	while(start<=stop):
		yield start
		start=start+step


#Main Program
kv=kvrrange(10,51,10)
print("Type of kv=",type(kv))
while(True):
	try:
		print(next(kv))
	except StopIteration:
		break
print("-----------------------------------------------")
kv1=kvrrange(100,106)
for val in kv1:
	print(val)
print("-----------------------------------------------")
kv1=kvrrange(15)
for val in kv1:
	print(val)