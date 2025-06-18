#program for Demonstrating Class Level Data Members
#ClassLevelDataMemberEx1.py
class Student:
    crs="PYTHON" # here crs is called Class Level Data Member
class Emp:
    compname="IBM" # here compname is called Class Level Data Member
#Main Program
print("Course for all Students=",Student.crs)
print("Comp Name of all Employees=",Emp.compname)
print("------------------OR-------------------")
s=Student()
e=Emp()
print("Course for all Students=",s.crs)
print("Comp Name of all Employees=",e.compname)


