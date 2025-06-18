#Program for finding Sum of N Natural Numbers where n is +ve
#ForLoopEx7.py
n=int(input("Enter Howe Many Natural Numbers Sum u want:"))
if(n<=0):
    print("\t{} is Invalid".format(n))
else:
    print("-----------------------------------------------------")
    print("Natural Numbers within:{}".format(n))
    print("-----------------------------------------------------")
    s=0 # for the purpose of Accumuting sum
    for i in range(1,n+1):
        s=s+i
        print("\t{}".format(i))
    else:
        print("-----------------------------------------------------")
        print("Sum of {} Natural Numbers={}".format(n, s))
        print("-----------------------------------------------------")


