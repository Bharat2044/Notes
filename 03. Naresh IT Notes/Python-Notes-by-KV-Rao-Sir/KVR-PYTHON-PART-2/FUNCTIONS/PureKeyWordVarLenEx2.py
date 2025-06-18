#Program for Demonstrating the Need of Keyword Variable length Arguments
#PureKeyWordVarLenEx2.py
def  disp(**a):
	print("Number of Values=",len(a))
	for k,v in a.items():
		print("\t{}-->{}".format(k,v))
	print("-----------------------------------------")


#Main Program
disp(sno=10,sname="RS",marks=12.34) # Function call with 3 Key Word Args
disp(eno=20,ename="TR",sal=3.4,dsg="SE") # Function call with 4 Key Word Args
disp(tno=30,tname="SS",subject="Python",exp=10,city="HYD") # Function call with 5 Key Word Args