from operator import index

import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text


soup = BeautifulSoup(yc_webpage, "html.parser")
article_tag = soup.find(name="a", class_="storylink")
print(article_tag)

article_text = article_tag.get_text()
print(article_text)

article_link = article_tag.get("href")
print(article_link)

article_upvote = soup.find(name="span", class_="score").getText()
print(article_upvote)

articles = soup.find_all(name="a", class_="storylink")
# print(articles)

article_texts = [item.getText() for item in articles]
print(len(article_texts))

article_links = [item.get("href") for item in articles]
print(article_links)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)

max_upvotes_index = article_upvotes.index(max(article_upvotes))
print(max_upvotes_index)

print(article_texts[max_upvotes_index])
print(article_links[max_upvotes_index])