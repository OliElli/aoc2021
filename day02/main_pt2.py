#!/usr/bin/env python3

file = 'input.txt'
horizontal = 0
depth = 0
aim = 0

with open(file) as f:
    input = f.read().splitlines()

for line in input:
    direction = line.split(' ')[0]
    distance = line.split(' ')[1]

    if direction == 'forward':
        horizontal += int(distance)
        depth += int(distance) * aim
    elif direction == 'down':
        aim += int(distance)
    elif direction == 'up':
        aim -= int(distance)

print(horizontal)
print(depth)
print(horizontal * depth)