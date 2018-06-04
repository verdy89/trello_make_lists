# coding:utf-8

from trello import TrelloApi
import datetime

### trelloにアクセスする ###
token = # my token
key = # my key
usr = TrelloApi(key)
usr.set_token(token)

"""
import trello
print(trello.__file__)
# もとのscriptをtrello.pyにしていたら、それがimportされてしまった
"""

# ボードID
idBoard = #board id

"""
### ボード上のリスト名とそのidを表示 ###
lists = usr.boards.get_list(idBoard)
for list in lists:
	print(list['name'])
"""

### 日ごとのリストを毎日自動生成する ###
# n日先の日付の取得
n = 10
delta = datetime.timedelta(days = n)
dist = datetime.date.today() + delta

# 曜日
youbi_list = [u"月", u"火", u"水", u"木", u"金", u"土", u"日"]
youbi = youbi_list[dist.weekday()]

# 追加するリスト名の文字列生成
month = '{0:%m}'.format(dist)
day   = '{0:%d}'.format(dist)
dist_str = month + "/" + day + "(" + youbi + ")"
print(dist_str) # 06/02(土)

# リストの作成
# 後ろに追加してほしいなあ
usr.lists.new(dist_str, idBoard)
