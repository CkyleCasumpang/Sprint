#CLASS CREATION
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
#TESTING
#anime1 = anime('name', 'atype', 'genre', 8.6, 23, 'Autumn', 2020)

#anime1.printInfo()

