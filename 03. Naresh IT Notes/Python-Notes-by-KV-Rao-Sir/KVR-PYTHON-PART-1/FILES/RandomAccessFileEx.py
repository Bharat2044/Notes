#Program for Demonstrating Random access Files
#tell()--->Gives Index of File Pointer
#seek()--->Makes the File Pointer to point to Perticular Valid Index to Data of File
#RandomAccessFileEx.py
try:
    with open("addr.info","r") as fp:
        print("---------------------------")
        print("Initial Position of fp=",fp.tell())
        fd=fp.read(5)
        print(fd)
        print("Now Position of fp=", fp.tell())
        print("---------------------------")
        fd = fp.read(4)
        print(fd)
        print("Now Position of fp=", fp.tell())
        print("---------------------------")
        fd = fp.read(7)
        print(fd)
        print("Now Position of fp=", fp.tell())
        print("---------------------------")
        fd=fp.read()
        print(fd)
        print("Now Position of fp=", fp.tell()) # 170
        print("---------------------------")
        fd = fp.read()
        print(fd)
        print("Now Position of fp=", fp.tell())
        print("---------------------------")
        fp.seek(0)
        print("---------------------------")
        fd = fp.read(2)
        print(fd)
        print("Now Position of fp=", fp.tell())
        print("---------------------------")
except FileNotFoundError:
    print("File Does not Exist")
