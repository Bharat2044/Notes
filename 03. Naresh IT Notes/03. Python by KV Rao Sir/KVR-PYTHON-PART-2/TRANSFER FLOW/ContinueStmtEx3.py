#My Requriment is to display PYHN
#ContinueStmtEx3.py
s="PYTHON"
print("By using for loop with continue stmt")
for ch in s:
    if (ch=="T") or (ch=="O"):
        continue
    print(ch)
else:
    print("else part of for loop with continue stmt")
print("-------------------------------------")
print("By using for loop with continue stmt")
for ch in s:
    if ch in ["T","O"]:
        continue
    print(ch)
else:
    print("else part of for loop with continue stmt")
print("-------------------------------------")