#Program for validating the name of person,place and product
name=input("Enter Any Name:")# Name=Guido Van Rossum
namewords=name.split()
res=True
for word in namewords:
    if( not word.isalpha()):
        res=False
        break
if(res):
    print("{} is Valid Name:".format(name))
else:
    print("{} Is Invalid Name".format(name))
