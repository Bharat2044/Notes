#Searches for all except  'a' or 'b' or 'c' only
#RegExpr5.py
import re
matd=re.finditer("[^abc]","cH4LuaP7#Bb6@QpWmD9%")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")