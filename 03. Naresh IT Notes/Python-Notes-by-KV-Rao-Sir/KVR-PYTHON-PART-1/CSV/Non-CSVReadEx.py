#Non-CSVReadEx.py
try:
    with open("E:\\KVR-PYTHON-7AM\\CSV\\NOTES\\employee.csv") as fp:
        filedata=fp.read()
        print(filedata)
except FileNotFoundError:
    print("File Does Not Exist")