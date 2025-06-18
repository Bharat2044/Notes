#Employee.py<----File Name and Module Name
class Employee:
    def setEmpValues(self,eno,ename,sal):
        self.eno=eno
        self.ename=ename
        self.sal=sal
    def getEmpValues(self):
        print("\t{}\t{}\t{}".format(self.eno,self.ename,self.sal))
