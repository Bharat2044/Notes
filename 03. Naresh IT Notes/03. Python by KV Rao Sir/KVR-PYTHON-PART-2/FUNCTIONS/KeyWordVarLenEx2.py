#Program for Demonstrating the Need of Keyword Variable length Arguments
##Conclusion:---This Program will execute bcoz PVM takes the Definition and Immediately calls
#KeyWordVarLenEx2.py
def disp(sno,sname,marks):
	print(sno,sname,marks)
disp(sno=10,sname="RS",marks=12.34) # Function call with 3 Key Word Args
#--------------------------------------------------------------------
def disp(eno,ename,sal,dsg):
	print(eno,ename,sal,dsg)
disp(eno=20,ename="TR",sal=3.4,dsg="SE") # Function call with 4 Key Word Args
#-----------------------------------------------------------------------
def disp(tno,tname,subject,exp,city):
	print(tno,tname,subject,exp,city)
disp(tno=30,tname="SS",subject="Python",exp=10,city="HYD") # Function call with 5 Key Word Args



