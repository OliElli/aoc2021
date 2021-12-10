#!/usr/bin/env python3

from statistics import median, mean

# pt1
input = [int(x) for x in [l for l in open("input.txt", "r")][0].split(',')]
print(round(sum([abs(x - median(input)) for x in input])))

# pt2
print(round(sum([f * (f + 1) / 2 for f in [abs(x - round(mean(input) - 1)) for x in input]])))
