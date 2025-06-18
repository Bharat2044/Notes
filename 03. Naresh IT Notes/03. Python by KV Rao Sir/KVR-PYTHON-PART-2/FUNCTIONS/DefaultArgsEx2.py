#Program for Demonstrating Possitional Arguments
#DefaultArgsEx2.py
def  dispstud(sno,sname,marks,crs="PYTHON",city="HYD"): # here  crs ,city are called Default Parameter
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,city))


#Main Program
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCITY")
print("*"*50)
dispstud(10,"RS",23.45) # Function call
dispstud(20,"TR",45.67)  # Function call
dispstud(30,"DR",25.67,"JAVA","USA")  # Function call
dispstud(40,"RD",15.67)  # Function call
dispstud(50,"LK",34.56,city="USA") # Function call
dispstud(60,"TR",22.22,"JAVA")  # Function call
dispstud(70,"SS",22.22,city="AUS",crs="JAVA")  # Function call
print("*"*50)