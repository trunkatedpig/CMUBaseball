from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

News=[["Zac Smiles at Camera",3,"http://i.imgur.com/P8nsRbX.jpg","March 7, 2016",["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer venenatis ligula ac leo feugiat, eu dignissim arcu sollicitudin. Aliquam vulputate tempor scelerisque. Phasellus finibus convallis nulla non vehicula. Aliquam lacinia orci id imperdiet fermentum. Vestibulum vitae erat lacus. Nam et arcu at turpis viverra accumsan nec quis ligula. Nullam aliquam ac ante nec mollis. Sed sagittis libero quis facilisis aliquam. Nulla in pharetra mi, nec laoreet eros.","Praesent eget laoreet purus, eget gravida odio. Donec eu aliquam est. Integer bibendum tellus enim. Nulla ac lacus et sem suscipit sollicitudin id non quam. Curabitur auctor, risus a aliquam maximus, sem urna vulputate ipsum, et condimentum sem tellus ac neque. Vestibulum urna ligula, ornare quis egestas sed, gravida quis lorem. Donec placerat imperdiet massa at faucibus. Mauris at placerat velit. Fusce et mollis dui. Duis id lacus a sapien pellentesque gravida at ac nunc. Morbi ut tortor et nibh commodo bibendum. Suspendisse eu eros tincidunt, feugiat libero at, blandit leo. In ex lacus, ultrices et aliquam eget, maximus nec neque. Nulla vulputate turpis nec sem dapibus porttitor. Morbi aliquam ligula tortor, quis varius nulla lobortis quis."]],
["Sameer Hits Balls",2,"http://i.imgur.com/y7PQTF7.jpg","March 6, 2016",["Vivamus vitae magna cursus, condimentum quam ac, maximus augue. Suspendisse congue consectetur magna id rutrum. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer facilisis quam diam, eget mattis ipsum lobortis ut. Praesent nulla enim, tincidunt vel justo eget, aliquam tincidunt risus. Etiam suscipit, leo a tristique cursus, metus risus aliquet tellus, nec fermentum lorem lorem eu sem. Fusce elementum ipsum tincidunt ultrices ultrices. In vestibulum ultricies elementum. Quisque consectetur ut sapien sit amet facilisis."]],
["Darren Throws Balls",1,"http://i.imgur.com/LiB1npZ.jpg","March 6, 2016",["Sed semper, sem vel vulputate fringilla, libero magna tincidunt tortor, a tincidunt enim enim suscipit ipsum. Praesent gravida diam pulvinar, dapibus leo sed, gravida leo. Donec aliquet elit enim, vel mattis orci condimentum non. Vestibulum tincidunt odio tellus, ut commodo purus consequat elementum. Suspendisse et lacus gravida magna gravida accumsan. Curabitur maximus risus sit amet malesuada maximus. Donec lobortis tristique eleifend.","Duis nec arcu at mauris auctor mollis. Nam condimentum, dolor ut hendrerit fermentum, orci risus hendrerit mi, ac sagittis nisi est sit amet nulla. Nullam a mollis magna. Donec sollicitudin fringilla leo rutrum suscipit. In vulputate mi odio, porta hendrerit dolor fringilla et. Aliquam euismod nunc felis, et dapibus nisi aliquet vel. Mauris vestibulum nisl id mauris iaculis elementum."]]]
Articles=[]
for article in News:
  Articles.append(article[:3])
Players = [
          ["Sameer Kolluri","http://i.imgur.com/V26FOLT.png","1","1B","Sophomore","R","R",'''5'11"''',"205",10],
          ["Morgan Dively","http://i.imgur.com/52xFN76.png","2","INF","Sophomore","R","R",'''6'0"''',"190",2],
          ["Alex Walenczyk","http://i.imgur.com/9bWiCbq.png","3","OF","Junior","R","R",'''5'9"''',"165",13],
          ["Cameron Dively","http://imgur.com/0sF7VAd","6","C","Sophomore","R","R",'''6'3"''',"205",11],
          ["Zachary Ettensohn","http://i.imgur.com/BBTdWzt.png","9","1B","Sophomore","L","L",'''6'5"''',"195",4],
          ["Lesther Martinez","http://i.imgur.com/ceEI65D.png","11","INF","Junior","R","R",'''5'5"''',"138",12],
          ["Rainer Nunez","IMAGE HERE","15","P/INF","Sophomore","R","R",'''5'9"''',"184",6],
          ["Darren Kerfoot","IMAGE HERE","20","P/INF","Senior","R","R",'''6'0"''',"205",14],
          ["Bryant Brackus","IMAGE HERE","23","P/OF","Sophomore","R","R",'''6'3"''',"200",19],
          ["Nick Halbedl","IMAGE HERE","25","OF","Junior","L","R",'''5'9"''',"195",8],
          ["Drew Fitzmorris","IMAGE HERE","26","OF","Sophomore","R","R",'''5'11"''',"190",15],
          ["Aaron Mortenson","http://i.imgur.com/nnzRl4k.png","30","OF","Freshman","R","R",'''6'0"''',"195",0],
          ["Tahj Spigner","http://i.imgur.com/VGyvxWO.png","42","INF","Freshman","R","R",'''5'10"''',"145",1],
          ["Jacob Johnson","IMAGE HERE","55","P/INF","Sophomore","R","R",'''5'11"''',"180",18],
          ["Paul Benoit","IMAGE HERE","","OF","Freshman","R","R",'''5'10"''',"150",3],
          ["Kellen Carleton","IMAGE HERE","","INF","Sophomore","R","R",'''5'11"''',"215",5],
          ["Drew Himmelrich","IMAGE HERE","","INF","Sophomore","R","R",'''6'0"''',"180",7],
          ["Travis Andring","IMAGE HERE","","1B","Junior","L","R",'''6'2"''',"235",9],
          ["Josh Solarek","IMAGE HERE","","C/OF","Sophomore","R","R",'''5'11"''',"190",16],
          ["John Ciaccio","IMAGE HERE","","P/INF","Sophomore","R","R",'''6'0"''',"190",17],
          ["Hidetaka Okamura","IMAGE HERE","","IF","Senior","R","R",'''6'1"''',"147",20]]

Playernames = []
for player in Players:
  Playernames.append([player[0],player[9]])

#[0:AWAY,1:HOME,2:AWAYSCORE,3:HOMESCORE,4:DATE,5:ID,6:WIN(bool),7:AWAY[R,H,E],8:HOME[R,H,E],9:INNINGS[[A,H],[A,H],...],10:HITTERS[ID,NAME,POS,NUMBER,STATS],11:PITCHERS[ID,NAME,NUMBER,STATS]]
#STATS:[PA,AB,R,H,2B,3B,HR,RBI,BB,SO,SB,CS]
#STATS:[W,L,GS,CG,SHO,SV,OUTS,H,R,ER,HR,BB,SO]
Games=[["CMU","CCAC Boyce",7,1,"March 26",6,True,[7,10,0],[1,7,1],[[0,0],[1,0],[0,0],[3,0],[0,0],[2,0],[1,1]],
         [[15,"Drew Fitzmorris","LF","26",4,3,0,1,0,1,0,0,1,1,1,0],
          [2,"Morgan Dively","3B","2"    ,4,3,0,0,0,0,0,0,1,0,0,0],
          [13,"Alex Walenczyk","CF","3"  ,4,4,0,2,1,0,0,0,0,1,0,1],
          [4,"Zachary Ettensohn","1B","9",4,3,1,2,0,0,0,0,1,1,0,0],
          [16,"Josh Solarek","C","12"    ,4,1,3,0,0,0,0,0,3,0,1,0],
          [1,"Tahj Spigner","2B","42"   ,4,3,1,2,0,0,0,0,1,0,1,0],
          [19,"Bryant Brackus","DH","23" ,4,2,0,0,0,0,0,2,1,0,0,2],
          [18,"Jacob Johnson","SS","30"  ,4,3,1,1,0,0,0,1,1,2,1,0],
          [11,"Cameron Dively","RF","6"  ,4,3,1,0,0,0,0,0,1,3,0,0],
          [8,"Nick Halbedl","EH","25"    ,3,3,0,2,0,0,0,2,0,0,0,1]],
         [[10,"Sameer Kolluri","1",1,0,1,1,0,0,21,7,1,1,0,0,4]]],
       ["CMU","CCAC Boyce",12,1,"March 26",5,True,[12,8,0],[1,4,2],[[1,1],[3,0],[1,0],[1,0],[3,0],[0,0],[3,0]],
          #ID,NAME,POS,NUMBER             ,P,A,R,H,2,3,4,B,W,K,S,C
         [[15,"Drew Fitzmorris","LF","26" ,5,3,2,1,0,1,0,1,2,0,1,0],
          [2,"Morgan Dively","3B","2"     ,5,2,0,0,0,0,0,0,3,1,0,0],
          [13,"Alex Walenczyk","CF","3"   ,5,3,1,0,0,0,0,1,1,0,2,0],
          [4,"Zachary Ettensohn","1B","9" ,5,4,0,1,0,0,0,0,1,1,0,0],
          [16,"Josh Solarek","C","12"     ,4,4,2,2,1,0,0,0,0,0,0,0],
          [8,"Nick Halbedl","RF","25"     ,4,3,0,0,0,0,0,0,1,1,0,0],
          [1,"Tahj Spigner","2B","42"    ,3,2,1,0,0,0,0,1,1,0,2,0],
          [20,"Hidetaka Okamura","2B","11",1,0,1,0,0,0,0,0,1,0,0,0],
          [11,"Cameron Dively","EH","6"   ,4,2,1,0,0,0,0,0,2,2,1,0],
          [19,"Bryant Brackus","P","23"   ,4,4,3,3,1,0,0,1,0,0,1,0],
          [10,"Sameer Kolluri","3B","1"   ,4,3,1,1,0,0,0,1,1,0,0,0]],
         [[19,"Bryant Brackus","23",1,0,1,0,0,0,15,2,1,1,0,3,5],
          [18,"Jacob Johnson","15" ,0,0,0,0,0,0,6 ,2,0,0,0,1,5]]],
       ["CMU","Xavier",4,15,"March 7",4,False,[0,0,0],[0,0,0],[],[],[]],
       ["VCU","CMU",14,17,"March 7",3,True,[0,0,0],[0,0,0],[],[],[]],
       ["Boston University","CMU",3,13,"March 6",2,True,[0,0,0],[0,0,0],[],[],[]],
       ["CMU","George Mason",4,2,"March 6",1,True,[0,0,0],[0,0,0],[],[],[]]]

Schedule=[["vs","Duquense","April 2","12:00 PM","at Bellevue Memorial",7],
          ["vs","Duquense","April 2","3:00 PM","at Bellevue Memorial",8],
          ["vs","Duquense","April 3","12:00 PM","at Bellevue Memorial",9],
          ["vs","Cal Pa.","April 9","12:00 PM","at Bellevue Memorial",10],
          ["vs","Cal Pa.","April 9","3:00 PM","at Bellevue Memorial",11],
          ["vs","Cal Pa.","April 10","10:00 AM","at Esmark Field",12],
          ["vs","WVU","April 23","12:00 PM","At Bellevue Memorial",13],
          ["vs","WVU","April 24","12:00 PM","at Bellevue Memorial",14],
          ["vs","WVU","April 24","3:00 PM","at Bellevue Memorial",15]]
#Hitters=[["Aaron Mortenson",4,12,10,0,2,0,0,0,1,2,7,0,0,'.200','.333','.200','.533']]
Hitters=[]
Pitchers=[]
for player in Players:
  Hitters.append([])
  Pitchers.append([])
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

@app.route('/score<int:id>')
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
