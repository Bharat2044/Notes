#Program for demonstrating continue statement
#ContinueStmtEx1.py
s="PYTHON"
print("By using for loop without continue stmt")
for ch in s:
    print(ch)
else:
    print("else part of for loop without continue stmt")
print("-------------------------------------")
#My Requriment is to display PYHON
print("By using for loop with continue stmt")
for ch in s:
    if (ch=="T"):
        continue
    print(ch)
else:
    print("else part of for loop with continue stmt")
print("-------------------------------------")