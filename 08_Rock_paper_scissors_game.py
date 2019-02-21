# Rock paper scissors game
# Function that checks who has won, depending on choices; output vvalues: 1 - first player has won 0 - draw (-1) - second player has won
def fight(pl1, pl2):
    pl1.lower()
    pl2.lower()
    if pl1 == "scissors":
        if pl2 == "rock":
            return -1
        elif pl2 == "paper":
            return 1
    elif pl1 == "paper":
        if pl2 == "scissors":
            return -1
        elif pl2 == "rock":
            return 1
    elif pl1 == "rock":
        if pl2 == "paper":
            return -1
        elif pl2 == "scissors":
            return 1
    return 0

# Takes an answer from player; checks if it is correct
def get_choice(name):
    choice = input(f"Hy {name}, give me your choice")
    choice.lower()
    while choice != "rock" and choice != "paper" and choice != "scissors":
        choice = input(f"Wrong choice {name}! Try again: ")
        choice.lower()
    return choice

# main game - function; no input/output values
def game():
    # number of player1 points(max 3)
    pl1_score = 0
    # number of player2 points(max 3)
    pl2_score = 0
    while pl1_score != 3 and pl2_score != 3:
        print("\nNew round")
        pl1_choice = get_choice("Player 1")
        pl2_choice = get_choice("Player 2")
        pl1_win = fight(pl1_choice, pl2_choice)
        if pl1_win == 1:
            print("Player1 has won this round")
            pl1_score += 1
        elif pl1_win == 0:
            print("No score")
        elif pl1_win == -1:
            print("Player2 has won this round")
            pl2_score += 1
        print(f"Player1 score:{pl1_score}\nPlayer2 score: {pl2_score} ")
    print("end game")
    if pl1_score == 3:
        print("Player1 has won the game")
    elif pl2_score == 3:
        print("Player2 has won the game")

# boolean value that checks if player still want to play
play = 1
while play == 1:
    game()
    decision = input("Do you still wanna play? :")
    if decision.lower() == "no":
        print("Thank you for the play")
        play = 0