#Program for Demonstrating local and Global Variables
#LocalGlobalVarEx2.py
def learnAI():
    sub1="AI" # Here sub1 is local variable
    print("To develop '{}' Applications, we use '{}' Prog Lang".format(sub1,lang))
    #print(sub2,sub3)--can't access bcoz sub2 and sub3 are local variables in other Funs
def learnML():
    sub2="ML" # Here sub2 is local variable
    print("To develop '{}' Applications, we use '{}' Prog Lang".format(sub2,lang))
    # print(sub1,sub3)--can't access bcoz sub1 and sub3 are local variables in other Funs
def learnDL():
    sub3="DL"  # Here sub3 is local variable
    print("To develop '{}' Applications, we use '{}' Prog Lang".format(sub3,lang))
    # print(sub1,sub2)--can't access bcoz sub1 and sub2 are local variables in other Funs
#Main Program
#learnAI()---we can't access global variables lang in learnAI() bcoz it was defined after Its Function Call
lang="PYTHON" # Here lang is called Global Variable
learnML()
learnDL()

