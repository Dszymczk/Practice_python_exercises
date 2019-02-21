# number = int(input("give me number and I'll tell you if it is odd or even: "))
# if number % 2 == 0:
#     print("Number is even")
#     if number % 4 == 0:
#         print("and divided by 4")
# else:
#     print("Number is odd")
num = int(input("Give me number: "))
check = int(input("Give me number to divide by: "))
if num % check == 0:
    print(f"{num} is divided by {check} and it equals {num / check}")
else:
    print(f"{num} is not divided by {check}")
