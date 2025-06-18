#StudentMarksReportEx1.py
#Accept Student Number and Validate--100 to 200
while(True):
    sno=int(input("Enter Student Number(100-200):"))
    if(sno<100) or (sno>200):
        print("\t{} is Invalid Student Number:".format(sno))
    else:
        break
#Validate Name
while(True):
    name=input("Enter Studenty Name:")# Name=Guido Van Rossum
    namewords=name.split()
    res=True
    for word in namewords:
        if( not word.isalpha()):
            res=False
            break
    if(res):
        break
    else:
        print("\t{} is Invalid Student Name-try again".format(name))
#Accept Student Marks in C Lang
while(True):
    cm=input("Enter Marks in C lang:")
    if(cm.isdigit()) and (0<=int(cm)<=100):
        break
    else:
        print("\t{} Invalid Marks in C Lang-try again".format(cm))
#Accept Student Marks in C++ Lang
while(True):
    cppm=input("Enter Marks in C++ lang:")
    if(cppm.isdigit()) and (0<=int(cppm)<=100):
        break
    else:
        print("\t{} Invalid Marks in C++ Lang-try again".format(cppm))
#Accept Student Marks in Python Lang
while(True):
    pym=input("Enter Marks in PYTHON lang:")
    if(pym.isdigit()) and (0<=int(pym)<=100):
        break
    else:
        print("\t{} Invalid Marks in Python Lang-try again".format(pym))
#Compute Total and Percentage
totmarks=int(cm)+int(cppm)+int(pym)
percent=(totmarks/300)*100
#Check for Failed Students
if(int(cm)<40) or (int(cppm)<40) or (int(pym)<40):
    grade="FAIL"
else:
    if(300>=totmarks>=250):
        grade="DISTINCTION"
    elif(totmarks in range(200,250)):
        grade="FIRST"
    elif(totmarks in range(150,200)):
        grade="SECOND"
    elif(totmarks>=120) and (totmarks<=149):
        grade="THIRD"
#Display Student Marks Report
print("*"*50)
print("\tSTUDENT MARKS REPORT")
print("*"*50)
print("\tStudent Number:{}".format(sno))
print("\tStudent Name:{}".format(name))
print("\tStudent Marks in C:{}".format(cm))
print("\tStudent Marks in C++:{}".format(cppm))
print("\tStudent Marks in PYTHON:{}".format(pym))
print("------------------------------------------")
print("\tTOTAL MARKS:{}".format(totmarks))
print("\tPERCETAGE OF MARKS:{}".format(percent))
print("\tSTUDENT GRADE:{}".format(grade))
print("*"*50)