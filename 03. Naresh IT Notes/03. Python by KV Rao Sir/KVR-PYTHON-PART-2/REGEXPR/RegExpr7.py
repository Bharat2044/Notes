#Searches for all  except Upper Case alphabets
#RegExpr7.py
import re
matd=re.finditer("[^A-Z]","cH4LuaP7#Bb6@QpWmD9%")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")