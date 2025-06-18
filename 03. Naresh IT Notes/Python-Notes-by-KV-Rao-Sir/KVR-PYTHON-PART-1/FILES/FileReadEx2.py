#Program for Demonstrating How to Read the Data from File--readlines()
#FileReadEx2.py
try:
    with open("addr.info","r") as fp:
        filedata=fp.readlines()
        print("--------------------------------")
        for line in filedata:
            print(line,end="")
        print("--------------------------------")
except FileNotFoundError:
    print("File Does not Exist")
