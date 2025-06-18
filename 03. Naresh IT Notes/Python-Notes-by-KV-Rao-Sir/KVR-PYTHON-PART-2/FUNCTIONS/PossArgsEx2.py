#Program for Demonstrating Possitional Arguments
#PossArgsEx2.py
def  dispstud(sno,sname,marks,crs):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))


#Main Program
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE")
print("*"*50)
dispstud(10,"RS",23.45,"PYTHON") # Function call
dispstud(20,"TR",45.67,"PYTHON")  # Function call
dispstud(30,"DR",25.67,"PYTHON")  # Function call
dispstud(40,"RD",15.67,"PYTHON")  # Function call
print("*"*50)