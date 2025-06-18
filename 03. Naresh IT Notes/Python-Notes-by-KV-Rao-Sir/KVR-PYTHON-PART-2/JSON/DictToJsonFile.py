#DictToJsonFile.py
import json
d={'sno': '100', 'name': 'ROSSUM', 'marks': '23.45'}
print(d,type(d))
with open("stud.json","a") as fp:
    json.dump(d,fp) # Transfer Dict Data to JSON File
    print("Diict Data Saved in Json File--verify")
