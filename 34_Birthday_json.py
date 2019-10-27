# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this 
# exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file 
# on disk, rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary,
# and update the JSON file you have on disk with the scientist’s name. If you run the
# program multiple times and keep adding new names, your JSON file should keep getting
# bigger and bigger.
import json

# Loads birthdays and names from file and return dictionary
def load_json(file_name):
	with open(file_name,"r") as file:
		bd = json.load(file)
		return bd

# Saves birtday dictionary to file 
def save_json(file_name, bd_dict):
	with open(file_name, "w") as file:
		json.dump(bd_dict, file)
		print('File "{}" saved'.format(file_name))


# Adds new record do json file
def add_date(bd_dict, date, full_name):
	bd_dict[full_name] = date
	print(bd_dict)

if __name__ == "__main__":
	file_name = "birthdays.json"
	# birthday_dict = {
	# "Benjamin Franklin": "17/01/1706",
	# "Mikolaj Kopernik": "19/02/1473",
	# "Galileo Galilei": "15/02/1564",
	# "Izaak Newton": "25/15/1642",
	# "Adam Mickiewicz": "24/12/1798"
	# }
	birthday_dict = load_json(file_name)
	add_date(birthday_dict, "24/02/1995", "Steve Jobs") 
	save_json(file_name, birthday_dict)


