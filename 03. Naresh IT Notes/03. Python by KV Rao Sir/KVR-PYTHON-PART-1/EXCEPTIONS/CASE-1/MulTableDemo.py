#MulTableDemo.py<---Main Program
from MulEcept import NegNumberError,ZeroError
from MulTable import table
try:
    n=int(input("Enter a Number for Mul table:"))
    table(n) # Function call--result or exception
except ValueError:
    print("Don't Enter floats , alnums, strs and symbols for Int Data")
except NegNumberError:
    print("Don't Enter -Ve Value for Mul Table")
except ZeroError:
    print("Don't Enter Zero for Mul Table")
except:
    print("Ooops Some thing wrong!!!")