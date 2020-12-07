import csv

# Exactly one of these positions must contain the given letter.
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
            # print(pw.index(pwLetter)+1)
            # if pw.index(pwLetter) == lenMax:

                # print(pwLetter, lenMin, pw)
            if pw.index(pwLetter)+1 == lenMin or pw.index(pwLetter)+1 == lenMax:
                i+=1
    print(i)
