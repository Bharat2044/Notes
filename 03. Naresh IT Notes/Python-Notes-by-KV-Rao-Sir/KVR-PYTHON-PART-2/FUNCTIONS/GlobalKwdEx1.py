#Program for Demonstrating global keyword
#GlobalKwdEx1.py
def incr():
	global a
	a=a+1
	
def modify():
	global a
	a=a*2

#Main program
a=10 # Here 'a' is called global Variable
print("Val of GV-a before function call=",a)
incr() # Function call
print("Val of GV-a  after function call=",a)
modify()
print("Val of GV-a  after function call=",a)