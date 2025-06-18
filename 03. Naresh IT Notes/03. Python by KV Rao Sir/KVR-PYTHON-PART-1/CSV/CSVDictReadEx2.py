#Program for Reading the Data from CSV File
#CSVDictReadEx2.py
import csv
try:
    with open("E:\\KVR-PYTHON-7AM\\CSV\\NOTES\\hydstudent.csv") as fp:
        csvdro=csv.DictReader(fp) # here csvdro is an object of <class,csv.DictReader>
        for record in csvdro: # Here record is an object <class, Dict>
            for k,v in record.items():
                print("{}-->{}".format(k,v))
            print()
            print("------------------------------")
except FileNotFoundError:
    print("CSV File does not Exist")
