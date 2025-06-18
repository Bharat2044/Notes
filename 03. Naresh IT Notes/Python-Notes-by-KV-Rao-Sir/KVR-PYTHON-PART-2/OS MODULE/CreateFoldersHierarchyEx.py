#Program for Creating   Folder Hierarchy
#To Create Folder Hierarchy, we use makedirs() of os module
#Syntax:   os.makedirs(Folder Hierarchy)
#CreateFoldersHierarchyEx.py
import os
try:
    os.makedirs("D:\\KVR\\HYD\\PYTHON")
    print("Folders hierarchy Created--Verify")
except FileExistsError:
    print("Folders Hierarchy already exist")