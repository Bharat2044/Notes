#Searches for either 'a' or 'b' or 'c' only
#RegExpr4.py
import re
gd="cH4LuaP7#Bb6@QpWmD9%"
sp="[abc]"
matd=re.finditer(sp,gd)
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")