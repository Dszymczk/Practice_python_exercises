from collections import Counter
bd = __import__('34_Birthday_json')


# Counts how many months are in birthday dictionary and print them out with number
def count_months(bd_dict):
	months = []
	for value in bd_dict.values():
	    months.append(num_to_month(value.split('/')[1]))
	print(Counter(months))


# convert number to string(month)     
def num_to_month(num):
	num_dict={
	'01':'January',
	'02':'February',
	'03':'March',
	'04':'April',
	'05':'May',
	'06':'June',
	'07':'July',
	'08':'August',
	'09':'September',
	'10':"Oktober",
	'11':'November',
	'12':'December',
	}
	return num_dict[num]


if __name__ == "__main__":
	file_name = "birthdays.json"
	bd_dict = bd.load_json(file_name)
	print(bd_dict.values())
	months = count_months(bd_dict)
	
