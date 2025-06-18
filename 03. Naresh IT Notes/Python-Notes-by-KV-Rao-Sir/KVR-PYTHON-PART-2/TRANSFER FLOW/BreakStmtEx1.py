#Program for Demonstrating break stmt
#BreakStmtEx1.py
s="PYTHON"
print("By using for Loop without break stmt")
for ch in s:
    print(ch)
else:
    print("else part of for loop")
print("------------------------------")
#My Requirment is to disp only PYT without using indexing and slicing
print("By using for Loop with break stmt")
for ch in s:
    if(ch=="H"):
        break
    print(ch,end="")
else:
    print("else part of for loop")
print()
print("Program execution Completed!!!")