from flask import Flask, render_template
import ast

app = Flask(__name__)
app.debug = True

def dataFromFile(fileName):
  this_file = open(fileName,'r')
  ret = ast.literal_eval(this_file.read())
  this_file.close()
  return ret

def gameInfo(id):
  for game in dataFromFile('Games'):
    if game[5] == id:
      return game
  return []

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', slides=dataFromFile('Articles'), scores=dataFromFile('Games')[:5], schedule=dataFromFile('Schedule')[:5])

@app.route('/stats')
def stats():
    return render_template('stats.html', hitters=dataFromFile('Hitters'), pitchers=dataFromFile('Pitchers'))

@app.route('/schedule')
def schedule():
    return render_template('schedule.html',upcoming=dataFromFile('Schedule'))

@app.route('/roster')
def roster():
    return render_template('roster.html', players=dataFromFile('Players'))

@app.route('/scores')
def scores():
    return render_template('scores.html',scores=dataFromFile('Games'))

@app.route('/score<int:id>')
def score(id):
    return render_template('boxscore.html',game=gameInfo(id))

@app.route('/news')
def news():
    return render_template('news.html',news=dataFromFile('News'))

@app.route('/zac')
def zac():
    return render_template('zac.html')

if __name__ == '__main__':
    app.run()
