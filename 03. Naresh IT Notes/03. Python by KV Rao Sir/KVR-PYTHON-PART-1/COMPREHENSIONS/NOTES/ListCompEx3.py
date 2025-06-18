#program for accepting only +VE Values from Keyboard
#ListCompEx3.py
print("Enter List of Numerical Values separated by space for getting +Ve Vals:")
pslist=[ float(value)  for value in input().split()  if float(value)>0 ]
print(pslist,type(pslist))
print("Number of +Ve Values=",len(pslist))
print("------------------------------------")
print("Enter List of Numerical Values separated by space for getting -Ve Vals:")
nglist=[ float(value)  for value in input().split()  if float(value)<0 ]
print(nglist,type(nglist))
print("Number of -Ve Values=",len(nglist))