import random


# Function that checks if hess is the same as number. If number is ok, then it returns [1, 0, 0]. If not, function
# returns number of cows(x) and bulls(y): [0, x, y]
# Parameters:
# number - desired number
# guess - number guessed by user
def number_check(number, guess):
    if number == guess:
        return[True, 0, 0]
    else:
        return how_many_cows_and_bulls(number, guess)


def how_many_cows_and_bulls(number, guess):
    cows = 0
    bulls = 0
    s_number = str(number)
    s_guess = str(guess)
    checked = []
    for i in range(len(s_number)):
        if s_number[i] == s_guess[i]:
            cows += 1
            checked.append(i)
    for i in range(len(s_number)):
        if i not in checked:
            for j in range(len(s_guess)):
                if j not in checked:
                    if s_number[i] == s_guess[j]:
                        bulls += 1
                        checked.append(j)
                        break
    return [False, cows, bulls]


if __name__ == "__main__":
    cows = 0
    bulls = 0
    guesses = 0
    number = random.randrange(1000, 10000)  # random 4-digit number to be guessed
    guess = int(input("Give me 4-digit number: "))
    # print(number_check(guess, number))
    score = number_check(number, guess)
    while not score[0]:
        guesses += 1
        print("You have ", score[1], " cows and ", score[2], "bulls", "try again")
        guess = int(input(" Try with another number"))
        score = number_check(number, guess)
    print("Well done, you guessed the number. Number of tries: ", guesses)
