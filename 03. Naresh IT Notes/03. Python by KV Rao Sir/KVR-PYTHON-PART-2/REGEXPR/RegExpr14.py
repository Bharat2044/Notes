#Searches for all   alpha-numerics
#RegExpr14.py
import re
matd=re.finditer("[A-Za-z0-9]","cH4LuaP7#Bb6@QpWmD9%")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")
