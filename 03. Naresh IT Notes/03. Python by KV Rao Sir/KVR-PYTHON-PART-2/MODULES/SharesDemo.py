#SharesDemo.py--View Program
import Shares,time,importlib
def dispshares(d):
    print("*"*50)
    print("Share Name\t\tShare Value")
    print("*" * 50)
    for sn,sv in d.items():
        print("\t{}\t\t{}".format(sn,sv))
    print("*" * 50)
#main program
d=Shares.sharesinfo()
dispshares(d)
print("I am going to sleep for 15 Seconds")
time.sleep(20)
print("I am coming out off sleep after 15 Seconds")
importlib.reload(Shares)
d=Shares.sharesinfo()
dispshares(d)
print("I am going to sleep for 15 Seconds")
time.sleep(20)
print("I am coming out off sleep after 15 Seconds")
importlib.reload(Shares)
d=Shares.sharesinfo()
dispshares(d)