#Program for Demonstrating Possitional Arguments
#DefaultArgsEx3.py
def  dispstud1(sno,sname,marks,crs="PYTHON",city="HYD"): # here  crs ,city are called Default Parameter
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,city))

def  dispstud2(sno,sname,marks,crs="JAVA",city="USA"): # here  crs ,city are called Default Parameter
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,city))

#Main Program
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCITY")
print("*"*50)
dispstud1(10,"RS",23.45) # Function call
dispstud1(20,"TR",45.67)  # Function call
dispstud1(40,"RD",15.67)  # Function call
dispstud1(50,"LK",34.56,city="USA") # Function call
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCITY")
print("*"*50)
dispstud2(30,"DR",25.67)  # Function call
dispstud2(60,"TR",22.22)  # Function call
dispstud2(70,"SS",22.22,city="AUS")  # Function call
print("*"*50)