#GenEx2.py
def kvrrange(val):
	i=0
	while(i<val):
		yield i
		i=i+1

#Main Program
r=kvrrange(10) # Here r type is <class, generator>
print("Type of r=",type(r))
print(next(r))
while(True):
	try:
		print(next(r))
	except StopIteration:
		break
print("-------------------------------------------")
r1=range(6)  # Here r1 type is <class, generator>
for val in r1:
	print(val)