#College.py<----File Name and Module Name
from Univ import University
class College(University):
    def getCollDet(self):
        self.cname=input("Enter College Name:")
        self.cloc=input("Enter College Location:")
        self.getUnivDet()# Calling Base Class Method from Derived class Method
    def dispCollDet(self):
        self.dispUnivDet()# Calling Base Class Method from Derived Class Method
        print("-" * 50)
        print("College Details")
        print("-" * 50)
        print("College Name:{}".format(self.cname))
        print("College Location:{}".format(self.cloc))
        print("-" * 50)
