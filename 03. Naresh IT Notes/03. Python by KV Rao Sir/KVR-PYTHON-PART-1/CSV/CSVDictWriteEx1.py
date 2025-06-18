##Program for Creating CSV File from Dict Object Data
#CSVDictWriteEx1.py
import csv
hnames=["SNO","NAME","MARKS"] # Step-2
records=[ {"SNO":100,"NAME":"RS","MARKS":88.88},
          {"SNO":200,"NAME":"TR","MARKS":45.67},
          {"SNO":300,"NAME":"DR","MARKS":33.33},
        ]
with open("E:\\KVR-PYTHON-7AM\\CSV\\NOTES\\hydstudent.csv","a") as fp: # Step-4
    csvdwr=csv.DictWriter(fp,fieldnames=hnames)
    csvdwr.writeheader()
    csvdwr.writerows(records)
    print("CSV File Created and Data Written--verify")

