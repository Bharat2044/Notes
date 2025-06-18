#SISProjectDemo.py
from SISMenu import menu
from SISInsert import recordinsert
from SISDeleteEx import deleterecord
from SISUpdate import updaterecord
from SISSelect import selectrecords
from SISViewRecords import viewrecords
while(True):
    menu()
    ch=int(input("Enter Ur Choice:"))
    try:
            match(ch):
                case 1:
                    recordinsert()
                case 2:
                    deleterecord()
                case 3:
                    updaterecord()
                case 4:
                    selectrecords()
                case 5:
                    viewrecords()

                case 6:
                    print("Thx for using Program")
                    break
                case _:
                    print("Ur Selection of Operation is wrong-try again")
    except ValueError:
            print("Don't Enter Alnums,str,symbols for Choice of Operation")
