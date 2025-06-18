#Searches for all   only Alphabtes
#RegExpr12.py
import re
matd=re.finditer("[A-Za-z]","cH4LuaP7#Bb6@QpWmD9%")
noa=0
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
	noa=noa+1
print("-----------------------------------------------------")
print("Number of alphabets=",noa)