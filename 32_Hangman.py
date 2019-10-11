# Hangman game
import random


# Picks word from file. Return this word(string)
#
# file_name - name of the file (with ".txt" ending)
def pick_word(file_name):
    list_of_words = []  # list containing all wards from file
    with open(file_name, 'r') as file:
        list_of_words = file.readlines()
        # line = file.readline()
        # while line:
        #     list_of_words.append(file.readline().strip())
        #     line = file.readline()
        # print(list_of_words)
        # print(len(list_of_words))
        word = random.choice(list_of_words)
    return word


# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to
# guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the
# actual game, the player can only guess 6 letters incorrectly before losing).


# Function that checks if in a given word is given letter.
# Returns list of positions where are those letters
#
# letter -
# word -
def check_word(letter, word):
    positions = []
    for i in range(len(word)):
        if word[i] == letter:
            positions.append(i)
    return positions


# Prints a word. If index is in guessed prints letter. If a letter is not in guessed prints " _ "
def write_a_word(word, guessed):
    to_write = ""
    for i in range(len(word)):
        if i in guessed:
            to_write += word[i]
        else:
            to_write += " _ "
    print(to_write)
    return to_write


if __name__ == "__main__":
    ended = 0
    word = pick_word("30_List_of_words.txt").upper()
    guessed = []
    count = 0
    wrongs = 0
    used = {}
    while wrongs < 8:
        print("You have ", 8 - wrongs, "chances")
        guess = input("guess a letter").upper()
        for i in guess:
            if i in guessed:
                print("This same letter again")
            elif i in word:
                positions = check_word(i, word)
                print(i)
                count += 1
                for j in positions:
                    guessed.append(j)
                used.add(i)
                print(used)
            else:
                wrongs += 1
        if write_a_word(word, guessed) == word:
            ended = 1
    print(word)


