#Advent of Code 2022 Day 3 Solution

import string

with open('day3input.txt') as f:
    rucksacks = f.read().split()
    #print(rucksacks)

    #Split rucksack values into the 2 compartments (by splitting the strings in half). Assumes there are no strings with an odd number of characters.
    compartments = []
    for item in rucksacks:
        section1, section2 = item[:len(item)//2], item[len(item)//2:]
        compartments.append([section1, section2])
    #print(compartments)

    #Priority values. Imports alphabet from 'string' library and combines into a list
    priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    #PART 1

    part1Sum = 0
    #Compare the characters in each string (items in each compartment) with eachother, find the matching char, and sum the priority value
    for item in compartments:
        common = ''.join(set(item[0]).intersection(item[1]))
        part1Sum += priorities.index(common) + 1

    print('Part 1 sum of the matching item priorities is:',part1Sum)


    #PART 2

    part2Sum = 0
    groups = list(zip(*[iter(rucksacks)]*3))    #Group the list of rucksacks into groups of 3
    #Find the common character among the rucksacks in each group and sum the priority value
    for sacks in groups:
        common = list(set.intersection(*map(set,sacks)))
        part2Sum += priorities.index(common[0]) + 1
    print('Part 2 sum of the matching item priorities is:',part2Sum)
