#!/usr/bin/env python3

file = 'test_input.txt'
bits = {}
gamma = []
epsilon = []
gamma_value = 0
epsilon_value = 0
updated_input = []

with open(file) as f:
    input = f.read().splitlines()

for i in range(0, len(input[0])):
    bits[i] = 0

for line in input:
    for i in range(0, len(input[0])):
        if line[i] == '1':
            bits[i] += 1

for i in range(0, len(input[0])):
    if bits[i] / len(input) > 0.5:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

print(input)
print(gamma)

input_line = -1
for line in input:
    input_line += 1
    for i in range(0, len(input[0])):
        print(line[i])
        if line[i] == gamma[i]:
            # not significant
            input.pop(input_line)
            continue
    break

print(input)




# for i in range(0, len(input[0])):
#     if gamma[i] == 1:
#         gamma_value += 2 ** i
#     if epsilon[i] == 1:
#         epsilon_value += 2 ** i

# print(gamma_value * epsilon_value)