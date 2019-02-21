# Program that asks user for a number and then prints out all the divisors of that number
num = int(input("Give me number please: "))
a = range(1, num)
divisors = []


for i in a:
    if num % int(i) == 0:
        divisors.append(i)
print(f" Those are all of the divisors of {num}: {divisors}")
