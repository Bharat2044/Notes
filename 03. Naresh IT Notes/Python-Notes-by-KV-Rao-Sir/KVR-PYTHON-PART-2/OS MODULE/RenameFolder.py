#Program for Renaming a Folder
#To Rename a Folder , we use rename() of os module
#Syntax: os.rename("Old Folder","New Folder Name")
#RenameFolder.py
import os
try:
    os.rename("D:\\KVR","D:\\ROSSUM")
    print("Folder Renamed--verify")
except FileNotFoundError:
    print("Source Folder does not Exist")
