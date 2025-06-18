#Program for demonstrating Iterator
#IterObjectEx3.py
x={10,"RS",34.56,2+3j,"Python"}
print(type(x))  # <class 'set'>
#Convert  Itetable object x into  Iterator object type
itobj=iter(x)
print("type of itobj=",type(itobj))  # <class 'set_iterator'>
print(next(itobj))
print(next(itobj))
for val in itobj:
	print(val)