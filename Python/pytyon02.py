import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
r = requests.get(url)
soup = BeautifulSoup(r.text,features="lxml")

# spanタグの数を確認する
# print(len(soup.find_all("span")))

# すべてのspanタグを確認
# print(soup.find_all("span"))

# say-no-moreクラスを持つspanタグをすべて取得する
# print(soup.find_all('span', class_='say-no-more'))

# say-no-moreクラスとmessageクラスを持つspanタグをすべて取得する
print(soup.find_all('span',class_=['say-no-more','message']))