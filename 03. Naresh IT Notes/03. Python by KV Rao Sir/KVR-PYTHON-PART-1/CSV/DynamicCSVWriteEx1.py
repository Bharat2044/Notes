#DynamicCSVWriteEx1.py--List of List--inner list
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
                print("Enter {} Records Values:".format(i))
                print("------------------------------------")
                rec=list() # For Taking Record Values
                for j in range(len(hnames)):
                    val=input("Enter Value for '{}':".format(hnames[j]))
                    rec.append(val)
                else:
                    records.append(rec)
            else:
                #Save the CSV File Data
                with open(csvfile,"a") as fp:
                    csvwr=csv.writer(fp)
                    csvwr.writerow(hnames)
                    csvwr.writerows(records)
                    print("CSV File Created and Records Written --Verify")

















