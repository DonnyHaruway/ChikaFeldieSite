import sqlite3
import os
import time

db_dir = 'database'

con = sqlite3.connect(os.path.join(db_dir, 'weblog_columns.sqlite'))
c = con.cursor()

# 一回作ったからもういい
c.execute("CREATE TABLE column_db (id INTEGER PRIMARY KEY, title TEXT, date TEXT, link TEXT)")
    
# コミットして接続を閉じる。
con.commit()
con.close()