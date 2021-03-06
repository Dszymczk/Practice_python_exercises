# Full tic tac toe game


# Draws a board
#
# board - Two dimensional list containing player choices
def draw_a_board(board):
    row = 3
    column = 3
    # choices = []  # list containing coordinates of firs player choices
    # x_choices = []  # list containing coordinates of second player choices
    line = "   "
    for i in range(column):
        line += " "
        line += str(i + 1)
        line += "  "
    print(line)
    print(" ", " ---" * column)
    for i in range(row):
        line = ""
        line += str(i+1)
        line += " "
        for j in range(column):
            line += "|"
            if board[i][j] == 1:
                line += " O "
            elif board[i][j] == 2:
                line += " X "
            else:
                line += "   "
        line += "|"
        print(line)
        print(" ", " ---" * column)
    #print("====" * column)


# Function that asks user of his move and controls user choice. It checks if chosen square is empty.
# It gives appropriate message
# It returns new board
#
# choice - player choice (row, column) - string
# board - previous board
# player - informs whose turn it is
def get_choice(choice, board, player):
    # converting string into apriopriate format
    choice = choice.split(",")
    choice = [int(i.strip()) for
              i in choice]
    # print(choice)
    # changing board

    if board[choice[0] - 1][choice[1] - 1] == 0:
        board[choice[0] - 1][choice[1] - 1] = player
    else:
        return 0
    return 1


# function to check the board
#
# board - 3x3 list
def check_board(board):
    for player in [1, 2]:
        for i in range(3):
            condition3 = board[0][0] == board[1][1] == board[2][2] == player
            if board[i][0] == board[i][1] == board[i][2] == player or board[0][i] == board[1][i] == board[2][i] == player  or condition3:
                return player
    return 0


# Checks if there are any moves left (if board is full). If board is full return 0, if there are moves do do, return 1
def is_move(board):
    is_0 = False
    for row in board:
        is_0 = is_0 or 0 in row
    return is_0


if __name__ == "__main__":
    print(" Start")
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    draw = 0
    draw_a_board(board)
    ended = 0
    print(' "O" Starts: ')
    player = 1
    choice = input(" What square do you choose? row,column ")
    get_choice(choice, board, 1)
    draw_a_board(board)

    while not ended and not draw:
        if player == 1:
            print('Now "X"')
            player = 2
        elif player == 2:
            print('Now "O"')
            player = 1
        choice = input(" What square do you choose? row,column ")
        while not get_choice(choice, board, player):
            print(" Wrong choice")
            choice = input(" What square do you choose? row,column ")
        draw_a_board(board)
        ended = check_board(board)
        draw = not is_move(board)
    if draw == 1:
        print("It is a draw!")
    elif player == 1:
        print("O has won!")
    elif player == 2:
        print("X has won!")
