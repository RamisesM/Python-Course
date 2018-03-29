# -*- coding: utf-8 -*-

def print_board(matrix):
    symbols = {0:" ", 1:"O", 4:"X"}
    for line in matrix:
        print("|", end="", flush=True)
        for value in line:
            print("{}|".format(symbols[value]), end="", flush=True),
        print("")

def check_victory(player_number, matrix):
    victory = False
    victory_sum = 3*player_number**2
    for index in range(0,3):
        # Checking lines
        victory = victory or (sum(matrix[index]) == victory_sum)
        # Checking columns
        victory = victory or (sum(list(map(list, zip(*matrix)))[index]) == victory_sum)
    # Checking diagonals
    victory = victory or (matrix[0][0]+matrix[1][1]+matrix[2][2] == victory_sum)
    victory = victory or (matrix[0][2]+matrix[1][1]+matrix[2][0] == victory_sum)
    return victory

def get_input(player_number) :
    print ("Player {} move".format(player_names[player_number]))
    Line = int(input ("Line (0 to 2): "))
    while Line < 0 or Line > 2:
        Line = int(input ("Invalid Line, type again (0 to 2):"))
    Column = int(input ("Column (0 to 2): "))
    while Column < 0 or Column > 2:
        Column = int(input ("Invalid Column, type again (0 to 2):"))
    return (Line, Column)

def register_play(player_number, matrix):
    (Line, Column) = get_input(player_number)
    while (matrix[Line][Column] != 0):
        print ("Invalid play! Already picked, please play again")
        (Line, Column) = get_input(player_number)
    matrix[Line][Column] = player_number**2
    return matrix

matrix = [[0,0,0],[0,0,0],[0,0,0]]
player_names = {1:"one", 2:"two"}
player_number = 1
running = True

while(running):
    print_board(matrix)
    matrix = register_play(player_number, matrix)
    if check_victory(player_number, matrix):
        break
    if player_number == 1:
        player_number = 2
    else:
        player_number = 1
    
print_board(matrix)
print ("Player {} won! Congratulations!!!".format(player_names[player_number]))