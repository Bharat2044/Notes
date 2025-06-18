#Program calculating Division of Two Numbers
#Div5.py------This Program Developed by KVR on 20-04-2024 at 8:18am
#In the near Future-2029, New Programmer Sumith--Fresher
try:
	print("Program Execution Started")
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	#Convert s1 and s2 into int type
	a=int(s1) # Exception generated statement--ValueError
	b=int(s2) # Exception generated statement--ValueError
	c=a/b  # Exception generated statement--ZeroDivisionError
	s="PYTHON"
	print(s[10])
except ZeroDivisionError:
	print("\tDON'T ENTER ZERO FOR DEN...")
except ValueError:
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
except IndexError:
	print("Plz Check the Index:")
except: # default except block
	print("Ooooops, some thing went wrong!!!")
else:
	print("----------------------------------------------")
	print("Val of a=",a)
	print("Val of b=",b)
	print("Div=",c)
	print("----------------------------------------------")
finally:
	print("Program Execution completed--finally block")
