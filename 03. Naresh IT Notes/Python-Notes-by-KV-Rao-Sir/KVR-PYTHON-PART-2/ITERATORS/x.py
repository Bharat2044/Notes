
def  addop(a,b):
	yield (a+b)

def subop(a,b):
	print("sub=",(a-b))
	res=addop(10,20)
	print("add=",next(res))


subop(100,200)