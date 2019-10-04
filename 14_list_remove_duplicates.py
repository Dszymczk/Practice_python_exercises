# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.


def remove_duplicates(a):
    b = []
    for x in a:
        if x in a and x not in b:
            b.append(x)
    return b


def remove_duplicates_set(a):
    return set(a)


a = [1, 4, 9, 16, 25, 9, 100, 64, 36, 49, 64, 81, 100]

c = remove_duplicates(a)
print("c: ", c)
print("d: ", remove_duplicates_set(a))

names = set()
names.add("Mikolaj")
names.add("Tomek")
names.add("Mikolaj")
print("SET: ", names)
names = list(names)
print("Lista: ", names)
names = set(names)
print("Znowu set: ", names)
