# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has
# a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.


if __name__ == "__main__":
    with open("23_Happy_numbers.txt", "r") as file:
        happy_numbers = file.read().split("\n")
    with open("23_Prime_numbers.txt", "r") as file:
        prime_numbers = file.read().split("\n")
    overlaps = []
    for elem in happy_numbers:
        if elem in prime_numbers:
            overlaps.append(elem)
    print(overlaps)
    print(len(overlaps))
