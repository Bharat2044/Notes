#Program for Demonstrating Instance Data Members
#I want to Store sno,sname and Marks
#InstanceDataMembersEx1.py
class Student:pass

#Main Program
s1=Student() # Object Creation
s2=Student() # Object Creation
#Add Instance Data Members to s1 Object by using OBJECT Itself
s1.sno=100
s1.name="RS"
s1.marks=44.56
#Add Instance Data Members to s2 Object by using OBJECT Itself
s2.stno=200
s2.sname="TR"
s2.marks=56.78
#Display the S1 Object Data--Instance Data Members of s1 Object
print("------------------------------------")
print("First Student Data")
print("------------------------------------")
print("\tStudent Number=",s1.sno)
print("\tStudent Name=",s1.name)
print("\tStudent Marks=",s1.marks)
#Display the S1 Object Data--Instance Data Members of s1 Object
print("------------------------------------")
print("Second Student Data")
print("\tStudent Number=",s2.stno)
print("\tStudent Name=",s2.sname)
print("\tStudent Marks=",s2.marks)
print("------------------------------------")