#Program for Finding Sum of List of Numbers by using recduce()
#ReduceEx1.py
import functools
lst=[10,20,30,40,50]
res=functools.reduce(lambda x,y: x+y, lst)
print("sum({})={}".format(lst,res))