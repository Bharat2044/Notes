#DecEx5.py
def splitwordsreverse(ucc):
	def reversesplit():
		line,lc,uc=ucc()
		words=lc.split()
		lst=[]
		for word in words:
			lst.append(word[::-1])
		return line,lc,uc,lst
	return  reversesplit

def convertupper(cl):
	def uppercon():
		line,lc=cl()
		uc=line.upper()
		return line,lc,uc
	return uppercon

def convertlower(gv):
	def lowercon():
		line=gv()
		lc=line.lower()
		return line,lc
	return lowercon

@splitwordsreverse
@convertupper
@convertlower
def getline():
	return input("Enter a Line of Text:")

#Main Program
line,lc,uc,lst=getline()
print("------------------------------------------")
print("Given Line:",line)
print("\nLower Case:",lc)
print("\nUpper Case:",uc)
print("\nReversed Words:",lst)
print("----------------OR--------------------------")
result=getline()
print("Given Line:",result[0])
print("\nLower Case:",result[1])
print("\nUpper Case:",result[2])
print("\nReversed Words:",result[3])