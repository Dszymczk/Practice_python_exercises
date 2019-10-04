# Program checks who has won i Tic tac toe game
# Matrix represents board:
# [[0,1,2],
#  [2,1,0],
#  [2,1,1]]
# 0 represents empty square, 1 firs player choice, 2 second player choice
#
# Damian


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
    board = [[1, 0, 2],
             [1, 2, 1],
             [2, 2, 2]]
    print(check_board(board))
