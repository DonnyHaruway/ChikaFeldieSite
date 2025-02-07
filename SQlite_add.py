import sqlite3
import os
import time

db_dir = 'database'

con = sqlite3.connect(os.path.join(db_dir, 'weblog_columns.sqlite'))
c = con.cursor()

# コラムデータの挿入プログラム(titleは全角で書くこと)
weblogs = [
    {"id": 17, "title": "気まぐれコラム ＃１７", "date": "2025.01.22", "link": "column17"}]

for weblog in weblogs:
    c.execute("INSERT INTO column_db (id, title, date, link)"\
              "VALUES (:id, :title, :date, :link)", weblog)
    
# コミットして接続を閉じる。
con.commit()
con.close()