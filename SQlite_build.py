import sqlite3
import os
import time

db_dir = 'database'

con = sqlite3.connect(os.path.join(db_dir, 'weblog_columns.sqlite'))
c = con.cursor()

# 一回作ったからもういい
# c.execute("CREATE TABLE column_db (id INTEGER PRIMARY KEY, title TEXT, date TEXT, link TEXT)")

# 仮のコラムデータ（実際はデータベースなどから取得することを想定）
weblogs = [
    {"id": 15, "title": "気まぐれコラム＃１５", "date": "2024.11.17", "link": "column15"},
    {"id": 16, "title": "気まぐれコラム＃１６", "date": "2024.11.30", "link": "column16"},
    ]

for weblog in weblogs:
    c.execute("INSERT INTO column_db (id, title, date, link)"\
              "VALUES (:id, :title, :date, :link)", weblog)
    
# コミットして接続を閉じる。
con.commit()
con.close()