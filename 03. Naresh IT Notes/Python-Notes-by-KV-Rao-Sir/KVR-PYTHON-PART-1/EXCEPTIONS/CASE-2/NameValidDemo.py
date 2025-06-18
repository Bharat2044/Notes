#NameValidDemo.py
from NameExcept import InvalidNameError
from NameValidation import validate
while(True):
    try:
        name=input("Enter Ur Name/place/product:")
        res=validate(name)
    except InvalidNameError:
        print("{} is Invalid Name, Try again".format(name))
    else:
        print(res)
        break
