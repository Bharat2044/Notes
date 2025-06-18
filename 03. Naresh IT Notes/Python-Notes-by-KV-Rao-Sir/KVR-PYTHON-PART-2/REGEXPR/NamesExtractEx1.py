#Program for extracting Names of students from given text
#NamesExtractEx1.py
import re
gd="Rossum got 55 marks , Travis got 44 marks , Kinney got 66 marks and Gosling got 22 marks and Kvr got 11 marks"
sp="[A-Z][a-z]+"
nameslist=re.findall(sp,gd)
print("-----------------------------------------")
print("Names")
print("-----------------------------------------")
for names in nameslist:
	print(names)
print("-----------------------------------------")
