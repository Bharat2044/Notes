#EmployeePick.py<----File Name and Module Name
from Employee import Employee
import pickle
class EmpPick:
    def saveemprecord(self):
        with open("emp.pic","ab") as fp:
            while(True):
                try:
                    print("--------------------------------")
                    #get the values from KBD
                    eno=int(input("Enter Employee Number:"))
                    name=input("Enter Employee Name:")
                    sal=float(input("Enter Employee Salary:"))
                    #create an object of Employee Class of Employee Module
                    eo=Employee()
                    eo.setEmpValues(eno,name,sal)
                    #Write OR Save the emp Data into the file
                    pickle.dump(eo,fp)
                    print("--------------------------------")
                    print("Employee Record Saved Sucessfully in File:")
                    print("--------------------------------")
                    ch=input("Do u want inert another Emp record(yes/no):")
                    if(ch.lower()=="no"):
                        print("Thx for using this program")
                        break
                except ValueError:
                    print("Don't try to enter alnums,strs and symbols for eno and salary")

