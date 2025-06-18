#Searches for  exactly one K
#RegExpr22.py
import re
matd=re.finditer("K","KVKKVKKKVKV")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")
