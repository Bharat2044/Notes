#DynamicCSVWriteEx2.py--Dict of List
import csv
csvfile=input("Enter CSV File Name with an extension.csv:")
print("Enter How Many ColNames u want for '{}' File".format(csvfile))
noc=int(input())
if(noc<=0):
    print("{} Invalid Number of Columns".format(noc))
else:
    #accept the columns names
    hnames=[]
    for i in range(1,noc+1):
        colname=input("Enter Col Name:{} for '{}' File:".format(i,csvfile))
        hnames.append(colname)
    else:
        #hnames=['EID', 'NAME', 'SAL', 'DSG']
        nor=int(input("Enter How Many Records u want to Enter for '{} File:".format(csvfile)))
        if(nor<=0):
            print("{} Invalid Number of Records:")
        else:
            records = list()  # For Holdling Inner List called Records
            for i in range(1,nor+1):
                print("------------------------------------")
                print("Enter {} Records Values:".format(i))
                print("------------------------------------")
                rec=dict() # For Taking Record Values
                for j in range(len(hnames)):
                    val=input("Enter Value for '{}':".format(hnames[j]))
                    rec[hnames[j]]=val
                else:
                    records.append(rec)
            else:
                with open(csvfile,"a") as fp:
                    csvdwr=csv.DictWriter(fp,fieldnames=hnames)
                    csvdwr.writeheader()
                    csvdwr.writerows(records)
                    print("CSV File Created and Records written to the CSV File")



















