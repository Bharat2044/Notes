#Program for Demonstrating the Need of Keyword Variable length Arguments
#PureKeyWordVarLenEx4.py
def computetotal(sid,sname,cls,**submarks):
	if(len(submarks)!=0):
		totmarks=0
		print("------------------------------------------------------")
		print("Student Number=",sid)
		print("Student Name=",sname)
		print("Student Class=",cls)
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
		print("------------------------------------------------------")


#Main program
computetotal(10,"Kumar","X",Tel=50,Hindi=90,English=76,Maths=90,Science=70,Social=75)
computetotal(20,"Likit","XII",Sankrit=99,Englis=70,Maths=75,Chemistry=60,Physics=55)
computetotal(30,"Sumith","B.Tech(CSE)",OS=70,DBMS=50)
computetotal(40,"Rossum","Scientist")