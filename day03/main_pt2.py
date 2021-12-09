#!/usr/bin/env python3

file = 'input.txt'

with open(file) as f:
    input = f.read().splitlines()

def more_ones(list, truth):
    data = []
    for i in range(0, len(list[0])):
        more_ones = sum([1 for x in list if x[i] == '1']) >= sum([1 for x in list if x[i] == '0'])
        if more_ones:
            if truth:
                data.append(1)
            else:
                data.append(0)
        else:
            if truth:
                data.append(0)
            else:
                data.append(1)
    return data

def search_lists(input, truth):
    numbers = input.copy()
    for i in range(0, len(input[0])):
        count = 0
        for line in numbers:
            if line[i] == str(more_ones(numbers, truth)[i]):
                count += 1
        if count == len(numbers) / 2:
            char = (1 if truth else 0)
        else:
            char = more_ones(numbers, truth)[i]
        for line in list(numbers):
            if line[i] != str(char):
                numbers.remove(line)
        if len(numbers) == 1:
            return numbers[0]

print(int(search_lists(input, True), 2) * int(search_lists(input, False), 2))