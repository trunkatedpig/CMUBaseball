import MySQLdb
import sys
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
cursor = MySQLdb.connect (host = "192.168.1.2", user = "user", passwd = "password, db = "scripting_mysql")

def getArticles():
	cursor.execute("SELECT * FROM ARTICLES")
	return list(cursor.fetchall()).reverse();

def getNArticles(n,start):
	return getArticles()[start:start+n]

def getNArticles(n):
	cursor.execute("SELECT * FROM ARTICLES")
	result = []
	counter = 0
	for c in cursor:
		if counter < n:
			result.append(c)
	return result

def insertPlayer(values):
	cursor.execute("INSERT INTO PLAYERS VALUES("+join(',',values)+")"

def updatePlayer(values):
	cursor.execute("REPLACE INTO PLAYERS VALUES("+join(',',values)+")"

def getPlayer(id):
	cursor.execute("SELECT * FROM PLAYERS WHERE player_id = "+id)
	return list(cursor.fetcall())[0]