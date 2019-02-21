#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out
import random

# compare two numbers. If num is greater than gal, function gives back 1. If goal is greater, gives -1. If equal gives 0
def compare_num(num, goal):
    if num == goal:
        return 0
    if num >= goal:
        return 1
    if num <= goal:
        return -1


# boolean variable which tells if player still want to play
play = True
while play and guess != "exit":
    goal = random.randint(1,10)
    guess = 0
    guess_number = 0
    while guess != goal:
        guess_number += 1
        guess = int(input("Guess the number: "))
        is_correct = compare_num(guess,goal)
        if is_correct == 1:
            print("Your guess is to high")
        elif is_correct == -1:
            print("Your guess is to low")
        elif is_correct == 0:
            print(f"You are right! Congratulations,\nNumber of guesses: {guess_number}")

    play_str = input("Do you still wanna play? (yes/no)")
    if play_str.lower() == "no":
        play = 0