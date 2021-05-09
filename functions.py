import animeClass
#for setting the filters
#ep num, genre, type, and rating

def filterGenre(genreTKList):
    #list of genres
    genreList = []
    #fills the list if the genre is selected
    for genre in genreTKList:
        if genre == True:
            #not final code might depend on how to get the text of the selector
            genreList.append(str(genre))

    #assigns the amount of genres to this var
    genreListNum = len(genreList)

    #turns the list into a string in one var
    genreFinal = ""
    for genre in genreList[:-1]:
        genreFinal = genreFinal + genre + ","
    genreFinal = genreFinal + genreList[genreListNum-1]

    return genreFinal

#for finding the animes
#genreFilter comes from a var that has the filterGenre function
#just add more arguments in the function depending on the names of the tkinter stuff
def find(genreTKList, typeString, episodeString, ratingString, aniListObjs):
    #list for anime that will be recommended
    animeRecommend = []
    #gets a string genre
    genreFilter = filterGenre(genreTKList)

    #if statements for typeString
    for sampleType in aniListObjs:
        if  sampleType.getType() == typeString:
            animeRecommend.append(sampleType)
    
    for sampleGenre in animeRecommend:
        if sampleGenre.getGenre() != genreFilter:
            animeRecommend.remove(sampleGenre)

    for sampleEpisode in animeRecommend:
        #depends on the range
        if sampleEpisode.getEpisode() < 12:
            cursor.execute("SELECT * FROM anime where episodes<12")
            result = cursor.fetchall()
            print(result)
        if sampleEpisode.getEpisode() >= 24:
            cursor.execute("SELECT * FROM anime where episodes>12 AND episodes<25")
            result = cursor.fetchall()
            print(result)
        if sampleEpisode.getEpisode() > 25:
            cursor.execute("SELECT * FROM anime where episodes>25")
            result = cursor.fetchall()
            print(result)

    for sampleRating in animeRecommend:
        #depends on the range
        if sampleRating.getRating() 
    



