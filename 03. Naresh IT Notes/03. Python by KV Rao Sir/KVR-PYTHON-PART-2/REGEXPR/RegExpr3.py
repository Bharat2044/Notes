#RegExpr3.py
import re
gd="Python is an oop lang.python is also fun lang"
sp="Python"
res=re.search(sp,gd) # here res is an object of <class, re.match> if data found other res type is <class 'NoneType'>
if(res!=None):
	print("Search is Successful")
	print("Start Index:",res.start())
	print("End Index:",res.end())
	print("Value:",res.group())
else:
	print("Search is Un-Successful")
