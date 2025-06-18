#Program for Demonstrating the Need of Keyword Variable length Arguments
#PureKeyWordVarLenEx6.py
def computetotal(sid,sname,cls,*vals,city="HYD",**submarks):
	print("Variable Args")
	print("-----------------------------------------")
	for v in vals:
		print("{}".format(v),end="  ")
	print()
	if(len(submarks)!=0):
		totmarks=0
		print("------------------------------------------------------")
		print("Student Number=",sid)
		print("Student Name=",sname)
		print("Student Class=",cls)
		print("Student City=",city)
		print("------------------------------------------------------")
		print("Subject\tMarks")
		print("------------------------------------------------------")
		for sub,marks in submarks.items():
			print("{}\t{}".format(sub,marks))
			totmarks+=marks
		print("------------------------------------------------------")
		print("TOTAL MARKS=",totmarks)
		print("------------------------------------------------------")
	else:
		print("------------------------------------------------------")
		print("Student Number=",sid)
		print("Student Name=",sname)
		print("Student Class=",cls)
		print("Student City=",city)
		print("------------------------------------------------------")

#Main program
computetotal(10,"Kumar","X",10,20,30,40,50,Tel=50,Hindi=90,English=76,Maths=90,Science=70,Social=75)
computetotal(20,"Likit","XII",1,2,3,Sankrit=99,Englis=70,Maths=75,Chemistry=60,Physics=55)
computetotal(30,"Sumith","B.Tech(CSE)",1.2,2.2,3.4,4.4,OS=70,DBMS=50)
computetotal(40,"Rossum","Scientist","Python","Numpy")
computetotal(50,"KVR","Triner",city="BANG")
computetotal(50,"RR","SE",city="MUMBAI",sub1=20,sub2=30,sub3=50,)