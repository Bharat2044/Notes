#Program for Renaming a File
#To Rename a File , we use rename() of os module
#Syntax: os.rename("Old File Name","New File Name")
#RenameFile.py
import os
try:
    os.rename("D:\\SUB\\kv.py","D:\\SUB\\hyd.py")
    print("File Name Renamed--verify")
except FileNotFoundError:
    print("Source File Name does not Exist")
