# recap game
# new game
# set up player
# 9 turns or interrupted if row of X or O
#  1- player n, provide coordinate
#  2- test winner
#       if yes ~ give points
#       if no - again

import random


def initGame(p1name, p1tks, p2name):
    '''
    Initialise the game with two player
    :param p1name: str
    :param p1tks: str X or O
    :param p2name: str
    :return: dictionarie
    '''
    testvar = False
    while not testvar:
        if not p1name:
            p1name = str(input("Again P1 Name: "))
        elif not p1tks or p1tks.upper() not in ["X", "O"]:
            p1tks = str(input("Again P1 Tks X ou O: "))
        elif not p2name:
            p2name = str(input("Again P2 Name: "))
        else:
            testvar = True
            break

    if p1tks.upper() == "X":
        p1_active = True
        p2tks = "O"
        p2_active = False
    else:
        p1_active = False
        p2tks = "X"
        p2_active = True

    setgame = {"p1": {"name": p1name, "tks": p1tks, "active": p1_active},
               "p2": {"name": p2name, "tks": p2tks, "active": p2_active}}

    return setgame


# set the board
def set_board():
    '''
    Set the board game
    :return: Matrix
    '''
    return [["#", "A", "B", "C"],
            ["1", "_", "_", "_"],
            ["2", "_", "_", "_"],
            ["3", "_", "_", "_"]]


# print de board
def print_board(board):
    '''
    Print the board
    :param board: Matrix with even 4*3
    :return: print board
    '''
    for row in range(len(board)):
        for cell in range(len(board[row])):
            print(board[row][cell], end=" ")
        print()


def check_coord(coord, board):
    testvar = False
    while not testvar:
        print(len(coord))
        if not len(coord) == 2:
            coord = input("Error: expected only two .. ")
        elif not isinstance(coord[0], str) or coord[0].upper() not in ["A", "B", "C"]:
            coord = input("Error, expected on letter and a number. ex: 'B2' ")
        elif coord[1] not in ["1", "2", "3"]:
            coord = input("Error, expected on letter and a number. ex: 'B2' ")
        else:
            col_coord = {"A": 1, "B": 2, "C": 3}
            col = col_coord[coord[0].upper()]
            row = int(coord[1])
            current_coord = board[row][col]
            if current_coord != "_":
                coord = input("Error, coordinate already taken : ")
            else:
                testvar = True

    return coord.upper()


def new_coord(coord, tks, board):
    '''
    Change coord in board
    :param coord: str
    :param tks: str
    :param board: list
    :return: list
    '''

    col_coord = {"A": 1, "B": 2, "C": 3}
    col = col_coord[coord[0]]
    row = int(coord[1])
    current_coord = board[row][col]
    board[row][col] = tks
    return board


def listen_xo(board):
    list_board = []
    # row
    list_board.append([board[1][1], board[1][2], board[1][3]])
    list_board.append([board[2][1], board[2][2], board[2][3]])
    list_board.append([board[3][1], board[3][2], board[3][3]])
    # col
    list_board.append([board[1][1], board[2][1], board[3][1]])
    list_board.append([board[1][2], board[2][2], board[3][2]])
    list_board.append([board[1][3], board[2][3], board[3][3]])

    # list of diag
    list_board.append([board[1][1], board[2][2], board[3][3]])
    list_board.append([board[1][3], board[2][2], board[3][1]])
    return list_board


# set the board and print it
board = set_board()
print_board(board)
print("\n")

# input Names player + player 1
print("if you want to play against the computer write 'computer' for one player")
print("\n")
p1name = input("P1 Name: ")
p1tks = input("P1 Tks: ").upper()
p2name = input("P2 Name: ")

new_game = initGame(p1name, p1tks, p2name)

# print(new_game['p1'])
winner = False
i = 0
while winner is False:
    # print(f" winner is {winner}")
    # print(i)
    i += 1
    print(f"Turn: {i}")
    # print("\n")
    if new_game['p1']['active']:
        name = new_game['p1']['name']
        tks = new_game['p1']['tks']
    else:
        name = new_game['p2']['name']
        tks = new_game['p2']['tks']

    #   if playing against computer
    if name == "computer":
        is_coord_computer = False
        while not is_coord_computer:
            col = random.choice(['A', 'B', 'C'])
            row = random.choice(['1', '2', '3'])

            col_coord = {"A": 1, "B": 2, "C": 3}
            col_check = col_coord[col]
            row_check = int(row)
            current_coord = board[row_check][col_check]
            if current_coord == "_":
                is_coord_computer = True

        coord = str(col + row)

    else:
        coord = str(input(f"Ok {name}, play you'r {tks} in the right coord: "))
        coord = check_coord(coord, board)

    # set new coord with tks (X OR O) in the board
    board = new_coord(coord, tks, board)
    print_board(board)
    # list of column
    list_board = listen_xo(board)
    # print(list_board)
    for row in list_board:
        set_row = set(row)
        # print(f"row  {row} adn the set {set_row}")
        # print(len(set_row))
        if len(set_row) == 1:
            for letter in set_row:
                if letter in ["X", "O"]:
                    # print("winner")
                    is_game = "winner"
                    # print('because of count')
                    winner = True
                    break
    if i == 9:
        print("Draw")
        is_game = "draw"
        winner = True
        break

    print(f"You just played {name}")
    print("\n")
    #     change switch active to another
    if new_game['p1']['active']:
        # then P2 now needs to be active
        new_game['p1']['active'] = False
        new_game['p2']['active'] = True
    else:
        new_game['p1']['active'] = True
        new_game['p2']['active'] = False

else:
    if is_game == "winner":
        print(f"Well done {name}, you won!")
    else:
        print("Draw !!")
