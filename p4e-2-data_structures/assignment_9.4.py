'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

fileName = input('Enter file name: ') 

if len(fileName) < 1 or not fileName.endswith('.txt'): fileName = 'mbox-short.txt'

try:
    fileHandler = open(fileName)

    senders = dict()
    for line in fileHandler:
        if line.startswith('From '):
            sender = line.split()[1]
            senders[sender] = senders.get(sender, 0) + 1

    moreOftenSender = None
    for sender in senders:
        if moreOftenSender is None or senders[sender] > senders[moreOftenSender]: moreOftenSender = sender

    # Using items() method
    # times = -1
    # for sender,count in senders.items():
    #     if moreOftenSender is None or count > times: 
    #         times = count
    #         moreOftenSender = sender

    print(moreOftenSender, senders[moreOftenSender])

except FileNotFoundError:
    print(f'The file {fileName} could\'t be opened')
except:
    print('Oops, something went wrong')