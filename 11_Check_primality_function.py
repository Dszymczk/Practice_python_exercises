# Program asks user for a number and determines whether the number is prime or not

# Function that checks if given number is prime: 1 - is prime, 0 - is not prime


def is_prime(num):
    for element in range(2, num - 1, 1):
        if num % element == 0:
            return 0
    return 1


num = int(input(" Give me some number please: "))
if is_prime(num):
    print(" Number is prime ")
else:
    print(" Number is not prime ")
