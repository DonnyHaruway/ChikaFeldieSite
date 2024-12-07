from flask import Flask, render_template, request
from datetime import datetime
import sqlite3
import os

##### DBと紐づける
db_dir = 'database'
con = sqlite3.connect(os.path.join(db_dir, 'weblog_columns.sqlite'))
cur = con.cursor()

cur.execute("SELECT id, title, date, link FROM column_db")
rows = cur.fetchall()

# リスト形式に変換
weblogs = [{'id': row[0], 'title': row[1], 'date': row[2], 'link': row[3]} for row in rows]
con.close()

###### Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live_info')
def live_info():
    return render_template('live_info.html')

@app.route('/weblog')
def weblog():
    # dateを基準に降順で並び替え
    sorted_weblogs = sorted(weblogs, key=lambda x: datetime.strptime(x['date'], '%Y.%m.%d'), reverse=True)
    
    page = request.args.get('page', 1, type=int)  # URLからページ番号を取得
    per_page = 10  # 1ページに表示するコラムの数
    start = (page - 1) * per_page
    end = start + per_page
    paginated_weblogs = sorted_weblogs[start:end]  # 表示する範囲のコラムを取得
    total_pages = (len(weblogs) - 1) // per_page + 1  # 全ページ数を計算
    
    return render_template('weblog.html', weblogs=paginated_weblogs, page=page, total_pages=total_pages)

# Weblogの個別コラムページ
@app.route('/weblog/column<int:column>')
def weblog_column(column):
    total_columns = len(weblogs)  # 総コラム数を取得
    return render_template(f"weblog_columns/column{column}.html", column=column, total_columns=total_columns)

# Worksページ
@app.route('/works')
def works():
    return render_template('works.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8888)