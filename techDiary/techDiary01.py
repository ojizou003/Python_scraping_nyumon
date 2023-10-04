import requests
from bs4 import BeautifulSoup

url = "https://tech-diary.net/python-scraping-books/"
r = requests.get(url)

soup = BeautifulSoup(r.text)
title =soup.find("h1").text
print(title)


# 【厳選3冊】Webスクレイピング(Python)でおすすめの本【実務OK】