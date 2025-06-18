#Program for Reading the Data Dynamically from KBD and write it to the file
#DynamicWriteEx.py
print("Enter the Data to write to the File and press @ to stop:")
with open("Addr.info","a") as fp:
    while(True):
        kbddata=input()
        if(kbddata!="@"):
            fp.write(kbddata+"\n")
        else:
            print("Data Written to the File--verify")
            break





