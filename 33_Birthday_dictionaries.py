# This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.

# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find 
# that information based on their name. Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter a name, and return the birthday of
# that person back to them. The interaction should look something like this:

# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.

birthday_dict = {
	"Benjamon Franklin": "17/01/1706",
	"Mikolaj Kopernik": "19/02/1473",
	"Galileo Galilei": "15/02/1564",
	"Izaak Newton": "25/15/1642",
	"Adam Mickiewicz": "24/12/1798"
}

if __name__ == "__main__":
	print("Welcome to the birthday dictionary. We know the birthdays of:")
	for name in birthday_dict.keys():
		print(name)
	name = input("Who's birthday do you want to look up?")
	if name in birthday_dict.keys():
		print("We know his birthday date")
		date = birthday_dict.get(name, "No such Name")
		print("{}'s birthday is {}".format(name, date))
	else:
		print("Wrong name")
