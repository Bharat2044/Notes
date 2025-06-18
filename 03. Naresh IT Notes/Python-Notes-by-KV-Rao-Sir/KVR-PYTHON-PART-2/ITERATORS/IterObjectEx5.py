#Program for demonstrating Iterator
#IterObjectEx5.py
x="PYTHON"
print(type(x))  # <class 'str'>
#Convert  Itetable object x into  Iterator object type
itobj=iter(x)
print("type of itobj=",type(itobj))  # <class 'str_ascii_Iterator'>
for ch in itobj:
	print(ch)