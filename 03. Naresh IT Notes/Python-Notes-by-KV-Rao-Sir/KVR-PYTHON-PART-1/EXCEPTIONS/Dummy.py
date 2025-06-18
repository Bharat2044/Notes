#Program calculating Division of Two Numbers
#Dummy.py
try:
	print("Program Execution Started")
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	#Convert s1 and s2 into int type
	a=int(s1) # Exception generated statement--ValueError
	b=int(s2) # Exception generated statement--ValueError
	print("Val of a=",a)
	print("Val of b=",b)
	c=a/b  # Exception generated statement--ZeroDivisionError
	print("Div=",c)
	print("Program Execution Ended")
except : # Default except block
	print("Ooooops, some thing went wrong!!!")

