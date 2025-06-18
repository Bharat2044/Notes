#Program for Reading the Data from CSV File
#DynamicCSVReadEx1.py
import csv
try:
    with open(input("Enter CSV File Name with Complete Path:"),"r") as fp:
        csvro=csv.reader(fp)
        for record in csvro:
            for val in record:
                print("{}".format(val),end="\t")
            print()
except FileNotFoundError:
    print("CSV File does not Exist")