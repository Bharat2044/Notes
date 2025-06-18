#Program for demonstrating Iterator
#IterObjectEx1.py
x=[10,"RS",34.56,2+3j,"Python"]
print(type(x))  # <class 'list'>
#Convert  Itetable object x into  Iterator object type
itobj=iter(x)
print("type of itobj=",type(itobj))  # <class 'list_iterator'>
print(next(itobj))
print(next(itobj))
while(True):
	try:
		print(next(itobj))
	except StopIteration:
		break