#Program for Displaying the content of any File
#FileReadEx3.py
def filedisplay():
    filename=input("Enter the file name to display its content:")
    try:
        with open(filename,"r") as fp:
            filedata=fp.read()
            print("----------------------------------")
            print("Content of:'{}' ".format(fp.name))
            print("----------------------------------")
            print(filedata)
            print("----------------------------------")
    except FileNotFoundError:
        print("File does not Exist")
#Main Program
filedisplay()