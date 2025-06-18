#DivOpDemo.py<---File Name--Phase-3 --Handling the exception
from DivOp import division
from Except import DenDivisionError
while(True):
    try:
        a = int(input("Enter Value of a:"))
        b = int(input("Enter Value of b:"))
        res=division(a,b) # Function call--gives either result or exception
    except DenDivisionError:
        print("Don't enter zero for Den....")
    except ValueError:
        print("Don't enter alnums,strs and symbols")
    else:
        print("Div=",res)
        break
    finally:
        print("I am from finally block")