#Searches for all   except Alphabtes
#RegExpr13.py
import re
matd=re.finditer("[^A-Za-z]","cH4LuaP7#Bb6@QpWmD9%")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")
