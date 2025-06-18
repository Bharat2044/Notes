#Program for Demonstrating Class Level Method
#ClassLevelMethodEx4.py
class Student:
   @classmethod
   def getcrs(cls):
       Student.crs = "Python"  # Class Level Data Member
   @classmethod
   def getaddr(cls):
       cls.getcrs() # Calling Class Level method w.r.t cls
       cls.addr="HYDERABAD"  # Class Level Data Member
#Main Program
Student.getaddr() # Calling Instance Method w.r.t Class Name
print("Student Course=",Student.crs)
print("Student Addr=",Student.addr)

