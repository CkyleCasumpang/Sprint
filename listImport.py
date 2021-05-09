#imports
import sqlite3
class anime:
    def __init__(self, name, atype, genre, rating,
     episodes):
        self.name = name
        self.type = atype
        self.genre = genre
        self.rating = rating
        self.episodes = episodes

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getType(self):
        return self.type

    def setType(self,atype):
        self.type = atype

    def getGenre(self):
        return self.genre

    def setGenre(self,genre):
        self.genre = genre
    
    def getRating(self):
        return self.rating

    def setRating(self,rating):
        self.rating = rating
    
    def getEpisodes(self):
        return self.episodes

    def setEpisodes(self,episodes):
        self.episodes = episodes

    def printInfo(self):
        print (
            " Name: ", self.name, '\n'
            ,"Type: ", self.type, '\n'
            ,"Genre: ", self.genre, '\n'
            ,"Rating: ", self.rating, '\n'
            ,"Episodes:", self.episodes, '\n'
        )

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
    name = row[1]
    genre = row[2]
    atype = row[3]
    episodes = row[4]
    aniList.append(anime(name, atype, genre, rating, episodes))
    
print(aniList[0].name)
