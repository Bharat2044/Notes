#Program for Searching a Record Based Emp Number
#EmpPickSearch.py<----File Name and Module Name
import pickle
def searchrecord():
    empno=int(input("Enter Emp Number for getting Other details:"))
    with open("emp.pick","rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                if(empno==record[0]):
                    print("--------------------------------")
                    print("Emp  Number:{}".format(record[0]))
                    print("Emp  Name:{}".format(record[1]))
                    print("Emp  Salary:{}".format(record[2]))
                    print("--------------------------------")
                    break
            except EOFError:
                print("--------------------------------")
                print("Employee Number does not Exist")
                print("--------------------------------")
                break

