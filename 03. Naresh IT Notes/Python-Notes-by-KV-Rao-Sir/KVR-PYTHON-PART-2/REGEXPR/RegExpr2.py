#RegExpr2.py
import re
gd="Python is an oop lang.Python is also fun lang"
sp="Python"
matd=re.finditer(sp,gd) # here matd is an object of <class, callable_iterator>
for mat in matd: # here mat is an object of <class, re.match>
	print("Start Index:{}   End Index:{}   Value:{}".format(mat.start(),mat.end(),mat.group()))
