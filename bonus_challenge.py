paragraph = 'To be or not to be'
wordCount = {}
splitParagraph = paragraph.split()
for word in splitParagraph:
    wordCount[word] = wordCount.get(word, 0) + 1

#sorted lists them in ascending order
#print sorted(wordCount.values())


#sorted lists whatever is asked for in ascending order
#reverse makes it descending order (the reverse of ascending order)
winners = sorted(wordCount, key=wordCount.__getitem__, reverse=True)

#print winners

#This creates an empty list
winnerString = []

#This appends first three items of winners into the empty list
for word in range(3):
    winnerString.append(winners[word])

print winnerString
