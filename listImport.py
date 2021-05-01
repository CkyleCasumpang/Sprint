#imports
import sqlite3
import animeClass

conn = sqlite3.connect('anime.db')
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
#importing the myanimelist database

#Using SELECT then send assign them to an object to be appended into the class
animeInsert = conn.execute("SELECT name, genre, type, episodes, rating from ANIME")

#loop for easier assignment
for row in animeInsert:
    name = row[1]
    genre = row[2]
    atype = row[3]
    episodes = row[4]
    rating = row[5]
    aniList.append(anime(name, atype, genre, rating, episodes))

