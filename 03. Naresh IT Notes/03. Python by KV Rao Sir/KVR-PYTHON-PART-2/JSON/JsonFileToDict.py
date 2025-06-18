#JsonFileToDict.py
import json
with open("stud.json","r") as fp:
    d=json.load(fp)
    print(d,type(d))
    print("-------------------------")
    for k in d:
        print("\t{}--->{}".format(k,d[k]))
    print("-------------------------")
    for k in d:
        print("\t{}--->{}".format(k, d.get(k)))
    print("-------------------------")
    for k,v in d.items():
        print("\t{}--->{}".format(k, v))
    print("-------------------------")
    #Reverting the Dict Data
    rd={v:k for k,v in d.items()}
    for k,v in rd.items():
        print("\t{}--->{}".format(k, v))
