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

@app.route('/works')
def works():
    return render_template('works.html')

if __name__ == '__main__':
    app.run(debug=True)
