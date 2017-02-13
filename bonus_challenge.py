def word_histogram(paragraph):
    wordCount = {}
    splitParagarph = paragraph.split()
    for word in splitParagarph:
        wordCount[word] = wordCount.get(word, 0) + 1
    print wordCount

word_histogram('To be or not to be')
