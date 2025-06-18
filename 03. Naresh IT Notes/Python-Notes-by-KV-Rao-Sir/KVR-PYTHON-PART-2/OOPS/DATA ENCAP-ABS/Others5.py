#Others5.py----Data Abstraction
#from Account5 import Account---Gives  ImportError
from Account5 import __Account

ac=__Account()
ac.getAccDet()
print(ac.__dict__)