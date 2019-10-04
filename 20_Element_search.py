# Write a function that takes an ordered list of numbers (a list where the elements are in order
# from smallest to largest) and another number. The function decides whether or not the given number
# is inside the list and returns (then prints) an appropriate boolean.
#
# Extras:
#
# Use binary search.
import random


# Give an information if a number is in a number_list. Print out information. Uses standard search
#
# number - number to check if is in a list
# number_list - list of numbers ordered from smallest to largest
def standard_search(number, number_list):
    if number in number_list:
        print("Number: ",number, " is in a list")
    else:
        print("Number: ",number, " is not in a list")


# Give an information if a number is in a number_list. Print out an information. Uses binary search
#
# number - number to check if is in a list
# number_list - list of numbers ordered from smallest to largest
def binary_search(number, number_list):
    is_in_a_list = 0    # boolean parameter informing if number is in a list
    while len(number_list) > 1:
        if number_list[round(len(number_list)/2)-1] == number:
            is_in_a_list = 1
            break
        elif number_list[round(len(number_list)/2)] > number:
            number_list = number_list[0:round(len(number_list)/2)-1]
            # print(number_list)
        elif number_list[round(len(number_list)/2)] < number:
            number_list = number_list[round(len(number_list)/2):len(number_list)]
            # print(number_list)
    if is_in_a_list:
        print("Number: ", number, "is in a list")
    else:
        print("Number: ", number, "is not in a list")


if __name__ == "__main__":
    # Generating ordered list
    number_list = random.sample(range(100), 20)
    number_list.sort()

    print("\n Standard Search ")
    print(number_list)
    standard_search(12, number_list)
    binary_search(12, number_list)
