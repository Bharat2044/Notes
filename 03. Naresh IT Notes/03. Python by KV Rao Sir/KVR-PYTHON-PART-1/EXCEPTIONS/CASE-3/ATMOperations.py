#ATMOperations.py<--File Name and Module Name
from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.00
def deposit():
    damt=float(input("Enter Ur Deposit Amount:")) # ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxxx123 Credited with INR:{}".format(damt))
        print("Ur Account xxxxxx123 Bal:{}".format(bal))
def withdraw():
    global bal
    wamt = float(input("Enter Ur Withdraw Amount:"))#ValueError
    if(wamt<=0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxx123 Debited with INR:{}".format(wamt))
        print("Ur Account xxxxxx123 Bal:{}".format(bal))

def balenq():
    print("Ur Account xxxxxx123 Bal:{}".format(bal))