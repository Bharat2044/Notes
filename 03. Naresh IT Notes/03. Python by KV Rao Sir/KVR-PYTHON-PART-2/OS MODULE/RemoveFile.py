#Program for Removing  a File
#To Remove a File , we use remove() of os module
#Syntax: os.remove("File Name")
#RemoveFile.py
import os
try:
    os.remove("D:\\SUB\\kvr.py")
    print("File Name Removed --verify")
except FileNotFoundError:
    print("File Name does not Exist")