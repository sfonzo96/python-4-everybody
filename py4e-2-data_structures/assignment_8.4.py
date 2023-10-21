'''
8.4 Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''

fileName = input('Enter file name: ')

romeoHandler = open(fileName)

wordsList = list()

for line in romeoHandler:
    # Generates a list of words for each line
    wordsAtLine = line.rstrip().split()

    # Adds words to the wordsList without repeating
    for word in wordsAtLine:
        if (word not in wordsList): wordsList.append(word)

wordsList.sort()

print(wordsList)
