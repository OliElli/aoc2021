#!/usr/bin/env python3

file = 'input.txt'
horizontal = 0
depth = 0

with open(file) as f:
    input = f.read().splitlines()

for line in input:
    direction = line.split(' ')[0]
    distance = line.split(' ')[1]

    if direction == 'forward':
        horizontal += int(distance)
    elif direction == 'down':
        depth += int(distance)
    elif direction == 'up':
        depth -= int(distance)

print(horizontal)
print(depth)
print(horizontal * depth)