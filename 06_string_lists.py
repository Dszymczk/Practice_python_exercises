# Program that checks whether a word given by user is palindrome
def is_palindrome(word):
    return word == word[::-1]


word = "kajak"  # input("Give me some word please: ")
reversed_word = []
for index in range(len(word) - 1, -1, -1):
    reversed_word.append(word[index])
palindrome = True
for i in range(len(word)):
    if word[i] != reversed_word[i]:
        palindrome = False
if palindrome:
    print("Word is palindrome")


# string based program <- much faster way
print("\n\nstring based program")
reversed_word = word[::-1]
print(reversed_word)
if reversed_word == word:
    print("Word is palindrome")

# Shorter code
if word == word[::-1]:
    print("\n\nWord is palindrome")

# Using function
if is_palindrome(word):
    print("\n\n(3) Word is palindrome")
