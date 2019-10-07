# In this exercise, the task is to write a function that
# picks a random word from a list of words from the SOWPODS dictionary
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


if __name__ == "__main__":
    file_name = "30_List_of_words.txt"
    print(pick_word(file_name))

