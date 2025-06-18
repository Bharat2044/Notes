#Program for Demonstrating Class Level Method
#ClassLevelMethodEx1.py
class Student:
   @classmethod
   def getcrs(cls):
       Student.crs = "Python"  # Class Level Data Member
       cls.addr="HYDERABAD"  # Class Level Data Member
#Main Program
Student.getcrs() # Calling Instance Method w.r.t Class Name
print("Student Course=",Student.crs)
print("Student Addr=",Student.addr)

