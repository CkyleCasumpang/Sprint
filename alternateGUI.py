#from animeClass import anime
#from functions import *
#import listImport
#import init

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
        width=633
        height=706
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.config(bg = '#efecec')
        root.resizable(width=False, height=False)
        
        epNum=ttk.Combobox(root)
        epNum["values"]=["Any", "Below 12", "12 up to 24", "25 and up" ]
        epNum.current(0)
        epNum.place(x=15,y=180,width=90,height=30)

        GLabel_352=tk.Label(root)
        GLabel_352["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=22)
        GLabel_352["font"] = ft
        GLabel_352["fg"] = "#000000"
        GLabel_352["justify"] = "center"
        GLabel_352["text"] = "Episodes"
        GLabel_352.place(x=0,y=140,width=140,height=30)

        GLabel_700=tk.Label(root)
        GLabel_700["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=15)
        GLabel_700["font"] = ft
        GLabel_700["fg"] = "#000000"
        GLabel_700["justify"] = "center"
        GLabel_700["text"] = "Ratings/Rankings"
        GLabel_700.place(x=250,y=140,width=140,height=30)

        GLabel_123=tk.Label(root)
        GLabel_123["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=22)
        GLabel_123["font"] = ft
        GLabel_123["fg"] = "#333333"
        GLabel_123["justify"] = "center"
        GLabel_123["text"] = "Type"
        GLabel_123.place(x=490,y=140,width=140,height=30)


        ratingsTTK=ttk.Combobox(root)
        ratingsTTK["values"]=["No order", "Highest Rated", "Worst Rated"]
        ratingsTTK.current(0)
        ratingsTTK["justify"] = "center"
        ratingsTTK.place(x=275,y=180,width=90,height=30)    

        typeTTK=ttk.Combobox(root)
        typeTTK["values"]=["Any","Movie", "TV", "OVA", "Special", "Music", "ONA"]
        typeTTK.current(0)
        typeTTK["justify"] = "center"
        typeTTK.place(x=520,y=180,width=90,height=30) 


        GLabel_378=tk.Label(root)
        GLabel_378["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=98)
        GLabel_378["font"] = ft
        GLabel_378["fg"] = "#333333"
        GLabel_378["justify"] = "center"
        GLabel_378["text"] = "AniSearch"
        GLabel_378.place(x=0,y=0,width=632,height=115)

        GLabel_76=tk.Label(root)
        GLabel_76["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=22)
        GLabel_76["font"] = ft
        GLabel_76["fg"] = "#333333"
        GLabel_76["justify"] = "center"
        GLabel_76["text"] = "Genre"
        GLabel_76.place(x=0,y=340,width=630,height=30)

        GCheckBox_364=tk.Checkbutton(root)
        GCheckBox_364["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_364["font"] = ft
        GCheckBox_364["fg"] = "#333333"
        GCheckBox_364["justify"] = "center"
        GCheckBox_364["text"] = "Action"
        GCheckBox_364.place(x=0,y=380,width=70,height=25)
        GCheckBox_364["offvalue"] = "0"
        GCheckBox_364["onvalue"] = "1"

        GCheckBox_238=tk.Checkbutton(root)
        GCheckBox_238["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_238["font"] = ft
        GCheckBox_238["fg"] = "#333333"
        GCheckBox_238["justify"] = "center"
        GCheckBox_238["text"] = "Adventure"
        GCheckBox_238.place(x=0,y=410,width=70,height=25)
        GCheckBox_238["offvalue"] = "0"
        GCheckBox_238["onvalue"] = "1"

        GCheckBox_672=tk.Checkbutton(root)
        GCheckBox_672["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_672["font"] = ft
        GCheckBox_672["fg"] = "#333333"
        GCheckBox_672["justify"] = "center"
        GCheckBox_672["text"] = "Cars"
        GCheckBox_672.place(x=0,y=440,width=70,height=25)
        GCheckBox_672["offvalue"] = "0"
        GCheckBox_672["onvalue"] = "1"

        GCheckBox_104=tk.Checkbutton(root)
        GCheckBox_104["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_104["font"] = ft
        GCheckBox_104["fg"] = "#333333"
        GCheckBox_104["justify"] = "center"
        GCheckBox_104["text"] = "Comedy"
        GCheckBox_104.place(x=0,y=470,width=70,height=25)
        GCheckBox_104["offvalue"] = "0"
        GCheckBox_104["onvalue"] = "1"

        GCheckBox_6=tk.Checkbutton(root)
        GCheckBox_6["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_6["font"] = ft
        GCheckBox_6["fg"] = "#333333"
        GCheckBox_6["justify"] = "center"
        GCheckBox_6["text"] = "Dementia"
        GCheckBox_6.place(x=0,y=500,width=70,height=25)
        GCheckBox_6["offvalue"] = "0"
        GCheckBox_6["onvalue"] = "1"

        GCheckBox_800=tk.Checkbutton(root)
        GCheckBox_800["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_800["font"] = ft
        GCheckBox_800["fg"] = "#333333"
        GCheckBox_800["justify"] = "center"
        GCheckBox_800["text"] = "Ecchi"
        GCheckBox_800.place(x=0,y=590,width=70,height=25)
        GCheckBox_800["offvalue"] = "0"
        GCheckBox_800["onvalue"] = "1"

        GCheckBox_84=tk.Checkbutton(root)
        GCheckBox_84["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_84["font"] = ft
        GCheckBox_84["fg"] = "#333333"
        GCheckBox_84["justify"] = "center"
        GCheckBox_84["text"] = "Fantasy"
        GCheckBox_84.place(x=100,y=380,width=70,height=25)
        GCheckBox_84["offvalue"] = "0"
        GCheckBox_84["onvalue"] = "1"

        GCheckBox_46=tk.Checkbutton(root)
        GCheckBox_46["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_46["font"] = ft
        GCheckBox_46["fg"] = "#333333"
        GCheckBox_46["justify"] = "center"
        GCheckBox_46["text"] = "Game"
        GCheckBox_46.place(x=100,y=410,width=70,height=25)
        GCheckBox_46["offvalue"] = "0"
        GCheckBox_46["onvalue"] = "1"

        GCheckBox_988=tk.Checkbutton(root)
        GCheckBox_988["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=7)
        GCheckBox_988["font"] = ft
        GCheckBox_988["fg"] = "#333333"
        GCheckBox_988["justify"] = "center"
        GCheckBox_988["text"] = "Psychological"
        GCheckBox_988.place(x=320,y=440,width=70,height=25)
        GCheckBox_988["offvalue"] = "0"
        GCheckBox_988["onvalue"] = "1"

        GCheckBox_388=tk.Checkbutton(root)
        GCheckBox_388["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_388["font"] = ft
        GCheckBox_388["fg"] = "#333333"
        GCheckBox_388["justify"] = "center"
        GCheckBox_388["text"] = "Romance"
        GCheckBox_388.place(x=320,y=470,width=70,height=25)
        GCheckBox_388["offvalue"] = "0"
        GCheckBox_388["onvalue"] = "1"

        GCheckBox_957=tk.Checkbutton(root)
        GCheckBox_957["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_957["font"] = ft
        GCheckBox_957["fg"] = "#333333"
        GCheckBox_957["justify"] = "center"
        GCheckBox_957["text"] = "Samurai"
        GCheckBox_957.place(x=320,y=500,width=70,height=25)
        GCheckBox_957["offvalue"] = "0"
        GCheckBox_957["onvalue"] = "1"

        GCheckBox_581=tk.Checkbutton(root)
        GCheckBox_581["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_581["font"] = ft
        GCheckBox_581["fg"] = "#333333"
        GCheckBox_581["justify"] = "center"
        GCheckBox_581["text"] = "School"
        GCheckBox_581.place(x=320,y=530,width=70,height=25)
        GCheckBox_581["offvalue"] = "0"
        GCheckBox_581["onvalue"] = "1"

        GCheckBox_158=tk.Checkbutton(root)
        GCheckBox_158["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_158["font"] = ft
        GCheckBox_158["fg"] = "#333333"
        GCheckBox_158["justify"] = "center"
        GCheckBox_158["text"] = "Harem"
        GCheckBox_158.place(x=100,y=440,width=70,height=25)
        GCheckBox_158["offvalue"] = "0"
        GCheckBox_158["onvalue"] = "1"

        GCheckBox_314=tk.Checkbutton(root)
        GCheckBox_314["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_314["font"] = ft
        GCheckBox_314["fg"] = "#333333"
        GCheckBox_314["justify"] = "center"
        GCheckBox_314["text"] = "Hentai"
        GCheckBox_314.place(x=100,y=470,width=70,height=25)
        GCheckBox_314["offvalue"] = "0"
        GCheckBox_314["onvalue"] = "1"

        GCheckBox_827=tk.Checkbutton(root)
        GCheckBox_827["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_827["font"] = ft
        GCheckBox_827["fg"] = "#333333"
        GCheckBox_827["justify"] = "center"
        GCheckBox_827["text"] = "Historical"
        GCheckBox_827.place(x=100,y=500,width=70,height=25)
        GCheckBox_827["offvalue"] = "0"
        GCheckBox_827["onvalue"] = "1"

        GCheckBox_999=tk.Checkbutton(root)
        GCheckBox_999["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_999["font"] = ft
        GCheckBox_999["fg"] = "#333333"
        GCheckBox_999["justify"] = "center"
        GCheckBox_999["text"] = "Horror"
        GCheckBox_999.place(x=100,y=530,width=70,height=25)
        GCheckBox_999["offvalue"] = "0"
        GCheckBox_999["onvalue"] = "1"

        GCheckBox_152=tk.Checkbutton(root)
        GCheckBox_152["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_152["font"] = ft
        GCheckBox_152["fg"] = "#333333"
        GCheckBox_152["justify"] = "center"
        GCheckBox_152["text"] = "Josei"
        GCheckBox_152.place(x=100,y=560,width=70,height=25)
        GCheckBox_152["offvalue"] = "0"
        GCheckBox_152["onvalue"] = "1"

        GCheckBox_551=tk.Checkbutton(root)
        GCheckBox_551["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_551["font"] = ft
        GCheckBox_551["fg"] = "#333333"
        GCheckBox_551["justify"] = "center"
        GCheckBox_551["text"] = "Kids"
        GCheckBox_551.place(x=210,y=380,width=70,height=25)
        GCheckBox_551["offvalue"] = "0"
        GCheckBox_551["onvalue"] = "1"

        GCheckBox_584=tk.Checkbutton(root)
        GCheckBox_584["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_584["font"] = ft
        GCheckBox_584["fg"] = "#333333"
        GCheckBox_584["justify"] = "center"
        GCheckBox_584["text"] = "Demons"
        GCheckBox_584.place(x=0,y=530,width=70,height=25)
        GCheckBox_584["offvalue"] = "0"
        GCheckBox_584["onvalue"] = "1"

        GCheckBox_147=tk.Checkbutton(root)
        GCheckBox_147["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_147["font"] = ft
        GCheckBox_147["fg"] = "#333333"
        GCheckBox_147["justify"] = "center"
        GCheckBox_147["text"] = "Mecha"
        GCheckBox_147.place(x=210,y=470,width=70,height=25)
        GCheckBox_147["offvalue"] = "0"
        GCheckBox_147["onvalue"] = "1"

        GCheckBox_61=tk.Checkbutton(root)
        GCheckBox_61["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_61["font"] = ft
        GCheckBox_61["fg"] = "#333333"
        GCheckBox_61["justify"] = "center"
        GCheckBox_61["text"] = "Military"
        GCheckBox_61.place(x=210,y=500,width=70,height=25)
        GCheckBox_61["offvalue"] = "0"
        GCheckBox_61["onvalue"] = "1"

        GCheckBox_861=tk.Checkbutton(root)
        GCheckBox_861["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=8)
        GCheckBox_861["font"] = ft
        GCheckBox_861["fg"] = "#333333"
        GCheckBox_861["justify"] = "center"
        GCheckBox_861["text"] = "Martial Arts"
        GCheckBox_861.place(x=210,y=440,width=70,height=25)
        GCheckBox_861["offvalue"] = "0"
        GCheckBox_861["onvalue"] = "1"

        GCheckBox_820=tk.Checkbutton(root)
        GCheckBox_820["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_820["font"] = ft
        GCheckBox_820["fg"] = "#333333"
        GCheckBox_820["justify"] = "center"
        GCheckBox_820["text"] = "Mystery"
        GCheckBox_820.place(x=210,y=560,width=70,height=25)
        GCheckBox_820["offvalue"] = "0"
        GCheckBox_820["onvalue"] = "1"

        GCheckBox_849=tk.Checkbutton(root)
        GCheckBox_849["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_849["font"] = ft
        GCheckBox_849["fg"] = "#333333"
        GCheckBox_849["justify"] = "center"
        GCheckBox_849["text"] = "Parody"
        GCheckBox_849.place(x=320,y=380,width=70,height=25)
        GCheckBox_849["offvalue"] = "0"
        GCheckBox_849["onvalue"] = "1"

        GCheckBox_899=tk.Checkbutton(root)
        GCheckBox_899["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_899["font"] = ft
        GCheckBox_899["fg"] = "#333333"
        GCheckBox_899["justify"] = "center"
        GCheckBox_899["text"] = "Police"
        GCheckBox_899.place(x=320,y=410,width=70,height=25)
        GCheckBox_899["offvalue"] = "0"
        GCheckBox_899["onvalue"] = "1"

        GCheckBox_498=tk.Checkbutton(root)
        GCheckBox_498["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_498["font"] = ft
        GCheckBox_498["fg"] = "#333333"
        GCheckBox_498["justify"] = "center"
        GCheckBox_498["text"] = "Magic"
        GCheckBox_498.place(x=210,y=410,width=70,height=25)
        GCheckBox_498["offvalue"] = "0"
        GCheckBox_498["onvalue"] = "1"

        GCheckBox_329=tk.Checkbutton(root)
        GCheckBox_329["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_329["font"] = ft
        GCheckBox_329["fg"] = "#333333"
        GCheckBox_329["justify"] = "center"
        GCheckBox_329["text"] = "Music"
        GCheckBox_329.place(x=210,y=530,width=70,height=25)
        GCheckBox_329["offvalue"] = "0"
        GCheckBox_329["onvalue"] = "1"

        GCheckBox_93=tk.Checkbutton(root)
        GCheckBox_93["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_93["font"] = ft
        GCheckBox_93["fg"] = "#333333"
        GCheckBox_93["justify"] = "center"
        GCheckBox_93["text"] = "Seinen"
        GCheckBox_93.place(x=440,y=380,width=70,height=25)
        GCheckBox_93["offvalue"] = "0"
        GCheckBox_93["onvalue"] = "1"

        GCheckBox_357=tk.Checkbutton(root)
        GCheckBox_357["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_357["font"] = ft
        GCheckBox_357["fg"] = "#333333"
        GCheckBox_357["justify"] = "center"
        GCheckBox_357["text"] = "Shoujo"
        GCheckBox_357.place(x=440,y=410,width=70,height=25)
        GCheckBox_357["offvalue"] = "0"
        GCheckBox_357["onvalue"] = "1"

        GCheckBox_630=tk.Checkbutton(root)
        GCheckBox_630["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_630["font"] = ft
        GCheckBox_630["fg"] = "#333333"
        GCheckBox_630["justify"] = "center"
        GCheckBox_630["text"] = "Shoujo-ai"
        GCheckBox_630.place(x=440,y=440,width=70,height=25)
        GCheckBox_630["offvalue"] = "0"
        GCheckBox_630["onvalue"] = "1"

        GCheckBox_774=tk.Checkbutton(root)
        GCheckBox_774["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_774["font"] = ft
        GCheckBox_774["fg"] = "#333333"
        GCheckBox_774["justify"] = "center"
        GCheckBox_774["text"] = "Shounen"
        GCheckBox_774.place(x=440,y=470,width=70,height=25)
        GCheckBox_774["offvalue"] = "0"
        GCheckBox_774["onvalue"] = "1"

        GCheckBox_567=tk.Checkbutton(root)
        GCheckBox_567["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=8)
        GCheckBox_567["font"] = ft
        GCheckBox_567["fg"] = "#333333"
        GCheckBox_567["justify"] = "center"
        GCheckBox_567["text"] = "Shounen-ai"
        GCheckBox_567.place(x=440,y=500,width=70,height=25)
        GCheckBox_567["offvalue"] = "0"
        GCheckBox_567["onvalue"] = "1"

        GCheckBox_574=tk.Checkbutton(root)
        GCheckBox_574["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=8)
        GCheckBox_574["font"] = ft
        GCheckBox_574["fg"] = "#333333"
        GCheckBox_574["justify"] = "center"
        GCheckBox_574["text"] = "Slice of Life"
        GCheckBox_574.place(x=440,y=530,width=70,height=25)
        GCheckBox_574["offvalue"] = "0"
        GCheckBox_574["onvalue"] = "1"

        GCheckBox_859=tk.Checkbutton(root)
        GCheckBox_859["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_859["font"] = ft
        GCheckBox_859["fg"] = "#333333"
        GCheckBox_859["justify"] = "center"
        GCheckBox_859["text"] = "Space"
        GCheckBox_859.place(x=440,y=560,width=70,height=25)
        GCheckBox_859["offvalue"] = "0"
        GCheckBox_859["onvalue"] = "1"

        GCheckBox_752=tk.Checkbutton(root)
        GCheckBox_752["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_752["font"] = ft
        GCheckBox_752["fg"] = "#333333"
        GCheckBox_752["justify"] = "center"
        GCheckBox_752["text"] = "Sports"
        GCheckBox_752.place(x=560,y=380,width=70,height=25)
        GCheckBox_752["offvalue"] = "0"
        GCheckBox_752["onvalue"] = "1"

        GCheckBox_287=tk.Checkbutton(root)
        GCheckBox_287["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=8)
        GCheckBox_287["font"] = ft
        GCheckBox_287["fg"] = "#333333"
        GCheckBox_287["justify"] = "center"
        GCheckBox_287["text"] = "Superpower"
        GCheckBox_287.place(x=560,y=410,width=70,height=25)
        GCheckBox_287["offvalue"] = "0"
        GCheckBox_287["onvalue"] = "1"

        GCheckBox_283=tk.Checkbutton(root)
        GCheckBox_283["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=7)
        GCheckBox_283["font"] = ft
        GCheckBox_283["fg"] = "#333333"
        GCheckBox_283["justify"] = "center"
        GCheckBox_283["text"] = "Supernatural"
        GCheckBox_283.place(x=560,y=440,width=70,height=25)
        GCheckBox_283["offvalue"] = "0"
        GCheckBox_283["onvalue"] = "1"

        GCheckBox_918=tk.Checkbutton(root)
        GCheckBox_918["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_918["font"] = ft
        GCheckBox_918["fg"] = "#333333"
        GCheckBox_918["justify"] = "center"
        GCheckBox_918["text"] = "Thriller"
        GCheckBox_918.place(x=560,y=470,width=70,height=25)
        GCheckBox_918["offvalue"] = "0"
        GCheckBox_918["onvalue"] = "1"

        GCheckBox_912=tk.Checkbutton(root)
        GCheckBox_912["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_912["font"] = ft
        GCheckBox_912["fg"] = "#333333"
        GCheckBox_912["justify"] = "center"
        GCheckBox_912["text"] = "Vampire"
        GCheckBox_912.place(x=560,y=500,width=70,height=25)
        GCheckBox_912["offvalue"] = "0"
        GCheckBox_912["onvalue"] = "1"

        GCheckBox_801=tk.Checkbutton(root)
        GCheckBox_801["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_801["font"] = ft
        GCheckBox_801["fg"] = "#333333"
        GCheckBox_801["justify"] = "center"
        GCheckBox_801["text"] = "Yaoi"
        GCheckBox_801.place(x=560,y=530,width=70,height=25)
        GCheckBox_801["offvalue"] = "0"
        GCheckBox_801["onvalue"] = "1"

        GCheckBox_343=tk.Checkbutton(root)
        GCheckBox_343["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_343["font"] = ft
        GCheckBox_343["fg"] = "#333333"
        GCheckBox_343["justify"] = "center"
        GCheckBox_343["text"] = "Sci-Fi"
        GCheckBox_343.place(x=320,y=560,width=70,height=25)
        GCheckBox_343["offvalue"] = "0"
        GCheckBox_343["onvalue"] = "1"

        GCheckBox_127=tk.Checkbutton(root)
        GCheckBox_127["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_127["font"] = ft
        GCheckBox_127["fg"] = "#333333"
        GCheckBox_127["justify"] = "center"
        GCheckBox_127["text"] = "Yuri"
        GCheckBox_127.place(x=560,y=560,width=70,height=25)
        GCheckBox_127["offvalue"] = "0"
        GCheckBox_127["onvalue"] = "1"

        GCheckBox_967=tk.Checkbutton(root)
        GCheckBox_967["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_967["font"] = ft
        GCheckBox_967["fg"] = "#333333"
        GCheckBox_967["justify"] = "center"
        GCheckBox_967["text"] = "Drama"
        GCheckBox_967.place(x=0,y=560,width=70,height=25)
        GCheckBox_967["offvalue"] = "0"
        GCheckBox_967["onvalue"] = "1"

        GButton_473=tk.Button(root)
        GButton_473["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GButton_473["font"] = ft
        GButton_473["fg"] = "#000000"
        GButton_473["justify"] = "center"
        GButton_473["text"] = "Search"
        GButton_473.place(x=220,y=620,width=183,height=60)
        GButton_473["command"] = self.GButton_473_command

    def GButton_473_command(self):
        print("test")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
