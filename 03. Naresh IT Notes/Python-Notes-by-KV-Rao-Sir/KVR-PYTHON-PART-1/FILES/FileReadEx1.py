#Program for Demonstrating How to Read the Data from File--read()
#FileReadEx1.py
try:
    with open("Hyd.info","r") as fp:
        filedata=fp.read()
        print("--------------------------------")
        print(filedata)
        print("--------------------------------")
except FileNotFoundError:
    print("File Does not Exist")
