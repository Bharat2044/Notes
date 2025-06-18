#Searches for   all values
#RegExpr26.py
import re
matd=re.finditer(".","KVKKVKKKVKV")
print("-----------------------------------------------------")
for mat in matd:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------")
