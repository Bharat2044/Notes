#Program for Demonstrating Instance Method
#InstanceMethodEx1.py
class Student:
    def getstuddata(self,objinfo):
        print("-"*50)
        self.sno=int(input("Enter {} Student Number:".format(objinfo)))
        self.name=input("Enter {} Student Name:".format(objinfo))
        self.marks=float(input("Enter {} Student Marks:".format(objinfo)))
        print("-" * 50)
    def dispstuddata(self,objinfo):
        print("-"*50)
        print("{} Student Details".format(objinfo))
        print("-" * 50)
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))
        print("-" * 50)
#Main Program
s1=Student()
s2=Student()
print("Id of s1 in main program=",id(s1))
print("Id of s2 in main program=",id(s2))
print("------------------------")
s1.getstuddata("First")
s2.getstuddata("Second")
s1.dispstuddata("First")
s2.dispstuddata("Second")
