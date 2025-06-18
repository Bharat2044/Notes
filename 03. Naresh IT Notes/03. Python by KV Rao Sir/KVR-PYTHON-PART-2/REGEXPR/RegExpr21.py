#Searches for all   except Space Characters
#RegExpr21.py
import re
matd=re.finditer(r"\S","!cH 4LuaP 7#Bb6@QpWmD9%")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")
