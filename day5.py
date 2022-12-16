#Advent of Code 2022 Day 5 Solution

with open("day5input.txt", "r") as f:

    stackStrings,instructions = (i.splitlines() for i in f.read().split('\n\n'))
    
    # Create dictionary with stack number as the key, and empty integer list as the value
    stacks = {int(digit):[] for digit in stackStrings[-1].replace(' ','')}
    stacksP2 = {int(digit):[] for digit in stackStrings[-1].replace(' ','')}


    # Get indices of the crate numbers
    indices = [index for index, char in enumerate(stackStrings[-1]) if char != ' ']

    # Insert the crate values into their respective stacks in order
    for string in stackStrings[:-1]:
        stackNum = 1
        for index in indices:
            if string[index] != ' ':
                stacks[stackNum].insert(0, string[index])
                stacksP2[stackNum].insert(0, string[index])
            stackNum += 1

    # PART 1

    # Perform all moves specified in 'instructions' by popping crates from one stack and appending to the other.
    for instruction in instructions:
        instruction = instruction.split()
        moveQty,start,finish = int(instruction[1]),int(instruction[3]),int(instruction[5])
        i = 0
        while i < moveQty:
            crate = stacks[start].pop()
            stacks[finish].append(crate)
            i += 1

    # PART 2

    # Perform all moves specified in 'instructions' but maintain the order of the moved crates (grab multiple crates at once)
    for instruction in instructions:
        instruction = instruction.split()
        moveQty,start,finish = int(instruction[1]),int(instruction[3]),int(instruction[5])

        crates = stacksP2[start][-moveQty:]           # add crates to be moved to temp list
        stacksP2[start] = stacksP2[start][:-moveQty]  # remove crates to be moved from source stack

        for crate in crates:                        
            stacksP2[finish].append(crate)            # add crates to destination stack
        
    # Display stacks and contents
    print('\nPART 1 STACKS\n')
    for stack in stacks:
        print(stack, stacks[stack])
    print('\nPART 2 STACKS\n')
    for stack in stacksP2:
        print(stack, stacksP2[stack])
    print()