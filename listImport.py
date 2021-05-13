from animeClass import anime

#imports
import sqlite3


conn = sqlite3.connect('anime_sql.db')
print ('connection complete between python and sqlite3...')

#making variables
name = 'test'
genre = 'test'
atype = 'test'
episodes = 12
rating = 1.23

#CREATING LIST
aniList = []

#SQLite Stuff
#IMPORT the myanimelist database

#Using SELECT then send assign them to an object to be appended into the class
animeInsert = conn.execute("SELECT name, genre, type, episodes, rating from anime")

#loop for easier assignment
for row in animeInsert:
    name = row[0]
    genre = row[1]
    atype = row[2]
    episodes = row[3]
    rating = row[4]
    aniList.append(anime(name, atype, genre, rating, episodes))
    
aniListNum = len(aniList)
print(aniListNum)
