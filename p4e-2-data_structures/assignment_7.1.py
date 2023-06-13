'''
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
'''

fileName = input('Enter a file name: ')

try:
    # Makes the file available
    fileHandler = open(fileName)
    # Reads the data in the file and stores it all in one string
    content = fileHandler.read().rstrip()
    print(content.upper())
except:
    print('File cannot be opened:', fileName)
    quit()
