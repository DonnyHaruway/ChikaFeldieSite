from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live_info')
def live_info():
    return render_template('live_info.html')

@app.route('/weblog')
def weblog():
    return render_template('weblog.html')

@app.route('/weblog/column9')
def weblog_column9():
    return render_template("weblog_columns/column9.html")

@app.route('/weblog/column8') 
def weblog_column8():
    return render_template("weblog_columns/column8.html")

@app.route('/weblog/column7')
def weblog_column7():
    return render_template("weblog_columns/column7.html")

@app.route('/weblog/column6')
def weblog_column6():
    return render_template("weblog_columns/column6.html")

@app.route('/weblog/column5')
def weblog_column5():
    return render_template("weblog_columns/column5.html")

@app.route('/weblog/column4')
def weblog_column4():
    return render_template("weblog_columns/column4.html")

@app.route('/weblog/column3')
def weblog_column3():
    return render_template("weblog_columns/column3.html")

@app.route('/weblog/column2')
def weblog_column2():
    return render_template("weblog_columns/column2.html")

@app.route('/weblog/column1')
def weblog_column1():
    return render_template("weblog_columns/column1.html")

@app.route('/works')
def works():
    return render_template('works.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8888)
