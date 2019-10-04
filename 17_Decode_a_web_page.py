# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
import requests   # library that does HTML for humans
from bs4 import BeautifulSoup  # library that helps with parsing html
url1 = "https://www.nytimes.com"
r = requests.get(url1)
r_html = r.text  # whole web page html code
#print(r_html)
soup = BeautifulSoup(r.content, features="html.parser")
# title = soup.find('span', 'articletitle').string
print("ugabuga")
for i in soup.find_all("h2"):
    print(type(i.text))


