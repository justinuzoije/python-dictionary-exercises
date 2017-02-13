#The important function is split()
#You can eliminate all whitespace in a string and makes a list of each word

def word_histogram(paragraph):
    wordCount = {}
    splitParagarph = paragraph.split()

    for word in splitParagarph:
        wordCount[word] = wordCount.get(word, 0) + 1
    print wordCount


word_histogram('To be or not to be')

#sentence = 'To be or not to be'



#This counts the number of letters
# def word_histogram(paragraph):
#     letterCount = {}
#     for char in paragraph:
#         if char != " ":
#             letterCount[char] = letterCount.get(char, 0) + 1
#     print letterCount
#
# word_histogram('To be or not to be')
