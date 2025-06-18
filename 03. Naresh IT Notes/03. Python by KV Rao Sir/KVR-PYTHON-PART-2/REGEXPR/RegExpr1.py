#RegExpr1.py
import re
gd="Python is an oop lang.Python is also fun lang"
sp="Python"
noc=re.findall(sp,gd)
print("'{}'  found {} Times".format(sp,len(noc)))
