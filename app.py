from flask import Flask, render_template
from get_data import get_site_data
from threading import Timer

app = Flask(__name__)
app.debug = True

def load_data():
  raw_data = get_site_data('1QiViqtow-j8fBWSPgtBuwg7NUu2BCykjYKYr1zwGU9Q')

  Players = raw_data[1]
  Schedule = raw_data[2]
  News = raw_data[3]
  print raw_data[4]

  Articles=[]
  for article in News:
    Articles.append(article[:3])

  Playernames = []
  for player in Players:
    Playernames.append([player[0],player[9]])

#[0:AWAY,1:HOME,2:AWAYSCORE,3:HOMESCORE,4:DATE,5:ID,6:WIN(bool),7:AWAY[R,H,E],8:HOME[R,H,E],9:INNINGS[[A,H],[A,H],...],10:HITTERS[ID,NAME,POS,NUMBER,STATS],11:PITCHERS[ID,NAME,NUMBER,STATS]]
#STATS:[PA,AB,R,H,2B,3B,HR,RBI,BB,SO,SB,CS]
#STATS:[W,L,GS,CG,SHO,SV,OUTS,H,R,ER,HR,BB,SO]
  Games = raw_data[4]
#Hitters=[["Aaron Mortenson",4,12,10,0,2,0,0,0,1,2,7,0,0,'.200','.333','.200','.533']]
  Hitters= [None] * len(Players)
  Pitchers= [None] * len(Players)
  for player in Players:
    Hitters[player[9]] = [player[0],0,0,0,0,0,0,0,0,0,0,0,0,0,'.000','.000','.000','.000']
    Pitchers[player[9]] = [player[0],0,0,'0.00',0,0,0,0,0,0,0,0,0,0,0,0,'.000','0.00']

  for game in Games:
    for hitter in game[10]:
      Hitters[hitter[0]][1]+=1 #G
      Hitters[hitter[0]][2]+=hitter[4] #PA
      Hitters[hitter[0]][3]+=hitter[5] #AB
      Hitters[hitter[0]][4]+=hitter[6] #R
      Hitters[hitter[0]][5]+=hitter[7] #H
      Hitters[hitter[0]][6]+=hitter[8] #2B
      Hitters[hitter[0]][7]+=hitter[9] #3B
      Hitters[hitter[0]][8]+=hitter[10] #HR
      Hitters[hitter[0]][9]+=hitter[11] #RBI
      Hitters[hitter[0]][10]+=hitter[12] #BB
      Hitters[hitter[0]][11]+=hitter[13] #SO
      Hitters[hitter[0]][12]+=hitter[14] #SB
      Hitters[hitter[0]][13]+=hitter[15] #CS
    for pitcher in game[11]:
      Pitchers[pitcher[0]][1]+=pitcher[3] #W
      Pitchers[pitcher[0]][2]+=pitcher[4] #L
      Pitchers[pitcher[0]][4]+=1 #G
      Pitchers[pitcher[0]][5]+=pitcher[5] #GS
      Pitchers[pitcher[0]][6]+=pitcher[6] #CG
      Pitchers[pitcher[0]][7]+=pitcher[7] #SHO
      Pitchers[pitcher[0]][8]+=pitcher[8] #SV
      Pitchers[pitcher[0]][9]+=pitcher[9] #IP(OUTS)
      Pitchers[pitcher[0]][10]+=pitcher[10] #H
      Pitchers[pitcher[0]][11]+=pitcher[11] #R
      Pitchers[pitcher[0]][12]+=pitcher[12] #ER
      Pitchers[pitcher[0]][13]+=pitcher[13] #HR
      Pitchers[pitcher[0]][14]+=pitcher[14] #BB
      Pitchers[pitcher[0]][15]+=pitcher[15] #SO

  Hitters = filter(lambda x: x[1] != 0, Hitters)
  Pitchers = filter(lambda x: x[4] != 0, Pitchers)

  for hitter in Hitters:
    if hitter[3] != 0:
      hitter[14] = "%.3f" % (hitter[5]*1.0/hitter[3]) #BA
      hitter[16] = ((hitter[5]+hitter[6]+(2*hitter[7])+(3*hitter[8]))*1.0/hitter[3]) #SLG
    else:
      hitter[16] = 0.0 #SLG
    hitter[15] = ((hitter[5]+hitter[10])*1.0/hitter[2]) #OBP
    hitter[17] = "%.3f" % (hitter[15]+hitter[16]) #OPS
    hitter[15] = "%.3f" % hitter[15]
    hitter[16] = "%.3f" % hitter[16]

  for pitcher in Pitchers:
    pitcher[3] = "%.2f" % (pitcher[12]*21.0/pitcher[9]) #ERA
    pitcher[16] = "%.3f" % (pitcher[10]*1.0/(pitcher[10]+pitcher[9])) #BAA
    pitcher[17] = "%.3f" % ((pitcher[14]+pitcher[10])*3.0/pitcher[9]) #WHIP

  return (Players,Schedule,News,Articles,Playernames,Games,Hitters,Pitchers)


def run_forever():
  global Players,Schedule,News,Articles,Playernames,Games,Hitters,Pitchers
  try:
    Players,Schedule,News,Articles,Playernames,Games,Hitters,Pitchers = load_data()
  except:
    pass
  Timer(300.0, run_forever).start()

run_forever()

def gameInfo(id):
  for game in Games:
    if game[5] == id:
      print game
      return game
  return []

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', slides=Articles, scores=Games[:5], schedule=Schedule[:5])

@app.route('/stats')
def stats():
    return render_template('stats.html', hitters=Hitters, pitchers=Pitchers)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html',upcoming=Schedule)

@app.route('/roster')
def roster():
    return render_template('roster.html', players=Players)

@app.route('/scores')
def scores():
    return render_template('scores.html',scores=Games)

@app.route('/scores/<int:id>')
def score(id):
    return render_template('boxscore.html',game=gameInfo(id))

@app.route('/news')
def news():
    return render_template('news.html',news=News)

@app.route('/upload')
def upload(): 
    return render_template('upload.html')

@app.route('/articleadd')
def articleadd(): 
    return render_template('articleadd.html')

@app.route('/playeradd')
def playeradd(): 
    return render_template('playeradd.html')

@app.route('/playeredit')
def playeredit(): 
    return render_template('playeredit.html', players=Playernames)

@app.route('/gameschedule')
def gameschedule(): 
    return render_template('gameschedule.html')

@app.route('/gameinfo')
def gameinfo(): 
    return render_template('gameinfo.html',players=Players,schedule=Schedule)

@app.route('/zac')
def zac():
    return render_template('zac.html')

if __name__ == '__main__':
    app.run()
