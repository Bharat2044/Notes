#Program for Finding Sum of List of Numbers by using recduce()
#ReduceEx2.py
import functools
def sumop(x,y):
    return (x+y)

#Main Program
print("Enter List of Values Separated by space:")
lst=[float(val) for val in input().split()]
res=functools.reduce(sumop, lst)
print("sum({})={}".format(lst,res))