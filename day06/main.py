#!/usr/bin/env python3

file = 'input.txt'
with open(file) as f:
    input = f.read().splitlines()

fish = input[0].split(',')
for i in range(0, len(fish)):
    fish[i] = int(fish[i])
count = 0
while True:
    for i in range(0, len(fish)):
        if fish[i] == 0:
            fish.append(8)
            fish[i] = 7
        fish[i] -= 1
    count += 1
    if count == 80:
        break

print(len(fish))
