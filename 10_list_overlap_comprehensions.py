import random
# Lists with replacement
a = random.sample(range(0,10),10)
b = random.sample(range(0,11),11)
print(f"a: {a}\nb: {b}")

c = []
c = [x for x in a for y in b if x == y]
print(c)

# Lists without replacement
a = [random.randint(1,15) for element in range(10)]
b = [random.randint(1,15) for element in range(10)]
print(f"a: {a}\nb: {b}")
