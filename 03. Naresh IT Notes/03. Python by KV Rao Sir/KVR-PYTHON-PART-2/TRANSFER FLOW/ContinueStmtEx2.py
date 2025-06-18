#Program for demonstrating continue statement
#ContinueStmtEx2.py
s="PYTHON"
print("By using while loop without continue stmt")
i=0
while(i<len(s)):
    print(s[i])
    i+=1
else:
    print("else part of while loop without continue stmt")
print("-------------------------------------")
#My Requriment is to display PYHON
print("By using while loop with continue stmt")
i=0
while(i<len(s)):
    if(s[i]=="T"):
        i=i+1
        continue
    print(s[i])
    i=i+1
else:
    print("else part of while loop with continue stmt")
print("-------------------------------------")