#Program for accpepting List of words and find their Length
#DictCompEx2.py
print("Enter List of Words separated by comma:")
d={word:len(word) for word in input().split(",") }
print(d)
print("-------------------------------")
print("\tWord\tLength")
print("-------------------------------")
for word,length in d.items():
    print("\t{}\t{}".format(word,length))
print("-------------------------------")