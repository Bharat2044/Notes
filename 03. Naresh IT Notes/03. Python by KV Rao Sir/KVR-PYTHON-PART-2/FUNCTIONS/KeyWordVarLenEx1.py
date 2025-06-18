#Program for Demonstrating the Need of Keyword Variable length Arguments
#Conclusion:---This Program will not execute bcoz PVM Remembers Latest Function Defintion bcoz of PVM is performing Interpretation.
#KeyWordVarLenEx1.py
def disp(sno,sname,marks):
	print(sno,sname,marks)

def disp(eno,ename,sal,dsg):
	print(eno,ename,sal,dsg)

def disp(tno,tname,subject,exp,city):
	print(tno,tname,subject,exp,city)

#Main Program
disp(sno=10,sname="RS",marks=12.34) # Function call with 3 Key Word Args
disp(eno=20,ename="TR",sal=3.4,dsg="SE") # Function call with 4 Key Word Args
disp(tno=30,tname="SS",subject="Python",exp=10,city="HYD") # Function call with 5 Key Word Args