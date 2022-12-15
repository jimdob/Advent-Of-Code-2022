#Advent of Code 2022 Day 4 Solution

with open("day4input.txt", "r") as f:

    ranges = f.read().splitlines()

    overlappingRanges = 0   #count variable for part 1
    overlappingPairs = 0    #count variable for part 2

    #Each list element is a pair of ranges.
    #Split the element into the two ranges, split the range into two integers.
    for i in ranges:
        x,y = i.split(',')

        x0,x1 = [int(n) for n in x.split('-')]
        y0,y1 = [int(n) for n in y.split('-')]

        #PART 1
        #Compare the integers to determine if one range fully contains the other. Count.
        if (x0 <= y0 and x1 >= y1) or (y0 <= x0 and y1 >= x1):
            overlappingRanges += 1
            overlappingPairs += 1

        #PART 2
        elif (y0 <= x0 <= y1) or (y0 <= x1 <= y1):
            overlappingPairs += 1


    print('Part 1 number of overlapping assignment ranges is:',overlappingRanges)
    print('Part 2 number of overlapping assignment pairs is:',overlappingPairs)
