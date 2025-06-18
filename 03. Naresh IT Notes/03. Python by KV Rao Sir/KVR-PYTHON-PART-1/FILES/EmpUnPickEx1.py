#Program for Reading the Records from File--Un-Pickling
#EmpUnPickEx1.py
import pickle,sys
try:
    fp=open("emp.pick","rb")
    print("--------------------------------")
    print("Employee Record")
    print("--------------------------------")
    while(True):
        try:
            record=pickle.load(fp)
            for val in record:
                print("\t{}".format(val),end="\t")
            print()
        except EOFError:
            print("--------------------------------")
            break
except FileNotFoundError:
    print("File does not Exist")

