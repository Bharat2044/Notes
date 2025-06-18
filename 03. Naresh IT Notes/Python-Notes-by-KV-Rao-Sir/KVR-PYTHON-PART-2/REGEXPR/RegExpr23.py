#Searches for   one K or More K's
#RegExpr23.py
import re
matd=re.finditer("K+","KVKKVKKKVKV")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")
