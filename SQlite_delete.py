import sqlite3
import os

db_dir = 'database'

# データベースに接続
con = sqlite3.connect(os.path.join(db_dir, 'weblog_columns.sqlite'))
c = con.cursor()

# id=17 の行を削除
c.execute("DELETE FROM column_db WHERE id = ?", (17,))

# コミットして接続を閉じる
con.commit()
con.close()
