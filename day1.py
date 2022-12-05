#Advent of Code 2022 Day 1 solution

with open('day1input.txt') as f:
    groups = [line.split('\n') for line in [group.strip() for group in f.read().split("\n\n")]]
    calories = [[int(x) for x in lst] for lst in groups]
    #print(calories)

    #PART 1
    mostCals = 0
    for elf in calories:
        mostCals = max(sum(elf), mostCals)

    print('Part 1 answer:')
    print('The Elf carrying the most calories is carrying:',mostCals,'calories.')

    #PART 2

    #Solution below sums the list entries and then sorts from largest to smallest.

    totalCals = [sum(cals) for cals in calories]
    totalCals = sorted(totalCals, reverse=True)
    #print(totalCals)

    print('Part 2 answer:')
    print('The top three Elves are carrying a total of:',totalCals[0]+totalCals[1]+totalCals[2],'calories.')