#Program for Listing the Files in a Folder
#ListFilesEx2.py
import os
try:
    FolderName=input("Enter the Folder Name to List the Files:")
    FileList=os.listdir(FolderName)
    print("----------------------------")
    for file in FileList:
        print("\t{}".format(file))
    print("----------------------------")
    print("Number of Files=",len(FileList))
    print("----------------------------")
except FileNotFoundError:
    print("Folder Does not Exist")