# 【Python x スクレイピング入門】 はやたす(YouTube)

2023/10/1 ~  10/4

## 01_スクレイピングとは？注意点3つと必要なライブラリを紹介

注意点

- 規約違反になっていないか
- サーバーに負荷をかけないようにする
- 著作権侵害していないか

必要なライブラリ

- Requests
- BeautifulSoup
- time
- Selenium ..JavaScriptを使ったサイトをスクレイピングするとき

環境

- Anaconda

## 02_Requestsを使ってWebページにアクセスしてみよう

スクレイピングの流れ

1. RequestsでHTMLを取得
2. 取得したHTMLを解析(BeautifulSoup)
3. 欲しい情報を取得

## 03_BeautifulSoupの使い方①

BeautifulSoupとは、HTMLを解析するためのライブラリ
BeautifulSoupでHTMLを解析するときは、文字列が対象となる

## 04_BeautifulSoupで複数の要素を取得する方法(find_all)をマスターしよう

- find_all(タグ)で、任意のタグを取得し、(リスト型)
- この中からテキストのみを取得するときは for 文を使って取得する

## 05_クラスを指定して複数の要素を取得する方法をマスターしよう

- find_all([,]class_='')
- tag.text でテキストのみを取得

取得する範囲を狭くする方法

- soup.find().find_all()
- body = soup.find()
  body.find_all()

ノイズ要素を削除する方法

- soup.find().extract()

## 06_不動産情報の取得①

利用規約でスクレイピングが禁止されていないか確認  
検索キーワード

- 自動
- ロボット
- クローリング
- スクレイピング など

複数ページにアクセスすることを想定  

```python
url = 'https://suumo.jp/chintai/tokyo/sc_shinjuku/?page{}'
target_url = url.format(1)
```

## 07_不動産情報の取得②

unpack  
list = [1,2,3,4,5]
a,b =lise[2:4] -> a = 3, b = 4

from pprint import pprint  
pprint()

## 08_複数ページからの情報取得をマスターしよう

from time import sleep  
sleep(n) ..n秒間、Pythonの実行を休止する  
複数ページに対してスクレイピングするときは、相手のサーバーに負荷をかけないために、それぞれのリクエスト間に数秒のスリープを挟んであげる必要がある  

## 09_スクレイピングしたデータをＣＳＶに保存しよう

Pandasのインポート  
import pandas as pd  

取得したデータを表形式にする  

- スクレイピングした結果が入っているリストをデータフレーム(表)に変換  
  
  ```python
  df = pd.DataFrame(dlist)
  ```

- 中身の確認  
  df.head()と書くことで先頭の５行を確認できる

  ```python
  print(df.head())
  ```

  表の大きさを確認するときは、df.shape  
  物件名の重複を削除してその大きさを確認する ..len(df.a_物件名.unique())

  reをインポートし、不要な文字列、\r,\n,\t を削除する  
  import re
  df2 = df.applymap(lambda x: re.sub('\n', ' ', x))
  df3 = df2.applymap(lambda x: re.sub('\r', ' ', x))
  cdf = df3.applymap(lambda x: re.sub('\t', ' ', x))

- 表形式の取得結果をCSVに出力する  
  cdf.to_csv('ファイル名',index=None,encoding='utf-8-sig')  

## 10_Seleniumを使ったスクレイピングに挑戦しよう

Selenium(セレニウム)は、Webブラウザの操作を自動化するためのツール  
Seleniumを使うと、JavaScriptが使われているサイトでも、スクレイピングできるようになる  

1. ツールのSelenium本体をダウンロードする  
  以下のURLからSelenium本体のダウンロードができる  
  <https://sites.google.com/a/chromium.org/chromedriver/downloads>
2. PythonライブラリのSeleniumをインストールする  
  pip install selenium
3. Pythonで使えるようにする  
  from selenium import webdriver  
  from selenium.webdriver.chrome.options import Options  

SeleniumはgoogleColabで動かすよりPythonファイルで動かす方がいい  

## 11_Seleniumを使ってYahoo！で自動検索してみよう

ダウンロードしたchromedriver.exeは、実行するPythonファイルと同一フォルダにおく  

- driver.get('url') ..開始  
- sleep() ..適宜配置  
- driver.quit() ..終了

- driver.find_element_by_class_name('クラス名')  
- .send_keys(入力するテキスト)  
- .submit()  

## 12_ブラウザを自動スクロールしよう

driver.execute_script("JavaScript文")  
driver.execute_script("window.scrollTo(0, {});".format(height))  

## 13_自動で画像保存の準備！画像URLを取得しよう

- .find_element_by_class_name('')  
- .find_element_by_tag_name('')  
- .get_attribute('')  

データフレーム化  

- df = pd.DataFrame(リスト)

CSVに出力  

- df.to_csv('ファイル名')  

## 14_自動で画像を保存しよう

IMAGE_DIR = "./images/" ..画像を保存するディレクトリ  

image = requests.get('url')  

with open(IMAGE_DIR + file_name + ".jpg", "wb") as f:
  f.write(image.content)  

import random  
sleep(random.randint(1, 10)) ..とすることでより人間らしくなり、スクレイピングの規制にひっかかりにくくなる  
