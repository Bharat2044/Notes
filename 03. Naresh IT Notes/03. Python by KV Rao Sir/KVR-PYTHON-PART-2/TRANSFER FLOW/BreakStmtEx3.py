#Program for Demonstrating break stmt
#BreakStmtEx3.py
s="MISSISSIPPI"
print("By using for Loop without break stmt")
for ch in s:
    print(ch)
else:
    print("else part of for loop")
print("------------------------------")
#My Requirment is to disp only PYT without using indexing and slicing
print("By using for Loop with break stmt")
for hasind,hasval in enumerate(s):
    if(hasind==4):
        break
    print(hasval,end="")
else:
    print("else part of for loop")
print()
print("Program execution completed")

