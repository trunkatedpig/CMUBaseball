from flask import Flask, render_template

app = Flask(__name__)
app.debug = True



@app.route('/')
@app.route('/home')
def index():
    articles=[["Zac Smiles at Camera","http://i.imgur.com/P8nsRbX.jpg"],["Sameer Hits Balls","http://i.imgur.com/y7PQTF7.jpg"],["Darren Throws Balls","http://imgur.com/LiB1npZ.jpg"]]
    games=[["Boyce","CMU",1,14,"October 16"],["CMU","George Mason",4,2,"March 6"],["Boston University","CMU",3,10,"March 6"],["VCU","CMU",14,17,"March 7"],["CMU","Xavier",4,15,"March 7"]]
    return render_template('index.html', slides=articles, scores=games)

@app.route('/stats')
def stats():
    hitters=[["Aaron Mortenson",4,12,10,0,2,0,0,0,1,2,7,0,0,'.200','.333','.200','.533']]
    pitchers=[]
    return render_template('stats.html', hitters=hitters, pitchers=pitchers)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/roster')
def roster():
    players = [["Aaron Mortenson","http://i.imgur.com/UR6rM48.jpg",30,"OF","Freshman","R","R",'''6'0"''',"195"]]
    return render_template('roster.html', players=players)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/upload')
def upload():
    players=["Alex Walenczyk","Morgan Dively","Darren Kerfoot","Zac Ettensohn"]
    return render_template('upload.html', players=players)

@app.route('/zac')
def zac():
    return render_template('zac.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
