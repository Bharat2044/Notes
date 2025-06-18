#VoterEx2.py
while(True):
    age=int(input("Enter Age of Citizen:"))
    if(age<=17) or (age>100):
        print("\t{} Years Citizen is not Eligible Vote-try Again:".format(age))
    else:
        print("{} Years Citizen is  Eligible Vote:".format(age))
        break