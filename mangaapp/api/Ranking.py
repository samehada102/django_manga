import requests
from bs4 import BeautifulSoup

def getRanking():
    # めちゃコミの少年漫画ランキングサイト
    url = "https://mechacomic.jp/sales_rankings/monthly?genre=1"
    htmltext = requests.get(url).text
    soup = BeautifulSoup(htmltext, "lxml")

    #変数のリストを定義
    ranklist = []
    titlelist = []

    for el in soup.find_all("div", class_="p-book u-clearfix"):
        # 順位部分を抽出
        rank = el.find("div", class_="p-book_detail").contents[1].contents[0].strip()
        # 作品名を抽出
        title = el.find("dt", class_="p-book_title").contents[1].contents[0].strip()

        # リストに追加
        ranklist.append(rank)
        titlelist.append(title)


    return ranklist,titlelist