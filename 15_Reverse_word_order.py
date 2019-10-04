# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.


word = "This is a long sentence and I want to read it backwards"
word = word.split(" ")
word = word[::-1]
word = " ".join(word)


print(word)
