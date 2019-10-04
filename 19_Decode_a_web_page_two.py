from bs4 import BeautifulSoup
import requests


r = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
r_html = r.text
# print(r_html)
soup = BeautifulSoup(r_html, "html.parser")
# print(soup.prettify())
text = soup.find_all(class_="grid--item body body__container article__body grid-layout__content")
# print(text)
for element in text:
    print("ELEMENCIK")
    for desire_text in element.find_all('p'):
        print(desire_text.get_text(strip="True"))
