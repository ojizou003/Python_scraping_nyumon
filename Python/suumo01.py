from bs4 import BeautifulSoup
import requests
from pprint import pprint
from time import sleep
import pandas as pd
import re

url = 'https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}'

dlist = []

# 1～3page、ループする
for i in range(1,4):
  target_url = url.format(i)
  r = requests.get(target_url)
  sleep(1)
  soup = BeautifulSoup(r.text,features='lxml')
  contents =soup.find_all('div',class_='cassetteitem')
  for content in contents:
    # 物件名
    title = content.find('div',class_='cassetteitem_content-title').text
    # 物件情報
    detail = content.find('ul', class_='cassetteitem_detail')
    # 部屋情報
    other = content.find('table', class_='cassetteitem_other')
    # 住所
    address = detail.find('li', class_="cassetteitem_detail-col1").text
    # アクセス
    access= detail.find('li', class_="cassetteitem_detail-col2").text
    # 築年数
    age = detail.find('li', class_="cassetteitem_detail-col3").text
    # すべてのtrを取得
    rows = other.find_all('tr', class_='js-cassette_link')
    # 部屋情報
    # room_info = []
    for row in rows:
      # その中からすべてのtdを取得(9)
      tds = row.find_all('td')
      # 階数[2]
      floor = tds[2].text
      # 賃料/管理費[3]
      rent = tds[3]
      fee,manage = rent.find_all('li')
      # 敷金・礼金[4]
      firstmoney = tds[4]
      deposit,thank = firstmoney.find_all('li')
      # 間取り・面積[5]
      area =tds[5]
      madori,menseki = area.find_all('li')
      d = {
        'a_物件名':title,
        'b_住所':address,
        'c_アクセス':access,
        'd_築年数':age,
        'e_部屋の階数':floor,
        'f_賃料':fee.text,
        'g_管理費':manage.text,
        'h_敷金':deposit.text,
        'i_礼金':thank.text,
        'j_間取り':madori.text,
        'k_専有面積':menseki.text
      }
      dlist.append(d)

df = pd.DataFrame(dlist)
df2 = df.applymap(lambda x: re.sub('\n', ' ', x))
df3 = df2.applymap(lambda x: re.sub('\r', ' ', x))
cdf = df3.applymap(lambda x: re.sub('\t', ' ', x))
# print(cdf.head())
# print(cdf.shape)
# print(len(cdf.a_物件名.unique()))
cdf.to_csv('test.csv',index=None,encoding='utf-8')