#NameValidation.py
from NameExcept import InvalidNameError
def validate(name): # name=Dheerendar Kumar Jain
    words=name.split() # words=[Dheerendar,Kum1ar, Jain]
    res=False
    for word in words:
        if(not word.isalpha()):
            res=True
            break
    if(res):
        raise InvalidNameError
    else:
        return("'{}'is Valid Name".format(name))




