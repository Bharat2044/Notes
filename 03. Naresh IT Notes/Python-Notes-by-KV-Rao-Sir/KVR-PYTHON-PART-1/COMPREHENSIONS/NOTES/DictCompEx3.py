#Program for accpepting List of words and find their Length
#DictCompEx3.py
print("Enter List of Words separated by comma:")
x=dict([(word,len(word)) for word in input().split(",")])
#Here we are converting tuples of List into dict type by using dict()
print(x,type(x))
print("-------------------------------")
print("\tWord\tLength")
print("-------------------------------")
for word,length in x.items():
    print("\t{}\t{}".format(word,length))
print("-------------------------------")