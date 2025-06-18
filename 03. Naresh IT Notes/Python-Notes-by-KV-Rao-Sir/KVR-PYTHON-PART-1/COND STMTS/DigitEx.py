#Program for accepting any digit and display its name
#DigitEx.py
dictobj={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE",-1:"-ONE",-2:"-TWO",-3:"-THREE",-4:"-FOUR",-5:"-FIVE",-6:"-SIX",-7:"-SEVEN",-8:"-EIGHT",-9:"-NINE"}
d=int(input("Enter any Digit:")) # d=0 1 2 3 4 5 6 7 8 9
res= dictobj.get(d)  if dictobj.get(d)!=None  else "+VE NUMBER" if d>9 else "-VE NUMBER"
print("{} is {}".format(d,res))