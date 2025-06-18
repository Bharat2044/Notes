#Program for Demonstrating break stmt
#BreakStmtEx2.py
import sys
s="PYTHON"
print("By using while Loop without break stmt")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("else part of while loop")
print("------------------------------")
#My Requirment is to disp only PYTH without using indexing and slicing
print("By using while Loop with break stmt")
i=0
while(i<len(s)):
    if(s[i]=="O"):
        break
    print(s[i],end="")
    i+=1
else:
    print("else part of while loop")
print()
print("Program execution Completed!!!")