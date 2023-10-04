import requests
from bs4 import BeautifulSoup

url = 'https://tech-diary.net/python-scraping-books/'

r = requests.get(url)
soup = BeautifulSoup(r.text,features='lxml')

# h2h3 = soup.find_all(['h2','h3'])

# h2h3tli = [tag.text for tag in h2h3]
# print(h2h3tli)

# 記事の本文を指定して見出しタグを取得
h2h3 = soup.find('div',class_='post_content').find_all(['h2','h3'])
h2h3li = [tag.text for tag in h2h3]
print(h2h3li)