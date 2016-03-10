from flask import Flask, render_template

app = Flask(__name__)
app.debug = True



@app.route('/')
@app.route('/home')
def index():
    articles=[["Zac Smiles at Camera","http://i.imgur.com/P8nsRbX.jpg"],["Sameer Hits Balls","http://i.imgur.com/y7PQTF7.jpg"],["Darren Throws Balls","http://imgur.com/LiB1npZ.jpg"]]
    games=[["CMU","BU",10,3,"March 6"],["CMU","Xavier",4,15,"March 7"]]
    return render_template('index.html', slides=articles, scores=games)

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/roster')
def roster():
    return render_template('roster.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/zac')
def zac():
    return render_template('zac.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
