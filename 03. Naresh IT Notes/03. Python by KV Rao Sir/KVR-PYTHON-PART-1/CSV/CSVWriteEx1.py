#Program for Creating CSV File
#CSVWriteEx1.py
import csv # Step-1
hnames=["SNO","NAME","MARKS"] # Step-2
records= [[100,"RS",88.88],
            [200,"TR",45.67],
            [300,"DR",33.33],
          [400,"ST",66.45],
          [500,"SR",11.11] ]# Step-3
with open("E:\\KVR-PYTHON-7AM\\CSV\\NOTES\\student.csv","a") as fp: # Step-4
    csvwr=csv.writer(fp) # Step-5--here csvwr is an object of <class,csv.writer>
    csvwr.writerow(hnames) # Step-6
    csvwr.writerows(records) # Step-7
    print("CSV File Created and Data Written--verify")









