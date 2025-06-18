#Program for Listing the Files in a Folder
#ListFilesEx1.py
import os
FileList=os.listdir("E:\\KVR-PYTHON-7AM\\CSV")
print("----------------------------")
for file in FileList:
    print("\t{}".format(file))
print("----------------------------")
print("Number of Files=",len(FileList))
print("----------------------------")