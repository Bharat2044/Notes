#Program for Reading the Data from CSV File
#CSVReadEx2.py
import csv
try:
    with open("E:\\KVR-PYTHON-7AM\\CSV\\NOTES\\student.csv") as fp:
        csvro=csv.reader(fp)
        for record in csvro:
            for val in record:
                print("{}".format(val),end="\t")
            print()
except FileNotFoundError:
    print("CSV File does not Exist")
