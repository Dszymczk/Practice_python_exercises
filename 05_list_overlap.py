# Program that returns list that contains only the elements that are common between both lists(without duplicates)
import random


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result_list = []

# random list generation(with duplicates)
a = sorted([random.choice(range(10)) for i in range(10)])
b = sorted([random.choice(range(10)) for i in range(12)])

for element in a:
    if element not in result_list:
        if element in b:
            result_list.append(element)
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {result_list}")
