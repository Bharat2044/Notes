#Program for accepting a Line of Text and get words and their length
#MaxCountWordsLength.py
line=input("Enter Line of Text:")
words=line.split() # words=['Python', 'is', 'an', 'OOP', 'Lang']
wd=dict() # Creating empty dict for storing word and its length
for word in words:
    wd[word]=len(word)
else:
    #get the values from dict object
    vals=wd.values()
    maxlen=max(vals)#Obtaing Max Length value by using max()
    hslenwordds=list()
    for key,value in wd.items():
        if(value==maxlen):
            hslenwordds.append(key)
    else:
        print("Max Length Words")
        for words in hslenwordds:
            print(words)

