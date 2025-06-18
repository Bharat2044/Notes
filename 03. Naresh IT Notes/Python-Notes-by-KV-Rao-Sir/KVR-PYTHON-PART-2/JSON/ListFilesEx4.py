#Program for Listing the Python Files in a Folder
#ListFilesEx4.py
import os
try:
    FolderName=input("Enter the Folder Name to List the Files:")
    FileList=os.listdir(FolderName)
    print("----------------------------")
    nop=0
    for file in FileList:
        if(file[-4:]==".csv"):
            print("\t{}".format(file))
            nop=nop+1
    print("----------------------------")
    print("Total Number of Files=",len(FileList))
    print("Number of CSV  Files=",nop)
    print("----------------------------")
except FileNotFoundError:
    print("Folder Does not Exist")