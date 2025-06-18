#ContinueStmtEx5.py
line=input("Enter Line of Text:") # line=PYTHON
print("Given Line:{}".format(line))
#logic for obtaining Vowels
vwlist=list()
for ch in line:
    if ch.lower() not in ["a","e","i","o","u"]:
        continue
    vwlist.append(ch)
else:
    print("List of Vowels")
    print(vwlist)
    print("Number of Vowels={}".format(len(vwlist)))

