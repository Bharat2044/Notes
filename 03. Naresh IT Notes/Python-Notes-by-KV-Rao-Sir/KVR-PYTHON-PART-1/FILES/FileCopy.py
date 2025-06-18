#Program for Copying the content of One file into another File
def filecopy():
    try:
        srcfile=input("Enter Source File:")
        with open(srcfile,"r") as rp:
            dstfile=input("Enter Destnation File:")
            if(srcfile==dstfile):
                print("Danger Source and Destination Files")
            else:
                with open(dstfile,"w") as wp:
                    #Read the Data from SOURCE FILE
                    srcfiledata=rp.read()
                    #Write the srcfiledata to Destination File
                    wp.write(srcfiledata)
                    print("File Copied--Verify")

    except FileNotFoundError:
        print("Source File Does not Exist")

#Main program
filecopy()