#Program for extracting Names and Marks of students from given File
#NamesMarksExtractEx2.py
import re
try:
	with open("E:\\KVR-PYTHON-6PM\\REG EXPR\\NOTES\\students.data","r") as fp:
		filedata=fp.read()
		markslist=re.findall(r"\d{2}",filedata)
		nameslist=re.findall(r"[A-Z][a-z]+",filedata)
		print("-----------------------------------------")
		print("Names\tMarks")
		print("-----------------------------------------")
		for names,marks in zip(nameslist,markslist):
			print("{}\t{}".format(names,marks))
		print("-----------------------------------------")
		
except FileNotFoundError:
	print("File does not exist")
