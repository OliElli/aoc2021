#!/usr/bin/env python3

file = 'input.txt'
count = 0

with open(file) as f:
    input = f.read().splitlines()

for i in range(0, len(input)):
    if i < len(input) - 3:
        value1 = int(input[i]) + int(input[i+1]) + int(input[i+2])
        value2 = int(input[i+1]) + int(input[i+2]) + int(input[i+3])
        if value1 < value2:
            count = count + 1

print(count)