# Find the two entries that sum to 2020; what do you get if you multiply them together?

# import file into array of ints
list_ = open("input.txt").read().split()
numbers_list = []
for line in list_:
    numbers_list.append(int(line.strip('\n')))

for numberA in list_:
    for numberB in list_:
        if int(numberA) + int(numberB) == 2020:
            print('yaaaas, found it')
            print(int(numberA) * int(numberB))
