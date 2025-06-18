#Program for Finding max and min of List of Numbers by using recduce()
#ReduceEx3.py
import functools
print("Enter List of Values Separated by space:")
lst=[float(val) for val in input().split()] # lst=[10,20,14,30,5]
maxv=functools.reduce(lambda k,v: k if k>v else v, lst)
minv=functools.reduce(lambda k,v: k if k<v else v, lst)
print("Max({})={}".format(lst,maxv))
print("Min({})={}".format(lst,minv))