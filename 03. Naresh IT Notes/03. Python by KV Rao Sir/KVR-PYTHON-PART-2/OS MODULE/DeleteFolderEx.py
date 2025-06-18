#Program for Deleting a Single Folder
#To Delete Single Folder, we use rmdir() of os module
#Syntax: os.rmdir("Folder Name with Path")
#DeleteFolderEx.py
import os
try:
    os.rmdir("APPLE")
    print("Folder Deleted---Verify")
except FileNotFoundError:
    print("Folder Does not Exist")
except OSError:
    print("Folder is not empty")