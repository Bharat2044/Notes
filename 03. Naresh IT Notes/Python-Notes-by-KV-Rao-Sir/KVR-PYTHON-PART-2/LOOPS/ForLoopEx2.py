#Program for Obtaining every character from string data
#ForLoopEx2.py
s=input("Enter Any String Data")
print("By using for loop")
print("============================")
for ch in s: # s="PYTHON
    print(ch)
else:
    print("****************************************")
print("By using for loop-reversed data")
for ch in s[::-1]:
    print(ch)
else:
    print("==================================")