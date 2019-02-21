import time;


#name = input("Give me your name please: ")
#age = input("Give me your age please: ")
name = "Damian"
age = 22
time_now = time.localtime(time.time())
message = f"Hy {name}, your are {age} now, and you'll turn 100 in {time_now[0] + 100 - int(age)}"
print(message)
multiply = int(input("How many times would you like to multiply this message?\n"))
print((message+"\n")*multiply)
