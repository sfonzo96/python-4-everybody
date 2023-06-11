'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

fileName = input("Enter file: ")

if len(fileName) < 1: fileName = "mbox-short.txt"

fileHandler = open(fileName) 

hours = dict()
for line in fileHandler:
    if line.startswith('From '):
        words = line.rstrip().split()
        time = next((datetime for datetime in words if ':' in datetime), None)
        if time is not None: 
            hour = time.split(':')[0]
            hours[hour] = hours.get(hour, 0) + 1
        else:
            continue

for hour,count in sorted(hours.items()):
    print(hour, count)
