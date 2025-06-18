#JsonToDict.py
import json
jsonstrdata='{"sno":"100","name":"ROSSUM","marks":"23.45"}'
print(jsonstrdata,type(jsonstrdata))
print("-------------------------------------------")
#Convert Json Str Data into Dict Object
dobj=json.loads(jsonstrdata)
for key,val in dobj.items():
    print("\t{}-->{}".format(key,val))
print("-------------------------------------------")
#Again Convert Dict Object into str format by using str()
sdict=str(dobj)
print(sdict,type(sdict))