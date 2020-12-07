import csv

# How many passwords are valid according to their policies?
# number of times a letter can be present

with open('input.csv', 'r') as inputFile:
    lines=csv.reader(inputFile, delimiter=' ')
    i=0
    for line in lines:
        # ['4-6', 'b:', 'bhbbbrhbb']

        pw=line[2]
        lenMinS = line[0].split('-')[0]
        lenMaxS = line[0].split('-')[1]
        lenMin = int(lenMinS)
        lenMax = int(lenMaxS)
        pwLetter = line[1].split(':')[0]

        if pwLetter in pw:
            if pw.count(pwLetter) >= lenMin and pw.count(pwLetter) <= lenMax:
                i+=1
    print(i)
