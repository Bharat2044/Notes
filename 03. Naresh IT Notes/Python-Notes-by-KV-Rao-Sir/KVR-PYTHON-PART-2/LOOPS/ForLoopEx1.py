#Program for Obtaining every character from string data
#ForLoopEx1.py
s="PYTHON"
print("By using while loop +ve Index")
print("============================")
i=0  # Initlization Part
while(i<len(s)): # Cond Part
    print(s[i])
    i+=1 # Updation Part
else:
    print("============================")
print("By using while loop -ve Index")
print("============================")
i=-len(s)
while(i<=-1):
    print(s[i])
    i=i+1
else:
    print("============================")
print("By using for loop")
print("============================")
for ch in s: # s="PYTHON
    print(ch)
else:
    print("****************************************")