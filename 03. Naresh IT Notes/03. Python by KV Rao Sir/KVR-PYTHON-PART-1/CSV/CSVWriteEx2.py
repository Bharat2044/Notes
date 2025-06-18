#Program for Adding the Record to the Existing CSV File
#CSVWriteEx2.py
import csv # Step-1
record=[225,"Swapnil",77.89]
with open("E:\\KVR-PYTHON-7AM\\CSV\\NOTES\\student.csv","a") as fp: # Step-4
    csvwr=csv.writer(fp)
    csvwr.writerow(record)
    print("Records added to Existing CSV File--verify")
