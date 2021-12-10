#!/usr/bin/env python3

file = 'input.txt'
with open(file) as f:
    input = f.read().splitlines()

fish = input[0].split(',')
for i in range(0, len(fish)):
    fish[i] = int(fish[i])

value_map = {}
for i in range(0, 9):
    value_map[i] = 0
for i in fish:
    value_map[i] += 1

count = 0
for i in range(0, 256):
    value_map_copy = value_map.copy()
    for key, value in value_map.items():
        if key == 6:
            value_map_copy[6] = value_map[7] + value_map[0]
        elif key == 8:
            value_map_copy[8] = value_map[0]
        else:
            value_map_copy[key] = value_map[key + 1]
    value_map = value_map_copy
    count += 1

print(sum(value_map.values()))
