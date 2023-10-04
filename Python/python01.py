import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
r = requests.get(url) # rはresponseの略

# print(r.url) # アクセスしたurlを確認

# print(r.status_code) # ステータスコードを確認 200->アクセス成功

# print(type(r.text)) # 取得したテキストの型を確認

soup = BeautifulSoup(r.text,features="lxml") # 単なる文字列から、解析可能なデータに変換

# soup.find('h2') # soupから最初のh2タグを取得する
# soup.find('h2').text # そのテキストを取得する


h2li = soup.find_all('h2')# soup.find_all('h2') #soupからすべてのh2タグを取得する
# for i,h2 in enumerate(h2li): #そのテキストを取得する
#   print(i,h2.text) 

# h2のテキストをリスト化するとき
# h2t_li = []
# for h2 in h2li:
#   h2t_li.append(h2.text)

# リスト内包表記
h2t_li = [h2.text for h2 in h2li]

print(h2t_li)

