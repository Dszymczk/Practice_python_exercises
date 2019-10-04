# Program that asks player what square does he/she wants and draw a board with this choice.
# It remembers earlier choices
# Choices need do be written: (row, column)


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
    return board


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


if __name__ == "__main__":
    print(" Start")
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    draw_a_board(board)
    ended = 0
    print(' "O" Starts: ')
    player = 1
    choice = input(" What square do you choose? row,column ")
    board = get_choice(choice,board,1)
    draw_a_board(board)
    while not ended:
        print('Now "X"')
        player = 2
        choice = input(" What square do you choose? row,column ")
        oard = get_choice(choice, board, player)
        draw_a_board(board)
        ended = check_board(board)
        if ended:
            print(" X has won")
            break
        print('Now "O"')
        player = 1
        choice = input(" What square do you choose? row,column ")
        board = get_choice(choice, board, player)
        draw_a_board(board)
        ended = check_board(board)
        if ended:
            print(" O has won")
            break
