#Program for Demonstrating Key Word Arguments
#KeywordArgsEx2.py
def  disp(a,b,c,d,city="HYD"):
      print("\t{}\t{}\t{}\t{}\t{}".format(a,b,c,d,city))

#Main program
print("-------------------------------------")
print("\tA\tB\tC\tD\tCity")
print("-------------------------------------")
disp(10,20,30,40) # Function Call with Positional Params
disp(10,20,d=40,c=30) # Function Call with Positional Params with Keyword args
disp(c=30,d=40,a=10,b=20)# Function Call with Keyword args
disp(c=30,d=40,a=10,b=20) # Function Call with Keyword args
disp(b=20,a=10,city="BANG",c=30,d=40) # Function Call with Keyword args
print("-------------------------------------")
