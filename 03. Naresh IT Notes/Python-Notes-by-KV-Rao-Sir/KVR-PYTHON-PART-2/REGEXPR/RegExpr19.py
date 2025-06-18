#Searches for all   special symbols
#RegExpr19.py
import re
matd=re.finditer(r"\W","!cH4LuaP 7#Bb6@QpWmD9%")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")
