#Program for obtaining a line of text from List of words
#ReduceEx4.py
import functools
print("Enter List of Words Separated by Comma:")
lst=[val for val in input().split(",")] # lst=["Python","Is","An","oop","lang"]
line=functools.reduce(lambda x,y: x+" "+y, lst)
print("Line of text=",line)