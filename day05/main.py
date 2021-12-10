#!/usr/bin/env python3

file = 'input.txt'
with open(file) as f:
    input = f.read().splitlines()

# Build output grid
grid = []
for x in range(0, 999):
    grid.append([])
    for y in range(0, 999):
        grid[x].append(0)

def positive_range(x, y):
    x = int(x)
    y = int(y)
    if y > x:
        return(range(x, y+1))
    else:
        return(range(y, x+1))

for line in input:
    start, end = line.split(' -> ')
    start_x, start_y = start.split(',')
    end_x, end_y = end.split(',')

    if (start_x == end_x or start_y == end_y):
        for x in positive_range(start_x, end_x):
            for y in positive_range(start_y, end_y):
                grid[y][x] += 1

count = 0
for i in grid:
    for j in i:
        if j > 1:
            count += 1

print(count)