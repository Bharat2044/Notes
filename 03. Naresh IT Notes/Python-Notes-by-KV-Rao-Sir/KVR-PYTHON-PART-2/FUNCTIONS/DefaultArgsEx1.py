#Program for Demonstrating Possitional Arguments
#DefaultArgsEx1.py
def  dispstud(sno,sname,marks,crs="PYTHON"): # here  crs is called Default Parameter
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))


#Main Program
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE")
print("*"*50)
dispstud(10,"RS",23.45) # Function call
dispstud(20,"TR",45.67)  # Function call
dispstud(30,"DR",25.67)  # Function call
dispstud(40,"RD",15.67)  # Function call
print("*"*50)