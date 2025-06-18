#EmpPickUnPickOops1.py
from EmployeePick import EmpPick
from EmployeeUnPick import EmpUnPick
while(True):
    print("-"*50)
    print("\tEmployee Pick and Un-Pickling Operations")
    print("-"*50)
    print("\t1.Insert Emp Record")
    print("\t2.Read Emp Records")
    print("\t3.Exit")
    print("-"*50)
    ch=int(input("Enter Ur Choice:"))
    match(ch):
        case 1:
            ep=EmpPick()
            ep.saveemprecord()
        case 2:
            eo=EmpUnPick()
            eo.readrecords()
        case 3:
            print("Thx for using this App")
            break
        case _:
            print("Ur Selection of Operation is Wrong--try Again")

