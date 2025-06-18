#Program for extracting Marks of students from given text
#MarksExtractEx1.py
import re
gd="Rossum got 55 marks , Travis got 44 marks , Kinney got 66 marks and Gosling got 22 marks and Kvr got 11 marks"
sp=r"\d{2}"
markslist=re.findall(sp,gd)
print("-----------------------------------------")
print("Marks")
print("-----------------------------------------")
for marks in markslist:
	print(marks)
print("-----------------------------------------")