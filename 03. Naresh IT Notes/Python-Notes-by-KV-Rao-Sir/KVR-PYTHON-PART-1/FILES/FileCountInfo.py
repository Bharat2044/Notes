#Program for Counting Number of Lines, words and Chars of any file
#FileCountInfo.py
filename=input("Enter File Name to count number of Lines, words and chars:")
with open(filename,"r") as fp:
    filedata=fp.readlines() # filedata=['Hyd is the\n', 'Cap of TS']
    nol,nw,noc=0,0,0
    for line in filedata:
        noc=noc+len(line)
        nw=nw+len(line.split())
        nol=nol+1
    else:
        print("--------------------")
        print("Number of Lines=",nol)
        print("Number of words=",nw)
        print("Number of Chars=",noc)
        print("--------------------")
