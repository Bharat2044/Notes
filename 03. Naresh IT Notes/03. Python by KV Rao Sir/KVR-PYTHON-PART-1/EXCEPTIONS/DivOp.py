#DivOp.py-<----File Name and Module Name--Phase-2--Hitting the exception
from Except import DenDivisionError
def division(a,b):
    if(b==0):
        raise DenDivisionError
    else:
        return(a/b)

# While we are process the Input with Function Processing Logic
# there is change of occuring Invalid Input
# then raise Programmer-Defined Exception