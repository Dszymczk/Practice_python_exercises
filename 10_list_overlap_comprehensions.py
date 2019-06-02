#This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

#Take two lists, say for example these two:
#	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.


import random
# Lists without replacement
a = random.sample(range(0,10),10)
b = random.sample(range(0,11),11)
print(f"a: {a}\nb: {b}")

c = []
c = [x for x in a for y in b if x == y]
print(c)

# Lists with replacement
a = [random.randint(1,15) for element in range(10)]
b = [random.randint(1,15) for element in range(10)]
print(f"a: {a}\nb: {b}")
