# Read the file and determine the sum of all number appearences

import re

fileName = input('Enter file: ')
if len(fileName) < 1: fileName = "regex_sum_1830010.txt"

fileHandler = open(fileName)
text = fileHandler.read()

# Looks for all strings or chars that match the regex '[0-9]+' (Numbers from 0 to 9, any amount of digits) in the 'text' string
# Retrieved as a list of strings 
numbers = re.findall('[0-9]+', text)

integers = list()
for number in numbers:
    integers.append(int(number))

print(sum(integers))
