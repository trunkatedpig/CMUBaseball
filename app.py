from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

News=[["Zac Smiles at Camera",3,"http://i.imgur.com/P8nsRbX.jpg","March 7, 2016",["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer venenatis ligula ac leo feugiat, eu dignissim arcu sollicitudin. Aliquam vulputate tempor scelerisque. Phasellus finibus convallis nulla non vehicula. Aliquam lacinia orci id imperdiet fermentum. Vestibulum vitae erat lacus. Nam et arcu at turpis viverra accumsan nec quis ligula. Nullam aliquam ac ante nec mollis. Sed sagittis libero quis facilisis aliquam. Nulla in pharetra mi, nec laoreet eros.","Praesent eget laoreet purus, eget gravida odio. Donec eu aliquam est. Integer bibendum tellus enim. Nulla ac lacus et sem suscipit sollicitudin id non quam. Curabitur auctor, risus a aliquam maximus, sem urna vulputate ipsum, et condimentum sem tellus ac neque. Vestibulum urna ligula, ornare quis egestas sed, gravida quis lorem. Donec placerat imperdiet massa at faucibus. Mauris at placerat velit. Fusce et mollis dui. Duis id lacus a sapien pellentesque gravida at ac nunc. Morbi ut tortor et nibh commodo bibendum. Suspendisse eu eros tincidunt, feugiat libero at, blandit leo. In ex lacus, ultrices et aliquam eget, maximus nec neque. Nulla vulputate turpis nec sem dapibus porttitor. Morbi aliquam ligula tortor, quis varius nulla lobortis quis."]],
["Sameer Hits Balls",2,"http://i.imgur.com/y7PQTF7.jpg","March 6, 2016",["Vivamus vitae magna cursus, condimentum quam ac, maximus augue. Suspendisse congue consectetur magna id rutrum. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer facilisis quam diam, eget mattis ipsum lobortis ut. Praesent nulla enim, tincidunt vel justo eget, aliquam tincidunt risus. Etiam suscipit, leo a tristique cursus, metus risus aliquet tellus, nec fermentum lorem lorem eu sem. Fusce elementum ipsum tincidunt ultrices ultrices. In vestibulum ultricies elementum. Quisque consectetur ut sapien sit amet facilisis."]],
["Darren Throws Balls",1,"http://i.imgur.com/LiB1npZ.jpg","March 6, 2016",["Sed semper, sem vel vulputate fringilla, libero magna tincidunt tortor, a tincidunt enim enim suscipit ipsum. Praesent gravida diam pulvinar, dapibus leo sed, gravida leo. Donec aliquet elit enim, vel mattis orci condimentum non. Vestibulum tincidunt odio tellus, ut commodo purus consequat elementum. Suspendisse et lacus gravida magna gravida accumsan. Curabitur maximus risus sit amet malesuada maximus. Donec lobortis tristique eleifend.","Duis nec arcu at mauris auctor mollis. Nam condimentum, dolor ut hendrerit fermentum, orci risus hendrerit mi, ac sagittis nisi est sit amet nulla. Nullam a mollis magna. Donec sollicitudin fringilla leo rutrum suscipit. In vulputate mi odio, porta hendrerit dolor fringilla et. Aliquam euismod nunc felis, et dapibus nisi aliquet vel. Mauris vestibulum nisl id mauris iaculis elementum."]]]
Articles=[]
for article in News:
  Articles.append(article[:3])
Players = [["Aaron Mortenson","http://i.imgur.com/UR6rM48.jpg","30","OF","Freshman","R","R",'''6'0"''',"195",1],
          ["Tahj Springer","http://i.imgur.com/xnSAFPh.jpg","42","INF","Freshman","R","R",'''5'10"''',"145",2],
          ["Morgan Dively","IMAGE HERE","2","INF","Sophomore","R","R",'''6'0"''',"190",3],
          ["Paul Benoit","IMAGE HERE","","OF","Freshman","R","R",'''5'10"''',"150",4],
          ["Zachary Ettensohn","IMAGE HERE","9","1B","Sophomore","L","L",'''6'5"''',"195",5],
          ["Kellen Carleton","IMAGE HERE","","INF","Sophomore","R","R",'''5'11"''',"215",6],
          ["Rainer Nunez","IMAGE HERE","15","P/INF","Sophomore","R","R",'''5'9"''',"195",7],
          ["Drew Himmelrich","IMAGE HERE","","INF","Sophomore","R","R",'''6'0"''',"180",8],
          ["Nick Halbedl","IMAGE HERE","25","OF","Junior","L","R",'''6'0"''',"195",9],
          ["Travis Andring","IMAGE HERE","1","1B","Junior","L","R",'''6'2"''',"235",10],
          ["Sameer Kolluri","IMAGE HERE","55","1B","Sophomore","R","R",'''5'11"''',"205",11],
          ["Cameron Dively","IMAGE HERE","6","C","Sophomore","R","R",'''6'3"''',"205",12],
          ["Lesther Martinez","IMAGE HERE","","INF","Junior","R","R",'''5'5"''',"138",13],
          ["Alex Walenczyk","IMAGE HERE","3","OF","Junior","R","R",'''5'9"''',"165",14],
          ["Darren Kerfoot","IMAGE HERE","20","P/INF","Senior","R","R",'''6'0"''',"205",15],
          ["Drew Fitzmorris","IMAGE HERE","11","OF","Sophomore","R","R",'''5'11"''',"190",16],
          ["Josh Solarek","IMAGE HERE","26","C/OF","Sophomore","R","R",'''5'11"''',"190",17],
          ["John Ciaccio","IMAGE HERE","","P/INF","Sophomore","R","R",'''6'0"''',"190",18],
          ["Jacob Johnson","IMAGE HERE","","P/INF","Sophomore","R","R",'''5'11"''',"180",19],
          ["Bryant Brackus","IMAGE HERE","23","P/OF","Sophomore","R","R",'''6'3"''',"200",20]]

Playernames = []
for player in Players:
  Playernames.append([player[0],player[9]])
Games=[["CMU","Xavier",4,15,"March 7"],["VCU","CMU",14,17,"March 7"],["Boston University","CMU",3,10,"March 6"],["CMU","George Mason",4,2,"March 6"],["Boyce","CMU",1,14,"October 16"]]
Schedule=[["at","CCAC Boyce","March 26","12:00PM","",6],["at","CCAC Boyce","March 26","3:00 PM","",7],["vs","Duqense","April 2","12:00 PM","at Bellevue Memorial",8],["vs","Duqense","April 2","3:00 PM","at Bellevue Memorial",9],["vs","Duqense","April 3","12:00 PM","at Bellevue Memorial",10],["vs","Cal Pa.","April 9","12:00 PM","at Bellevue Memorial",11],["vs","Cal Pa.","April 9","3:00 PM","at Bellevue Memorial",12],["vs","Cal Pa.","April 10","10:00 AM","at Esmark Field",13],["vs","WVU","April 23","12:00 PM","At Bellevue Memorial",14],["vs","WVU","April 24","12:00 PM","at Bellevue Memorial",15],["vs","WVU","April 24","3:00 PM","at Bellevue Memorial",16]]
Scores=[["CMU","Xavier",4,15,"March 7"],["VCU","CMU",14,17,"March 7"],["Boston University","CMU",3,10,"March 6"],["CMU","George Mason",4,2,"March 6"],["Boyce","CMU",1,14,"October 16"]]
Hitters=[["Aaron Mortenson",4,12,10,0,2,0,0,0,1,2,7,0,0,'.200','.333','.200','.533']]
Pitchers=[]

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
    return render_template('scores.html',scores=Scores)

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
    app.run(host='0.0.0.0', port=8000)
