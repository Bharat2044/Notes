#Program for Reading the employee Data from KBD and Save them in a file
#EmpPickEx1.py
import pickle
with open("emp.pick","ab") as fp:
    while(True):
        #read the employee data from KBD
        eno=int(input("Enter Employee Number:"))
        ename=input("Enter Employee Name:")
        sal=float(input("Enter Employee Salary:"))
        print("-------------------------------------")
        #Create an empty list for place emp values
        emplist=list()
        emplist.append(eno)
        emplist.append(ename)
        emplist.append(sal)
        pickle.dump(emplist,fp)
        print("Employee Record Saved in File sucessfully")
        print("-------------------------------------")
        ch=input("Do u want to Insert Another Record(yes/no):")
        if(ch.lower()=="no"):
            print("Thx for Using program")
            break



