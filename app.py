from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# 仮のコラムデータ（実際はデータベースなどから取得することを想定）
weblogs = [
    {"id": 1, "title": "気まぐれコラム＃１", "date": "2024.06.06", "link": "column1"},
    {"id": 2, "title": "気まぐれコラム＃２", "date": "2024.06.16", "link": "column2"},
    {"id": 3, "title": "気まぐれコラム＃３", "date": "2024.06.21", "link": "column3"},
    {"id": 4, "title": "気まぐれコラム＃４", "date": "2024.07.01", "link": "column4"},
    {"id": 5, "title": "気まぐれコラム＃５", "date": "2024.07.30", "link": "column5"},
    {"id": 6, "title": "気まぐれコラム＃６", "date": "2024.08.16", "link": "column6"},
    {"id": 7, "title": "気まぐれコラム＃７", "date": "2024.08.21", "link": "column7"},
    {"id": 8, "title": "気まぐれコラム＃８", "date": "2024.08.31", "link": "column8"},
    {"id": 9, "title": "気まぐれコラム＃９", "date": "2024.09.08", "link": "column9"},
    {"id": 10, "title": "気まぐれコラム＃１０", "date": "2024.09.15", "link": "column10"},
    {"id": 11, "title": "気まぐれコラム＃１１", "date": "2024.09.20", "link": "column11"},
    {"id": 12, "title": "気まぐれコラム＃１２", "date": "2024.09.29", "link": "column12"},
    {"id": 13, "title": "気まぐれコラム＃１３", "date": "2024.10.17", "link": "column13"},
    {"id": 14, "title": "気まぐれコラム＃１４", "date": "2024.10.25", "link": "column14"},
]

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
    