from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/newest")
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')


scores = []
score = soup.find_all(name="span", class_="score")

for tag in score:
    scores.append(tag.text)


# anchor_text = soup.select(selector='span', class_="titleline")
# for tag in anchor_text:
#     print(tag.find_all(name="a", limit=1))

def has_sub(css_class):
    return css_class is not None and "https" in css_class

news= [ ]
anchor = soup.find_all(href=has_sub, class_="")
for tag in anchor:
    news.append(tag.text)


print(news)
print(scores)

# print(anchor_text.get("text"))
# for tag in anchor_text:
#     print(tag.getText())





















'''
with open("Day41.html", encoding="utf8" ) as file:
    content = file.read()


soup = BeautifulSoup(content, "lxml")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

all_tag = soup.find_all(name="a")

# print(all_tag)

for tag in all_tag:
    # print(tag.getText())
    # print(tag.get('href'))
    pass

tag_With_class = soup.find(name="h2", id="hello")
# print(tag_With_class.text)

a_tag = soup.select_one(selector="ul a")
print(a_tag)
'''