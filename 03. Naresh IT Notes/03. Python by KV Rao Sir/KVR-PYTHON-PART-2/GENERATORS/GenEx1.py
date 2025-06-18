#GenEx1.py
def  infinite_series():
	i=0
	while True:
		yield i
		i=i+1

#Main Program
kvr=infinite_series() # Here kvr an object of type <class, 'generator'>
print("Type of kvr=",type(kvr))
print("--------------------------------------------")
print(next(kvr))
print(next(kvr))
print(next(kvr))
for i in range(6):
	print(next(kvr))