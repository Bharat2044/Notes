#Program for finding Sum of Squares N Natural Numbers where n is +ve
#ForLoopEx8.py
n=int(input("Enter How Many Natural Numbers Squares Sum u want:"))
if(n<=0):
    print("\t{} is Invalid".format(n))
else:
    print("-----------------------------------------------------")
    print("Nat Nums\t\tSquares")
    print("-----------------------------------------------------")
    ss=0 # for the purpose of Accumuting Squares sum
    s=0 # for the purpose of Accumuting Nat nums sum
    for i in range(1,n+1):
        ss=ss+i**2
        s=s+i
        print("\t{}\t\t\t\t\t{}".format(i,i**2))
    else:
        print("-----------------------------------------------------")
        print("\t{}\t\t\t\t\t{}".format(s,ss))
        print("-----------------------------------------------------")


