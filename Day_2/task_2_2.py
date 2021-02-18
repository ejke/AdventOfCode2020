import csv

# Each policy actually describes two positions in the password, 
# where 1 means the first character, 2 means the second character, and so on. 
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
# Exactly one of these positions must contain the given letter. 
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
with open('input.csv', 'r') as inputFile:
    lines=csv.reader(inputFile, delimiter=' ')
    f=0
    s=0
    b=0
    for line in lines:
        # print(line)
        # ['4-6', 'b:', 'bhbbbrhbb']

        pw=line[2]
        # print(pw)
        first_char_string = line[0].split('-')[0]
        second_char_string = line[0].split('-')[1]

        first_char = int(first_char_string)
        second_char = int(second_char_string)
        # print(first_char, second_char)

        first_char_mod = first_char-1
        second_char_mod = second_char-1
        # print(first_char_mod, second_char_mod)

        pwLetter = line[1].split(':')[0]
        # print(pwLetter)
        # print('----')
        if pwLetter in pw:
            # print('Char at index', first_char_mod, 'is :', pw[first_char_mod], '.Is it same as rule?', pwLetter == pw[first_char_mod], pwLetter)
            # print('Char at index', second_char_mod, 'is :', pw[second_char_mod])
            
            # if 
            if pwLetter == pw[first_char_mod]:
                print('Char at index', first_char_mod, 'is :', pw[first_char_mod], '.Is it same as rule?', pwLetter == pw[first_char_mod], pwLetter)
                # print('True')
            # and pw[second_char_mod] == pwLetter:
                f+=1

            if pwLetter == pw[second_char_mod]:
                print('Char at index', second_char_mod, 'is :', pw[second_char_mod], '.Is it same as rule?', pwLetter == pw[second_char_mod], pwLetter)
                s+=1

            if pwLetter == pw[first_char_mod] and pwLetter == pw[second_char_mod]:
                b+=1
    print('first', f)
    print('second', s)
    print('both', b)
    print('answer', f+s-b)