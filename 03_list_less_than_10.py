my_list = [5, 2, 7, 3, 7, 3, 7, 4, 7, 9, 5]
# for element in my_list:
#     if element > 5:
#         print(element)

# new list instead of printing elements one by one
new_list = []
for element in my_list:
    if element >= 5:
        new_list.append(element)

# prints out new list
for element in new_list:
    print(element)

# list element greater than number given by user
check = int(input("give me number"))
new_list = []
for element in my_list:
    if element >= check:
        new_list.append(element)

# prints out new list
for element in new_list:
    print(element)


# First task done in one line
print([element for element in my_list if element < 5])  # Why [] in print

