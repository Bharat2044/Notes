#Searches for all   except Lower Case alphabets
#RegExpr9.py
import re
matd=re.finditer("[^a-z]","cH4LuaP7#Bb6@QpWmD9%")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")