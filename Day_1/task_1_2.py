# What is the product of the three entries that sum to 2020?

list_ = open("input.txt").read().split()
numbers_list = []
for line in list_:
    numbers_list.append(int(line.strip('\n')))

def tasktwo():
    for numberA in numbers_list:
        for numberB in numbers_list:
            for numberC in numbers_list:
                if numberA + numberB + numberC == 2020:
                    ans = numberA * numberB * numberC
                    return(ans)

print(tasktwo())