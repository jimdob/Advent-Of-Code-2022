#Advent of Code 2022 Day 6 Solution

with open("day6input.txt", "r") as f:
    signal = f.read()

def findMarker(buffer,markerLength):
    for i in range(len(buffer) - markerLength - 1):
        marker = buffer[i:i + markerLength]
        if len(set(marker)) == markerLength:
            return i + markerLength

print('Part 1 marker position:',findMarker(signal,4))
print('Part 2 marker position:',findMarker(signal,14))