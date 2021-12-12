#!/usr/bin/env python3

# pt1
inputs = [l.split('|')[0].strip() for l in open("input.txt", "r")]
outputs = [l.split('|')[1].strip() for l in open("input.txt", "r")]

input_words = [l.split(' ') for l in inputs]
output_words = [l.split(' ') for l in outputs]
output_count = [l for l in output_words]

signal = [l for l in range(0, len(input_words))]

# Find 1, 4, 7, 8
for i in range(0, len(input_words)):
    signal[i] = [l for l in range(0, 10)]
    for j in input_words[i]:
        j = ''.join(sorted(j))
        if len(j) == 2:
            signal[i][1] = j
        elif len(j) == 3:
            signal[i][7] = j
        elif len(j) == 4:
            signal[i][4] = j
        elif len(j) == 7:
            signal[i][8] = j
# Find 0 ,6, 9
for i in range(0, len(input_words)):
    for j in input_words[i]:
        j = ''.join(sorted(j))
        if len(j) == 6:
            if len(set(signal[i][4]).intersection(j)) == 4:
                signal[i][9] = j
            # if both 1 chars in, its 0, else its 6
            elif len(set(signal[i][1]).intersection(j)) == 2:
                signal[i][0] = j
            else:
                signal[i][6] = j
# Find 2, 3, 5
for i in range(0, len(input_words)):
    for j in input_words[i]:
        j = ''.join(sorted(j))
        if len(j) == 5:
            if len(set(signal[i][1]).intersection(j)) == 2:
                signal[i][3] = j
            elif len(set(signal[i][6]).intersection(j)) == 5:
                signal[i][5] = j
            else:
                signal[i][2] = j

# pt2
pt2 = 0
for i in range(0, len(output_words)):
    output = []
    for j in output_words[i]:
        j = ''.join(sorted(j))
        output.append(str(signal[i].index(j)))
    pt2 += int(''.join(output))
print(pt2)

'''
Notes:

 aaaa             aaaa    aaaa            aaaa    aaaa    aaaa    aaaa    aaaa
b    c        c       c       c  b    c  b       b            c  b    c  b    c
b    c        c       c       c  b    c  b       b            c  b    c  b    c
                  dddd    dddd    dddd    dddd    dddd            dddd    dddd    
e    f        f  e            f       f       e  e    f       f  e    f       f
e    f        f  e            f       f       e  e    f       f  e    f       f
 gggg             gggg    gggg            gggg    gggg            gggg    gggg

a = 0   2 3   5 6 7 8 9
b = 0       4 5 6   8 9
c = 0 1 2 3 4     7 8 9
d =     2 3 4 5 6   8 9
e = 0   2     5 6   8
f = 0 1   3 4   6 7 8 9
g = 0   2 3   5 6   8 9

0 = a b c   e f g       6
1 =     c     f         2
2 = a   c d e   g       5
3 = a   c d   f g       5
4 =   b c d   f         4
5 = a b   d e   g       5
6 = a b   d e f g       6
7 = a   c     f         3
8 = a b c d e f g       7
9 = a b c d   f g       6

2 has 1
3 has 7
4 has 4
5 has 2 3 5
6 has 0 6 9
7 has 8
'''
