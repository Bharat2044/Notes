#Program calculating Division of Two Numbers
#Div4.py
try:
	print("Program Execution Started")
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	#Convert s1 and s2 into int type
	a=int(s1) # Exception generated statement--ValueError
	b=int(s2) # Exception generated statement--ValueError
	c=a/b  # Exception generated statement--ZeroDivisionError
except ZeroDivisionError as z:
	print("\t",z)
except ValueError as v:
	print("\t",v)
else:
	print("----------------------------------------------")
	print("Val of a=",a)
	print("Val of b=",b)
	print("Div=",c)
	print("----------------------------------------------")
finally:
	print("Program Execution completed--finally block")
