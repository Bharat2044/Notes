#Program for Removing the Folders Hierarchy
#To Remove the Folders Hierarchy, we juse removedirs() os module
#Syntax:  os.removedirs(Folders Hierarchy)
#DeleteFoldersHierarchyEx.py
import os
try:
    os.removedirs("C:\\KVR\\PYTHON")
    print("Folder Hierarchy Removed--Verify")
except FileNotFoundError:
    print("Folder Does not Exist")
except OSError:
    print("Folder is not empty")


