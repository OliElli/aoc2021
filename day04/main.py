#!/usr/bin/env python3

file = 'input.txt'
with open(file) as f:
    input = f.read().splitlines()

pulled_nums = input[0].split(',')
for i in range(0, 2):
    input.remove(input[0])

boards = {}
board_num = 0
for i in input:
    boards[board_num] = []
    if i == '':
        board_num += 1
board_num = 0
for i in input:
    if i == '':
        board_num += 1
    else:
        boards[board_num].append(i.split())

rows = {}
columns = {}

# Build boards for rows and columns
for board in range(0, len(boards)):
    rows[board] = []
    columns[board] = []
    
    for row in range (0, len(boards[0][0])):
        columns[board].append([])
        rows[board].append(boards[board][row])
    
    for column in range(0, len(boards[0][0])):
        for row in range(0, len(boards[0][0])):
            columns[board][column].append(rows[board][row][column])

def find_number(number, data):
    board_num = 0
    for board in data:
        for i in data[board]:
            if number in i:
                i.remove(number)
                if len(i) == 0:
                    return data[board], board_num
        board_num += 1

def find_score(board, winning_num):
    total = 0
    for i in board:
        for j in i:
            total += int(j)
    return(total * int(winning_num))

# pt1
for number in pulled_nums:
    winning_board = find_number(number, rows)
    if winning_board:
        print(winning_board[0])
        print(find_score(winning_board[0], number))
        break
    winning_board = find_number(number, columns)
    if winning_board:
        print(winning_board[0])
        print(find_score(winning_board[0], number))
        break

def winning_board(number, data):
    winning_board = find_number(number, data)
    return winning_board[0]

# pt2
for number in pulled_nums:
    while len(rows) > 1:
        


    winning_board = find_number(number, rows)
    if winning_board:
        # Remove board 
        print(winning_board[1])
        rows.pop(winning_board[1])


print(len(rows))
rows.pop(1)
print(len(rows))