#Program for demonstrating Iterator
#IterObjectEx4.py
x={10:"Python",20:"Java",30:"C",40:"C++"}
print(type(x))  # <class 'dict'>
#Convert  Itetable object x into  Iterator object type
itobj=iter(x)
print("type of itobj=",type(itobj))  # <class 'dict_key_iterator'>
for val in itobj:
	print("{}-->{}".format(val,x.get(val)))