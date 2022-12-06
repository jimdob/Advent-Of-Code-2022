#Advent of Code 2022 Day 4 Solution

with open('day4input.txt') as f:
    # Parse the input and create a list of tuples

    ranges = []
    for group in f.read().splitlines():
        pair = group.split(',')
        for x in pair:
            y = tuple(map(int, x.split('-')))
            ranges.append(y)
    
    print(ranges)

    overlappingRanges = 0
    


    # Return the result
    print(overlappingRanges)
