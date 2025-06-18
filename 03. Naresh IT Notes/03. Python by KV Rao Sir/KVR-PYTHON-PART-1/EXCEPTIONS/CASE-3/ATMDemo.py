#ATMDemo.py
from ATMMenu import menu
from ATMExcept import DepositError,WithDrawError,InSuffFundError
from ATMOperations import deposit,withdraw,balenq
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("Don't Try Deposit -Ve and Zero Value")
                except ValueError:
                    print("Don't try to Deposit alnums,strs and symbols")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("Don't Try Withdraw -Ve and Zero Value")
                except ValueError:
                    print("Don't try to WithDraw alnums,strs and symbols")
                except InSuffFundError:
                    print("U Account does not have funds--read python notes")
            case 3:
                balenq()
            case 4:
                print("Thx for using Program")
                break
            case _:
                print("Ur Selection of Operation is wrong--try again")
    except ValueError:
        print("Don't enter strs, alnums,and symbols for choice:-try again")
