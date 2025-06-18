#Program for extracting Names and Marks of students from given text
#NamesMarksExtractEx1.py
import re
gd="Rossum got 55 marks , Travis got 44 marks , Kinney got 66 marks and Gosling got 22 marks and Kvr got 11 marks"
sp=r"\d{2}"
markslist=re.findall(sp,gd)
nameslist=re.findall("[A-Z][a-z]+",gd)
print("-----------------------------------------")
print("Names\tMarks")
print("-----------------------------------------")
for names,marks in zip(nameslist,markslist):
	print("{}\t{}".format(names,marks))
print("-----------------------------------------")
