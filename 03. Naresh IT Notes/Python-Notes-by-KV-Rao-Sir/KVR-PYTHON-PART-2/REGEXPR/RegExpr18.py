#Searches for all   word character
#RegExpr18.py
import re
matd=re.finditer(r"\w","!cH4LuaP7#Bb6@QpWmD9%")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")
