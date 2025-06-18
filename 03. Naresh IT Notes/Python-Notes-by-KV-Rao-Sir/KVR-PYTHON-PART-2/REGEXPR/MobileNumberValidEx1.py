#Program for Validating Mobile Number
#MobileNumberValidEx1.py
import re
while(True):
	mno=input("Enter Ur Mobile Number:")
	if (len(mno)==10):
		res=re.search(r"\d{10}",mno)
		if(res!=None):
			print("{} is Valid Mobile Number".format(mno))
			break
		else:
			print("\tMobile Number Should Not Contain Non-Ints--try again")
	else:
		print("\t{} is Invalid mobile Number due to wrong length-try again".format(mno))
