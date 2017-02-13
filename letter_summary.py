def letter_histogram(word):
    letterDict = {}
    for char in word:
        #The key is the character
        #The value is given the default value of 0 if it is not there
        #The value is then given + 1 to increase it
        #The key-value pair is the letter and the number of times it appears
        letterDict[char] = letterDict.get(char, 0) + 1

    print letterDict

letter_histogram('banana')

#This is a dynamic dictionary because it is made after the program is run
