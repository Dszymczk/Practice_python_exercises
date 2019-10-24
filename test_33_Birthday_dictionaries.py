# 33_Birthday_dictionaries tests
bd = __import__('33_Birthday_dictionaries')

birthday_dict = {
	"Benjamin Franklin": "17/01/1706",
	"Mikolaj Kopernik": "19/02/1473",
	"Galileo Galilei": "15/02/1564",
	"Izaak Newton": "25/15/1642",
	"Adam Mickiewicz": "24/12/1798"
}

def test_find_date1():
	assert bd.find_date("Benjamin Franklin", birthday_dict) == "17/01/1706"


def test_find_date2():
	assert bd.find_date("Galileo Galilei", birthday_dict) == "15/02/1564"


def test_find_date3():
	assert bd.find_date("Adam Mickiewicz", birthday_dict) == "24/12/1798"		
