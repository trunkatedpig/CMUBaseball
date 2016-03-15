from flask import Flask, render_template

app = Flask(__name__)
app.debug = True



@app.route('/')
@app.route('/home')
def index():
    articles=[["Zac Smiles at Camera",3,"http://i.imgur.com/P8nsRbX.jpg"],["Sameer Hits Balls",2,"http://i.imgur.com/y7PQTF7.jpg"],["Darren Throws Balls",1,"http://imgur.com/LiB1npZ.jpg"]]
    games=[["CMU","Xavier",4,15,"March 7"],["VCU","CMU",14,17,"March 7"],["Boston University","CMU",3,10,"March 6"],["CMU","George Mason",4,2,"March 6"],["Boyce","CMU",1,14,"October 16"]]
    schedule=[["vs","OSU","March 20"],["at","Boyce","March 26"],["vs","Duqense","March 27"]]
    return render_template('index.html', slides=articles, scores=games, schedule=schedule)

@app.route('/stats')
def stats():
    hitters=[["Aaron Mortenson",4,12,10,0,2,0,0,0,1,2,7,0,0,'.200','.333','.200','.533']]
    pitchers=[]
    return render_template('stats.html', hitters=hitters, pitchers=pitchers)

@app.route('/schedule')
def schedule():
    upcoming=[["vs","OSU","March 20"],["at","Boyce","March 26"],["vs","Duqense","March 27"]]
    scores=[["CMU","Xavier",4,15,"March 7"],["VCU","CMU",14,17,"March 7"],["Boston University","CMU",3,10,"March 6"],["CMU","George Mason",4,2,"March 6"],["Boyce","CMU",1,14,"October 16"]]
    return render_template('schedule.html',upcoming=upcoming,scores=scores)

@app.route('/roster')
def roster():
    players = [["Aaron Mortenson","http://i.imgur.com/UR6rM48.jpg",30,"OF","Freshman","R","R",'''6'0"''',"195"],
               ["Tahj Springer","http://i.imgur.com/xnSAFPh.jpg",43,"2B","Freshman","R","R",'''5'10"''',"120"]]
    return render_template('roster.html', players=players)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    news=[["Zac Smiles at Camera",3,"http://i.imgur.com/P8nsRbX.jpg","March 7, 2016",["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer venenatis ligula ac leo feugiat, eu dignissim arcu sollicitudin. Aliquam vulputate tempor scelerisque. Phasellus finibus convallis nulla non vehicula. Aliquam lacinia orci id imperdiet fermentum. Vestibulum vitae erat lacus. Nam et arcu at turpis viverra accumsan nec quis ligula. Nullam aliquam ac ante nec mollis. Sed sagittis libero quis facilisis aliquam. Nulla in pharetra mi, nec laoreet eros.","Praesent eget laoreet purus, eget gravida odio. Donec eu aliquam est. Integer bibendum tellus enim. Nulla ac lacus et sem suscipit sollicitudin id non quam. Curabitur auctor, risus a aliquam maximus, sem urna vulputate ipsum, et condimentum sem tellus ac neque. Vestibulum urna ligula, ornare quis egestas sed, gravida quis lorem. Donec placerat imperdiet massa at faucibus. Mauris at placerat velit. Fusce et mollis dui. Duis id lacus a sapien pellentesque gravida at ac nunc. Morbi ut tortor et nibh commodo bibendum. Suspendisse eu eros tincidunt, feugiat libero at, blandit leo. In ex lacus, ultrices et aliquam eget, maximus nec neque. Nulla vulputate turpis nec sem dapibus porttitor. Morbi aliquam ligula tortor, quis varius nulla lobortis quis."]],
["Sameer Hits Balls",2,"http://i.imgur.com/y7PQTF7.jpg","March 6, 2016",["Vivamus vitae magna cursus, condimentum quam ac, maximus augue. Suspendisse congue consectetur magna id rutrum. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer facilisis quam diam, eget mattis ipsum lobortis ut. Praesent nulla enim, tincidunt vel justo eget, aliquam tincidunt risus. Etiam suscipit, leo a tristique cursus, metus risus aliquet tellus, nec fermentum lorem lorem eu sem. Fusce elementum ipsum tincidunt ultrices ultrices. In vestibulum ultricies elementum. Quisque consectetur ut sapien sit amet facilisis."]],
["Darren Throws Balls",1,"http://i.imgur.com/LiB1npZ.jpg","March 6, 2016",["Sed semper, sem vel vulputate fringilla, libero magna tincidunt tortor, a tincidunt enim enim suscipit ipsum. Praesent gravida diam pulvinar, dapibus leo sed, gravida leo. Donec aliquet elit enim, vel mattis orci condimentum non. Vestibulum tincidunt odio tellus, ut commodo purus consequat elementum. Suspendisse et lacus gravida magna gravida accumsan. Curabitur maximus risus sit amet malesuada maximus. Donec lobortis tristique eleifend.","Duis nec arcu at mauris auctor mollis. Nam condimentum, dolor ut hendrerit fermentum, orci risus hendrerit mi, ac sagittis nisi est sit amet nulla. Nullam a mollis magna. Donec sollicitudin fringilla leo rutrum suscipit. In vulputate mi odio, porta hendrerit dolor fringilla et. Aliquam euismod nunc felis, et dapibus nisi aliquet vel. Mauris vestibulum nisl id mauris iaculis elementum."]]]
    return render_template('news.html',news=news)

@app.route('/upload')
def upload():
    players=["Alex Walenczyk","Morgan Dively","Darren Kerfoot","Zac Ettensohn"]
    return render_template('upload.html', players=players)

@app.route('/zac')
def zac():
    return render_template('zac.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
