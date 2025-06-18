#Program for accepting a Line of Text and get words and their length
#CountWordsLength.py
line=input("Enter Line of Text:")
words=line.split() # words=['Python', 'is', 'an', 'OOP', 'Lang']
for word in words:
    print("{}--->{}".format(word,len(word)))
