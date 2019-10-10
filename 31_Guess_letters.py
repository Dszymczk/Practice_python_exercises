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
    word = "cokolwiek"
    guessed = []
    count = 0
    while not ended:
        guess = input("guess a letter")
        for i in guess:
            positions = check_word(i, word)
            count += 1
            for j in positions:
                guessed.append(j)
        if write_a_word(word, guessed) == word:
            ended = 1

