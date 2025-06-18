#Program for Demonstrating Key Word Arguments
#KeywordArgsEx1.py
def  disp(a,b,c,d):
      print("\t{}\t{}\t{}\t{}".format(a,b,c,d))

#Main program
print("-------------------------------------")
print("\tA\tB\tC\tD")
print("-------------------------------------")
disp(10,20,30,40) # Function Call with Positional Params
disp(10,20,d=40,c=30) # Function Call with Positional Params with Keyword args
disp(c=30,d=40,a=10,b=20)# Function Call with Keyword args
disp(c=30,d=40,a=10,b=20) # Function Call with Keyword args
print("-------------------------------------")
