#Program for Demonstrating Instance Data Members
#I want to Store sno,sname and Marks and course
#ClassLevelDataMemberEx4.py
class Student:
    crs="PYTHON PROGRAMMING" # here cls is called Class Level Data Member

#Main Program
s1=Student() # Object Creation
s2=Student() # Object Creation
print("------------------------------------")
print("Content of s1={} and Number of Vals={}".format(s1.__dict__,len(s1.__dict__)))
print("Content of s2={} and Number of Vals={}".format(s2.__dict__,len(s2.__dict__)))
print("------------------------------------")
#Add Instance Data Members to s1 Object by using OBJECT Itself
while(True):
    try:
        s1.sno=int(input("Enter First Student Number:"))
        s1.name=input("Enter First Student Name:")
        s1.marks=float(input("Enter First Student Marks:"))
    except ValueError:
        print("Don't Enter alnums,strs and synbols for sno and marks")
    else:
        # Display the S1 Object Data--Instance Data Members of s1 Object
        print("------------------------------------")
        print("First Student Data")
        print("------------------------------------")
        print("\tStudent Number=", s1.sno)
        print("\tStudent Name=", s1.name)
        print("\tStudent Marks=", s1.marks)
        print("\tSTUDENT COURSE=", s1.crs)
        print("------------------------------------")
        break
#Add Instance Data Members to s2 Object by using OBJECT Itself
while(True):
    try:
        s2.sno=int(input("Enter second Student Number:"))
        s2.name=input("Enter Second Student Name:")
        s2.marks=float(input("Enter Second Student Marks:"))
    except ValueError:
        print("Don't Enter alnums,strs and synbols for sno and marks")
    else:
        print("Second Student Data")
        print("------------------------------------")
        print("\tStudent Number=",s2.sno)
        print("\tStudent Name=",s2.name)
        print("\tStudent Marks=",s2.marks)
        print("\tSTUDENT COURSE=",s2.crs)
        print("------------------------------------")
        break