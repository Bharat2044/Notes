#UniqueElements.py
class Words:
    def getvalues(self):
        print("Enter List of Values separated by space:")
        words=[word for word in input().split()]
        return words
    def getuniquevalues(self):
        words=self.getvalues() # words=[HYD BANG HYD BANG]
        uw=[] # Creating Empty List for storing unique vals
        for word in words:
            if word not in uw:
                uw.append(word)
        else:
            print("Given List=",words)
            print("Unique Values=",uw)

#Main Program
w=Words()
w.getuniquevalues()