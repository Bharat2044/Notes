#Program for Demonstrating Possitional Arguments
#PossArgsEx1.py
def  dispstud(sno,sname,marks):
	print("\t{}\t{}\t{}".format(sno,sname,marks))


#Main Program
print("*"*50)
print("\tSTNO\tNAME\tMARKS")
print("*"*50)
dispstud(10,"RS",23.45) # Function call
dispstud(20,"TR",45.67)  # Function call
dispstud(30,"DR",25.67)  # Function call
print("*"*50)