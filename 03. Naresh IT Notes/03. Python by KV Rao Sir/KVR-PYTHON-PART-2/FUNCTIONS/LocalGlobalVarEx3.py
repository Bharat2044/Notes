#Program for Demonstrating Local anf Global Variables
#LocalGlobalVarEx3.py
def learnAI():
	sub1="AI" # Here sub1 is called Local Variable
	print("TO Develop '{}' Applications, we use '{}' Programming Lang".format(sub1,lang))
	#print(sub2,sub3)----bcoz sub2 and sub3 are local to other functions
def learnML():
	sub2="ML"  # Here sub2 is called Local Variable
	print("TO Develop '{}' Applications, we use '{}' Programming Lang".format(sub2,lang))
	#print(sub1,sub3)----bcoz sub1 and sub3 are local to other functions
lang="PYTHON" # Here lang is called Global Variable
def learnDL():
	sub3="DL"   # Here sub3 is called Local Variable
	print("TO Develop '{}' Applications, we use '{}' Programming Lang".format(sub3,lang))
	#print(sub1,sub1)----bcoz sub1 and sub1 are local to other functions
#Main Program
learnAI()
learnML()
learnDL()