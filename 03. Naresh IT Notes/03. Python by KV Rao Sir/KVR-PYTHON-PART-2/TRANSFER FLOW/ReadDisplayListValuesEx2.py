#Read n values and place them in list and display the values
#ReadDisplayListValuesEx1.py
import sys
print("Enter List of Values (to stop press @ ):")
lst=list()
while(True):
    value=input()
    if(value!='@'):
        lst.append(float(value))
    else:
        print("List of Values:{}".format(lst))
        print("Thx for using program!!!")
        sys.exit()
