import animeClass
from animeClass import *
import listImport
from listImport import *

#tkinter for GUI
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import *


class App:
    def __init__(self, root):
        #setting title
        root.title("aniSearch")
        #setting window size
        root.geometry("1300x706")
        root.configure(bg = '#efecec')
        root.resizable(width=False, height=False)

        self.epTTK=ttk.Combobox(root)
        self.epTTK["values"]=["Any", "13 and Below", "14 up to 26", "27 and up" ]
        self.epTTK.current(0)
        self.epTTK["justify"] = "center"
        self.epTTK.place(x=15,y=180,width=90,height=30)

        self.labelRecommendedAnimeVar = StringVar()
        self.labelRecommendedAnime = tk.Label(root, textvariable = self.labelRecommendedAnimeVar)
        ft = tkFont.Font(family='Times',size=14)
        self.labelRecommendedAnime["font"] = ft
        self.labelRecommendedAnime["justify"] = "center"
        self.labelRecommendedAnime.place(x = 640, y = 50, width = 660, height = 656)


        labelRec=tk.Label(root)
        labelRec["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=26)
        labelRec["font"] = ft
        labelRec["text"] = "Recommended Anime"
        labelRec["justify"] = "center"
        labelRec.place(x=640,y=0,width=660,height=50)

        labelSep=tk.Label(root)
        labelSep["bg"] = "black"
        labelSep.place(x=635,y=0,width=5,height=706)

        labelEpisodes=tk.Label(root)
        labelEpisodes["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=22)
        labelEpisodes["font"] = ft
        labelEpisodes["fg"] = "#000000"
        labelEpisodes["justify"] = "center"
        labelEpisodes["text"] = "Episodes"
        labelEpisodes.place(x=0,y=140,width=140,height=30)

        labelRatings=tk.Label(root)
        labelRatings["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=15)
        labelRatings["font"] = ft
        labelRatings["fg"] = "#000000"
        labelRatings["justify"] = "center"
        labelRatings["text"] = "Ratings/Rankings"
        labelRatings.place(x=250,y=140,width=140,height=30)

        typeLabel=tk.Label(root)
        typeLabel["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=22)
        typeLabel["font"] = ft
        typeLabel["fg"] = "#333333"
        typeLabel["justify"] = "center"
        typeLabel["text"] = "Type"
        typeLabel.place(x=490,y=140,width=140,height=30)

        self.ratingsTTK=ttk.Combobox(root)
        self.ratingsTTK["values"]=["No order", "Highest Rated", "Worst Rated"]
        self.ratingsTTK.current(0)
        self.ratingsTTK["justify"] = "center"
        self.ratingsTTK.place(x=275,y=180,width=90,height=30)    

        self.typeTTK=ttk.Combobox(root)
        self.typeTTK["values"]=["Any","Movie", "TV", "OVA", "Special", "Music", "ONA"]
        self.typeTTK.current(0)
        self.typeTTK["justify"] = "center"
        self.typeTTK.place(x=520,y=180,width=90,height=30) 


        logoLabel=tk.Label(root)
        logoLabel["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=98)
        logoLabel["font"] = ft
        logoLabel["fg"] = "#333333"
        logoLabel["justify"] = "center"
        logoLabel["text"] = "AniSearch"
        logoLabel.place(x=0,y=0,width=635,height=115)

        genreLabel=tk.Label(root)
        genreLabel["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=22)
        genreLabel["font"] = ft
        genreLabel["fg"] = "#333333"
        genreLabel["justify"] = "center"
        genreLabel["text"] = "Genre"
        genreLabel.place(x=0,y=340,width=635,height=30)

        #Int variables
        #the assign to object
        self.actionVar = IntVar()
        action=tk.Checkbutton(root)
        action["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        action["font"] = ft
        action["fg"] = "#333333"
        action["justify"] = "center"
        action["text"] = "Action"
        action.place(x=0,y=380,width=70,height=25)
        action["offvalue"] = 0
        action["onvalue"] = 1
        action["variable"] = self.actionVar

        self.adventureVar = IntVar()
        adventure=tk.Checkbutton(root)
        adventure["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        adventure["font"] = ft
        adventure["fg"] = "#333333"
        adventure["justify"] = "center"
        adventure["text"] = "Adventure"
        adventure.place(x=0,y=410,width=70,height=25)
        adventure["offvalue"] = 0
        adventure["onvalue"] = 1
        adventure["variable"] = self.adventureVar

        self.carsVar = IntVar()
        cars=tk.Checkbutton(root)
        cars["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        cars["font"] = ft
        cars["fg"] = "#333333"
        cars["justify"] = "center"
        cars["text"] = "Cars"
        cars.place(x=0,y=440,width=70,height=25)
        cars["offvalue"] = 0
        cars["onvalue"] = 1
        cars["variable"] = self.carsVar

        self.comedyVar = IntVar()
        comedy=tk.Checkbutton(root)
        comedy["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        comedy["font"] = ft
        comedy["fg"] = "#333333"
        comedy["justify"] = "center"
        comedy["text"] = "Comedy"
        comedy.place(x=0,y=470,width=70,height=25)
        comedy["offvalue"] = 0
        comedy["onvalue"] = 1
        comedy["variable"] = self.comedyVar

        self.dementiaVar = IntVar()
        dementia=tk.Checkbutton(root)
        dementia["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        dementia["font"] = ft
        dementia["fg"] = "#333333"
        dementia["justify"] = "center"
        dementia["text"] = "Dementia"
        dementia.place(x=0,y=500,width=70,height=25)
        dementia["offvalue"] = 0
        dementia["onvalue"] = 1
        dementia["variable"] = self.dementiaVar

        self.ecchiVar = IntVar()
        ecchi=tk.Checkbutton(root)
        ecchi["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        ecchi["font"] = ft
        ecchi["fg"] = "#333333"
        ecchi["justify"] = "center"
        ecchi["text"] = "Ecchi"
        ecchi.place(x=0,y=590,width=70,height=25)
        ecchi["offvalue"] = 0
        ecchi["onvalue"] = 1
        ecchi["variable"] = self.ecchiVar

        self.fantasyVar = IntVar()
        fantasy=tk.Checkbutton(root)
        fantasy["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        fantasy["font"] = ft
        fantasy["fg"] = "#333333"
        fantasy["justify"] = "center"
        fantasy["text"] = "Fantasy"
        fantasy.place(x=100,y=380,width=70,height=25)
        fantasy["offvalue"] = 0
        fantasy["onvalue"] = 1
        fantasy["variable"] = self.fantasyVar

        self.gameVar = IntVar()
        game=tk.Checkbutton(root)
        game["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        game["font"] = ft
        game["fg"] = "#333333"
        game["justify"] = "center"
        game["text"] = "Game"
        game.place(x=100,y=410,width=70,height=25)
        game["offvalue"] = 0
        game["onvalue"] = 1
        game["variable"] = self.gameVar

        self.psychologicalVar = IntVar()
        psychological=tk.Checkbutton(root)
        psychological["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=7)
        psychological["font"] = ft
        psychological["fg"] = "#333333"
        psychological["justify"] = "center"
        psychological["text"] = "Psychological"
        psychological.place(x=320,y=440,width=70,height=25)
        psychological["offvalue"] = 0
        psychological["onvalue"] = 1
        psychological["variable"] = self.psychologicalVar

        self.romanceVar = IntVar()
        romance=tk.Checkbutton(root)
        romance["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        romance["font"] = ft
        romance["fg"] = "#333333"
        romance["justify"] = "center"
        romance["text"] = "Romance"
        romance.place(x=320,y=470,width=70,height=25)
        romance["offvalue"] = 0
        romance["onvalue"] = 1
        romance["variable"] = self.romanceVar

        self.samuraiVar = IntVar()
        samurai=tk.Checkbutton(root)
        samurai["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        samurai["font"] = ft
        samurai["fg"] = "#333333"
        samurai["justify"] = "center"
        samurai["text"] = "Samurai"
        samurai.place(x=320,y=500,width=70,height=25)
        samurai["offvalue"] = 0
        samurai["onvalue"] = 1
        samurai["variable"] = self.samuraiVar

        self.schoolVar = IntVar()
        school=tk.Checkbutton(root)
        school["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        school["font"] = ft
        school["fg"] = "#333333"
        school["justify"] = "center"
        school["text"] = "School"
        school.place(x=320,y=530,width=70,height=25)
        school["offvalue"] = 0
        school["onvalue"] = 1
        school["variable"] = self.schoolVar

        self.haremVar = IntVar()
        harem=tk.Checkbutton(root)
        harem["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        harem["font"] = ft
        harem["fg"] = "#333333"
        harem["justify"] = "center"
        harem["text"] = "Harem"
        harem.place(x=100,y=440,width=70,height=25)
        harem["offvalue"] = 0
        harem["onvalue"] = 1
        harem["variable"] = self.haremVar

        self.hentaiVar = IntVar()
        hentai=tk.Checkbutton(root)
        hentai["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        hentai["font"] = ft
        hentai["fg"] = "#333333"
        hentai["justify"] = "center"
        hentai["text"] = "Hentai"
        hentai.place(x=100,y=470,width=70,height=25)
        hentai["offvalue"] = 0
        hentai["onvalue"] = 1
        hentai["variable"] = self.hentaiVar

        self.historicalVar = IntVar()
        historical=tk.Checkbutton(root)
        historical["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        historical["font"] = ft
        historical["fg"] = "#333333"
        historical["justify"] = "center"
        historical["text"] = "Historical"
        historical.place(x=100,y=500,width=70,height=25)
        historical["offvalue"] = 0
        historical["onvalue"] = 1
        historical["variable"] = self.historicalVar

        self.horrorVar = IntVar()
        horror=tk.Checkbutton(root)
        horror["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        horror["font"] = ft
        horror["fg"] = "#333333"
        horror["justify"] = "center"
        horror["text"] = "Horror"
        horror.place(x=100,y=530,width=70,height=25)
        horror["offvalue"] = 0
        horror["onvalue"] = 1
        horror["variable"] = self.horrorVar

        self.joseiVar = IntVar()
        josei=tk.Checkbutton(root)
        josei["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        josei["font"] = ft
        josei["fg"] = "#333333"
        josei["justify"] = "center"
        josei["text"] = "Josei"
        josei.place(x=100,y=560,width=70,height=25)
        josei["offvalue"] = 0
        josei["onvalue"] = 1
        josei["variable"] = self.joseiVar

        self.kidsVar = IntVar()
        kids=tk.Checkbutton(root)
        kids["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        kids["font"] = ft
        kids["fg"] = "#333333"
        kids["justify"] = "center"
        kids["text"] = "Kids"
        kids.place(x=210,y=380,width=70,height=25)
        kids["offvalue"] = 0
        kids["onvalue"] = 1
        kids["variable"] = self.kidsVar

        self.demonsVar = IntVar()
        demons=tk.Checkbutton(root)
        demons["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        demons["font"] = ft
        demons["fg"] = "#333333"
        demons["justify"] = "center"
        demons["text"] = "Demons"
        demons.place(x=0,y=530,width=70,height=25)
        demons["offvalue"] = 0
        demons["onvalue"] = 1
        demons["variable"] = self.demonsVar

        self.mechaVar = IntVar()
        mecha=tk.Checkbutton(root)
        mecha["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        mecha["font"] = ft
        mecha["fg"] = "#333333"
        mecha["justify"] = "center"
        mecha["text"] = "Mecha"
        mecha.place(x=210,y=470,width=70,height=25)
        mecha["offvalue"] = 0
        mecha["onvalue"] = 1
        mecha["variable"] = self.mechaVar

        self.militaryVar = IntVar(0)
        military=tk.Checkbutton(root)
        military["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        military["font"] = ft
        military["fg"] = "#333333"
        military["justify"] = "center"
        military["text"] = "Military"
        military.place(x=210,y=500,width=70,height=25)
        military["offvalue"] = 0
        military["onvalue"] = 1
        military["variable"] = self.militaryVar

        self.martialArtsVar = IntVar()
        martialArts=tk.Checkbutton(root)
        martialArts["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=8)
        martialArts["font"] = ft
        martialArts["fg"] = "#333333"
        martialArts["justify"] = "center"
        martialArts["text"] = "Martial Arts"
        martialArts.place(x=210,y=440,width=70,height=25)
        martialArts["offvalue"] = 0
        martialArts["onvalue"] = 1
        martialArts["variable"] = self.martialArtsVar

        self.mysteryVar = IntVar()
        mystery=tk.Checkbutton(root)
        mystery["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        mystery["font"] = ft
        mystery["fg"] = "#333333"
        mystery["justify"] = "center"
        mystery["text"] = "Mystery"
        mystery.place(x=210,y=560,width=70,height=25)
        mystery["offvalue"] = 0
        mystery["onvalue"] = 1
        mystery["variable"] = self.mysteryVar

        self.parodyVar = IntVar()
        parody=tk.Checkbutton(root)
        parody["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        parody["font"] = ft
        parody["fg"] = "#333333"
        parody["justify"] = "center"
        parody["text"] = "Parody"
        parody.place(x=320,y=380,width=70,height=25)
        parody["offvalue"] = 0
        parody["onvalue"] = 1
        parody["variable"] = self.parodyVar

        self.policeVar = IntVar()
        police=tk.Checkbutton(root)
        police["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        police["font"] = ft
        police["fg"] = "#333333"
        police["justify"] = "center"
        police["text"] = "Police"
        police.place(x=320,y=410,width=70,height=25)
        police["offvalue"] = 0
        police["onvalue"] = 1
        police["variable"] = self.policeVar

        self.magicVar = IntVar()
        magic=tk.Checkbutton(root)
        magic["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        magic["font"] = ft
        magic["fg"] = "#333333"
        magic["justify"] = "center"
        magic["text"] = "Magic"
        magic.place(x=210,y=410,width=70,height=25)
        magic["offvalue"] = 0
        magic["onvalue"] = 1
        magic["variable"] = self.magicVar

        self.musicVar = IntVar()
        music=tk.Checkbutton(root)
        music["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        music["font"] = ft
        music["fg"] = "#333333"
        music["justify"] = "center"
        music["text"] = "Music"
        music.place(x=210,y=530,width=70,height=25)
        music["offvalue"] = 0
        music["onvalue"] = 1
        music["variable"] = self.musicVar

        self.seinenVar = IntVar()
        seinen=tk.Checkbutton(root)
        seinen["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        seinen["font"] = ft
        seinen["fg"] = "#333333"
        seinen["justify"] = "center"
        seinen["text"] = "Seinen"
        seinen.place(x=440,y=380,width=70,height=25)
        seinen["offvalue"] = 0
        seinen["onvalue"] = 1
        seinen["variable"] = self.seinenVar

        self.shoujoVar = IntVar()
        shoujo=tk.Checkbutton(root)
        shoujo["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        shoujo["font"] = ft
        shoujo["fg"] = "#333333"
        shoujo["justify"] = "center"
        shoujo["text"] = "Shoujo"
        shoujo.place(x=440,y=410,width=70,height=25)
        shoujo["offvalue"] = 0
        shoujo["onvalue"] = 1
        shoujo["variable"] = self.shoujoVar

        self.shoujoAiVar = IntVar()
        shoujoAi=tk.Checkbutton(root)
        shoujoAi["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        shoujoAi["font"] = ft
        shoujoAi["fg"] = "#333333"
        shoujoAi["justify"] = "center"
        shoujoAi["text"] = "Shoujo-ai"
        shoujoAi.place(x=440,y=440,width=70,height=25)
        shoujoAi["offvalue"] = 0
        shoujoAi["onvalue"] = 1
        shoujoAi["variable"] = self.shoujoAiVar

        self.shounenVar = IntVar()
        shounen=tk.Checkbutton(root)
        shounen["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        shounen["font"] = ft
        shounen["fg"] = "#333333"
        shounen["justify"] = "center"
        shounen["text"] = "Shounen"
        shounen.place(x=440,y=470,width=70,height=25)
        shounen["offvalue"] = 0
        shounen["onvalue"] = 1
        shounen["variable"] = self.shounenVar

        self.shounenAiVar = IntVar()
        shounenAi=tk.Checkbutton(root)
        shounenAi["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=8)
        shounenAi["font"] = ft
        shounenAi["fg"] = "#333333"
        shounenAi["justify"] = "center"
        shounenAi["text"] = "Shounen-ai"
        shounenAi.place(x=440,y=500,width=70,height=25)
        shounenAi["offvalue"] = 0
        shounenAi["onvalue"] = 1
        shounenAi["variable"] = self.shounenAiVar

        self.sliceOfLifeVar = IntVar()
        sliceOfLife=tk.Checkbutton(root)
        sliceOfLife["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=8)
        sliceOfLife["font"] = ft
        sliceOfLife["fg"] = "#333333"
        sliceOfLife["justify"] = "center"
        sliceOfLife["text"] = "Slice of Life"
        sliceOfLife.place(x=440,y=530,width=70,height=25)
        sliceOfLife["offvalue"] = 0
        sliceOfLife["onvalue"] = 1
        sliceOfLife["variable"] = self.sliceOfLifeVar

        self.spaceVar = IntVar()
        space=tk.Checkbutton(root)
        space["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        space["font"] = ft
        space["fg"] = "#333333"
        space["justify"] = "center"
        space["text"] = "Space"
        space.place(x=440,y=560,width=70,height=25)
        space["offvalue"] = 0
        space["onvalue"] = 1
        space["variable"] = self.spaceVar

        self.sportsVar = IntVar()
        sports=tk.Checkbutton(root)
        sports["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        sports["font"] = ft
        sports["fg"] = "#333333"
        sports["justify"] = "center"
        sports["text"] = "Sports"
        sports.place(x=560,y=380,width=70,height=25)
        sports["offvalue"] = 0
        sports["onvalue"] = 1
        sports["variable"] = self.sportsVar

        self.superpowerVar = IntVar()
        superpower=tk.Checkbutton(root)
        superpower["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=8)
        superpower["font"] = ft
        superpower["fg"] = "#333333"
        superpower["justify"] = "center"
        superpower["text"] = "Superpower"
        superpower.place(x=560,y=410,width=70,height=25)
        superpower["offvalue"] = 0
        superpower["onvalue"] = 1
        superpower["variable"] = self.superpowerVar

        self.supernaturalVar = IntVar()
        supernatural=tk.Checkbutton(root)
        supernatural["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=7)
        supernatural["font"] = ft
        supernatural["fg"] = "#333333"
        supernatural["justify"] = "center"
        supernatural["text"] = "Supernatural"
        supernatural.place(x=560,y=440,width=70,height=25)
        supernatural["offvalue"] = 0
        supernatural["onvalue"] = 1
        supernatural["variable"] = self.supernaturalVar

        self.thrillerVar = IntVar()
        thriller=tk.Checkbutton(root)
        thriller["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        thriller["font"] = ft
        thriller["fg"] = "#333333"
        thriller["justify"] = "center"
        thriller["text"] = "Thriller"
        thriller.place(x=560,y=470,width=70,height=25)
        thriller["offvalue"] = 0
        thriller["onvalue"] = 1
        thriller["variable"] = self.thrillerVar

        self.vampireVar = IntVar()
        vampire=tk.Checkbutton(root)
        vampire["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        vampire["font"] = ft
        vampire["fg"] = "#333333"
        vampire["justify"] = "center"
        vampire["text"] = "Vampire"
        vampire.place(x=560,y=500,width=70,height=25)
        vampire["offvalue"] = 0
        vampire["onvalue"] = 1
        vampire["variable"] = self.vampireVar

        self.yaoiVar = IntVar()
        yaoi=tk.Checkbutton(root)
        yaoi["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        yaoi["font"] = ft
        yaoi["fg"] = "#333333"
        yaoi["justify"] = "center"
        yaoi["text"] = "Yaoi"
        yaoi.place(x=560,y=530,width=70,height=25)
        yaoi["offvalue"] = 0
        yaoi["onvalue"] = 1
        yaoi["variable"] = self.yaoiVar

        self.sciFiVar = IntVar()
        sciFi=tk.Checkbutton(root)
        sciFi["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        sciFi["font"] = ft
        sciFi["fg"] = "#333333"
        sciFi["justify"] = "center"
        sciFi["text"] = "Sci-Fi"
        sciFi.place(x=320,y=560,width=70,height=25)
        sciFi["offvalue"] = 0
        sciFi["onvalue"] = 1
        sciFi["variable"] = self.sciFiVar

        self.yuriVar = IntVar()
        yuri=tk.Checkbutton(root)
        yuri["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        yuri["font"] = ft
        yuri["fg"] = "#333333"
        yuri["justify"] = "center"
        yuri["text"] = "Yuri"
        yuri.place(x=560,y=560,width=70,height=25)
        yuri["offvalue"] = 0
        yuri["onvalue"] = 1
        yuri["variable"] = self.yuriVar

        self.dramaVar = IntVar()
        drama=tk.Checkbutton(root)
        drama["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        drama["font"] = ft
        drama["fg"] = "#333333"
        drama["justify"] = "center"
        drama["text"] = "Drama"
        drama.place(x=0,y=560,width=70,height=25)
        drama["offvalue"] = 0
        drama["onvalue"] = 1
        drama["variable"] = self.dramaVar

        searchButton=tk.Button(root)
        searchButton["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        searchButton["font"] = ft
        searchButton["fg"] = "#000000"
        searchButton["justify"] = "center"
        searchButton["text"] = "Search"
        searchButton.place(x=220,y=620,width=183,height=60)
        searchButton["command"] = self.searchButton_command
    #variables
    #list for the checkboxes' vars of genre
        self.genreVarListTTK = [self.actionVar, self.adventureVar, self.carsVar, self.comedyVar, self.dementiaVar, self.demonsVar, self.dramaVar, self.ecchiVar, self.fantasyVar,
        self.gameVar, self.haremVar, self.hentaiVar, self.historicalVar, self.horrorVar, self.joseiVar, self.kidsVar, self.magicVar, self.martialArtsVar, self.mechaVar, 
        self.militaryVar, self.musicVar, self.mysteryVar, self.parodyVar, self.policeVar, self.psychologicalVar, self.romanceVar, self.samuraiVar, self.schoolVar, 
        self.sciFiVar, self.seinenVar, self.shoujoVar, self.shoujoAiVar, self.shounenVar, self.shounenAiVar, self.sliceOfLifeVar, self.spaceVar, self.sportsVar, 
        self.superpowerVar, self.supernaturalVar, self.thrillerVar, self.vampireVar, self.yaoiVar, self.yuriVar]

        self.genreListTTK = [action, adventure, cars, comedy, dementia, demons, drama, ecchi, fantasy, game, harem, hentai, historical, horror, josei, 
        kids, magic, martialArts, mecha, military, music, mystery, parody, police, psychological, romance, samurai, school, sciFi, seinen, shoujo, 
        shoujoAi, shounen, shounenAi, sliceOfLife, space, sports, superpower, supernatural, thriller, vampire, yaoi, yuri]


    
    #functions
    def searchButton_command(self):
        genreList = []
        counter = 0
        #checks if the checkboxes are checked
        for self.genreTTK in self.genreVarListTTK:
            if self.genreTTK.get() == 1:
                genreList.append(self.genreListTTK[counter].cget("text"))
            counter += 1

        #assigns the amount of genres to this var
        genreListNum = len(genreList)

        #turns the list into a string in one var
        genreFinal = ""
        for genre in genreList[:-1]:
            genreFinal = genreFinal + genre + ","
        genreFinal = genreFinal + genreList[genreListNum-1]
        #GENRE USED FOR FILTERING

        #Filter Type first
        animeListCheckType = []
        animeListCheckGenre = []
        animeListCheckEpisode = []
        animeListFinal = []

        if self.typeTTK.get() == "Any":
            animeListCheckType = aniList
        else:
            for sampleType in aniListObjs:
                if  sampleType.getType() == self.typeTTK.get():
                    animeListCheckType.append(sampleType)
        

        if self.epTTK.get() == "Any":
            animeListCheckEpisode = animeListCheckType
        else:
            if self.epTTK.get() == "13 and Below":
                for sampleEpisode in animeListCheckGenre:
                    if sampleEpisode.getEpisode() <= 13:
                        animeListCheckEpisode.append(sampleEpisode)

            if self.epTTK.get() == "14 up to 26":
                for sampleEpisode in animeListCheckGenre:
                    if sampleEpisode.getEpisode() >= 14 and sampleEpisode.getEpisode() <= 26:
                        animeListCheckEpisode.append(sampleEpisode)
            
            if self.epTTK.get() == "27 and up":
                for sampleEpisode in animeListCheckGenre:
                    if sampleEpisode.getEpisode() >= 27:
                        animeListCheckEpisode.append(sampleEpisode)

        for sampleGenre in animeListCheckEpisode:
            if sampleGenre.getGenre() != genreFinal:
                animeListFinal.append(sampleGenre)

        textAcc = ""
        for anime in animeListFinal:
            text = anime.getName(), " ", anime.getType(), " ", anime.getGenre(), " ", anime.getEpisodes(), " ", anime.getRating(), '\n'
            textAcc += text
            
        self.labelRecommendedAnimeVar.set(textAcc)
        



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
