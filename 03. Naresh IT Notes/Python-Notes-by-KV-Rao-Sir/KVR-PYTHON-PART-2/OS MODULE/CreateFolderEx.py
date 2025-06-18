#Program for Creating a Single Folder
#To Create a Single Folder, we use mkdir() of os module
#Syntax:   os.mkdir(Folder name)
#CreateFolderEx.py
import os
try:
    os.mkdir("c:\\INDIA\\TS")
    print("Folder Created Sucessfully")
except FileExistsError:
    print("Folder Alerady Created")
except FileNotFoundError:
    print("Folder Does not Exist")