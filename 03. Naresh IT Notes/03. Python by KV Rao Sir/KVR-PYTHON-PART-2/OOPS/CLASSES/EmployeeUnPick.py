#EmployeeUnPick.py<-----File Name and Module Name
import pickle
class EmpUnPick:
    def readrecords(self):
        with open("emp.pic","rb") as fp:
            print("-----------------------------------")
            while(True):
                try:
                    record=pickle.load(fp) # record is an object of <class, Employee.Employee>
                    record.getEmpValues()
                except EOFError:
                    print("-----------------------------------")
                    break
