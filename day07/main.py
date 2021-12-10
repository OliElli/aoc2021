#!/usr/bin/env python3

from statistics import median
# pt1 lol
print(sum([abs(x - median([int(x) for x in [l for l in open("input.txt", "r")][0].split(',')])) for x in [int(x) for x in [l for l in open("input.txt", "r")][0].split(',')]]))