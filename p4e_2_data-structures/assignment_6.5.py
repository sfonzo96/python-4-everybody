print("Excersise 6.5 from P4E:")

str = 'X-DSPAM-Confidence: 0.8475'

colonPosition = str.find(':')
slicedNumber = str[colonPosition + 2:]

print(float(slicedNumber))