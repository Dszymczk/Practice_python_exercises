# Take the code from the How To Decode A Website exercise (if you didn’t do it or just
# want to play with some different code, use the code from the solution), and instead
# of printing the results to a screen, write the results to a txt file. In your code,
# just make up a name for the file you are saving to.
#
# Extras:
#
# Ask the user to specify the name of the output file that will be saved.\
import requests   # library that does HTML for humans
from bs4 import BeautifulSoup  # library that helps with parsing html

# Requesting for HTML code
url1 = "https://www.nytimes.com"
r = requests.get(url1)
r_html = r.text  # whole web page html code
# Working with HTML and putting webpage text to string wp_text
soup = BeautifulSoup(r.content, features="html.parser")
wp_text = ""
#
number = 0
for i in soup.find_all("h2"):
    number += 1
    wp_text += (str(number) + ") ")
    wp_text += i.text
    wp_text += "\n"
# transferring text to file
file_name = input(" What file name do you prefer?(without .txt) ") + ".txt"

with open(file_name, "w") as file:
    file.write(wp_text)
