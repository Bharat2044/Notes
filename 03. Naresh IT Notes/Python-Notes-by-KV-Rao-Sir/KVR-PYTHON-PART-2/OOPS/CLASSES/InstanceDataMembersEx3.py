#Program for Demonstrating Instance Data Members
#I want to Store sno,sname and Marks
#InstanceDataMembersEx3.py
class Student:pass

#Main Program
s1=Student() # Object Creation
s2=Student() # Object Creation
print("------------------------------------")
print("Content of s1={} and Number of Vals={}".format(s1.__dict__,len(s1.__dict__)))
print("Content of s2={} and Number of Vals={}".format(s2.__dict__,len(s2.__dict__)))
print("------------------------------------")
#Add Instance Data Members to s1 Object by using OBJECT Itself
s1.sno=100
s1.name="RS"
s1.marks=44.56
#Add Instance Data Members to s2 Object by using OBJECT Itself
s2.stno=200
s2.sname="TR"
s2.marks=56.78
s2.addr="HYD"
#Display the S1 Object Data--Instance Data Members of s1 Object
print("------------------------------------")
print("First Student Data")
print("------------------------------------")
for idmn,idmv in s1.__dict__.items():
    print("\t{}--->{}".format(idmn,idmv))
print("Number of Values after adding=",len(s1.__dict__))
print("------------------------------------")
print("Second Student Data")
print("------------------------------------")
for idmn,idmv in s2.__dict__.items():
    print("\t{}--->{}".format(idmn,idmv))
print("Number of Values after adding=",len(s2.__dict__))
print("------------------------------------")