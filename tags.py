import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("")
        #setting window size
        width=633
        height=706
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_720=tk.Label(root)
        GLabel_720["bg"] = "#efecec"
        ft = tkFont.Font(family='Times',size=98)
        GLabel_720["font"] = ft
        GLabel_720["fg"] = "#000000"
        GLabel_720["justify"] = "center"
        GLabel_720["text"] = ""
        GLabel_720["relief"] = "groove"
        GLabel_720.place(x=0,y=0,width=632,height=709)

        GRadio_262=tk.Radiobutton(root)
        GRadio_262["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_262["font"] = ft
        GRadio_262["fg"] = "#030303"
        GRadio_262["justify"] = "center"
        GRadio_262["text"] = "Below 12"
        GRadio_262.place(x=0,y=180,width=90,height=30)
        GRadio_262["command"] = self.GRadio_262_command

        GRadio_218=tk.Radiobutton(root)
        GRadio_218["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_218["font"] = ft
        GRadio_218["fg"] = "#000000"
        GRadio_218["justify"] = "center"
        GRadio_218["text"] = "12 up to 24"
        GRadio_218.place(x=0,y=220,width=90,height=30)
        GRadio_218["command"] = self.GRadio_218_command

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

        GRadio_956=tk.Radiobutton(root)
        GRadio_956["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_956["font"] = ft
        GRadio_956["fg"] = "#333333"
        GRadio_956["justify"] = "center"
        GRadio_956["text"] = "All Anime"
        GRadio_956.place(x=180,y=190,width=85,height=25)
        GRadio_956["command"] = self.GRadio_956_command

        GRadio_952=tk.Radiobutton(root)
        GRadio_952["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_952["font"] = ft
        GRadio_952["fg"] = "#333333"
        GRadio_952["justify"] = "center"
        GRadio_952["text"] = "Top Airing"
        GRadio_952.place(x=180,y=220,width=85,height=25)
        GRadio_952["command"] = self.GRadio_952_command

        GRadio_584=tk.Radiobutton(root)
        GRadio_584["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=8)
        GRadio_584["font"] = ft
        GRadio_584["fg"] = "#333333"
        GRadio_584["justify"] = "center"
        GRadio_584["text"] = "Top Upcoming"
        GRadio_584.place(x=180,y=250,width=85,height=25)
        GRadio_584["command"] = self.GRadio_584_command

        GRadio_394=tk.Radiobutton(root)
        GRadio_394["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=9)
        GRadio_394["font"] = ft
        GRadio_394["fg"] = "#333333"
        GRadio_394["justify"] = "center"
        GRadio_394["text"] = "Top TV Series"
        GRadio_394.place(x=280,y=190,width=85,height=25)
        GRadio_394["command"] = self.GRadio_394_command

        GRadio_938=tk.Radiobutton(root)
        GRadio_938["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_938["font"] = ft
        GRadio_938["fg"] = "#333333"
        GRadio_938["justify"] = "center"
        GRadio_938["text"] = "Top Movies"
        GRadio_938.place(x=280,y=220,width=85,height=25)
        GRadio_938["command"] = self.GRadio_938_command

        GRadio_600=tk.Radiobutton(root)
        GRadio_600["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_600["font"] = ft
        GRadio_600["fg"] = "#333333"
        GRadio_600["justify"] = "center"
        GRadio_600["text"] = "25 and up"
        GRadio_600.place(x=0,y=260,width=90,height=30)
        GRadio_600["command"] = self.GRadio_600_command

        GRadio_51=tk.Radiobutton(root)
        GRadio_51["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_51["font"] = ft
        GRadio_51["fg"] = "#333333"
        GRadio_51["justify"] = "center"
        GRadio_51["text"] = "Top OVAs"
        GRadio_51.place(x=280,y=250,width=85,height=25)
        GRadio_51["command"] = self.GRadio_51_command

        GRadio_307=tk.Radiobutton(root)
        GRadio_307["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_307["font"] = ft
        GRadio_307["fg"] = "#333333"
        GRadio_307["justify"] = "center"
        GRadio_307["text"] = "Top ONAs"
        GRadio_307.place(x=380,y=190,width=85,height=25)
        GRadio_307["command"] = self.GRadio_307_command

        GRadio_159=tk.Radiobutton(root)
        GRadio_159["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_159["font"] = ft
        GRadio_159["fg"] = "#333333"
        GRadio_159["justify"] = "center"
        GRadio_159["text"] = "Top Special"
        GRadio_159.place(x=380,y=220,width=85,height=25)
        GRadio_159["command"] = self.GRadio_159_command

        GRadio_41=tk.Radiobutton(root)
        GRadio_41["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=9)
        GRadio_41["font"] = ft
        GRadio_41["fg"] = "#333333"
        GRadio_41["justify"] = "center"
        GRadio_41["text"] = "Most Popular"
        GRadio_41.place(x=380,y=250,width=85,height=25)
        GRadio_41["command"] = self.GRadio_41_command

        GCheckBox_955=tk.Checkbutton(root)
        GCheckBox_955["anchor"] = "center"
        GCheckBox_955["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_955["font"] = ft
        GCheckBox_955["fg"] = "#333333"
        GCheckBox_955["justify"] = "center"
        GCheckBox_955["text"] = "TV"
        GCheckBox_955.place(x=550,y=180,width=80,height=30)
        GCheckBox_955["offvalue"] = "0"
        GCheckBox_955["onvalue"] = "1"
        GCheckBox_955["command"] = self.GCheckBox_955_command

        GCheckBox_848=tk.Checkbutton(root)
        GCheckBox_848["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_848["font"] = ft
        GCheckBox_848["fg"] = "#333333"
        GCheckBox_848["justify"] = "center"
        GCheckBox_848["text"] = "Others"
        GCheckBox_848.place(x=550,y=300,width=80,height=30)
        GCheckBox_848["offvalue"] = "0"
        GCheckBox_848["onvalue"] = "1"
        GCheckBox_848["command"] = self.GCheckBox_848_command

        GCheckBox_962=tk.Checkbutton(root)
        GCheckBox_962["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_962["font"] = ft
        GCheckBox_962["fg"] = "#333333"
        GCheckBox_962["justify"] = "center"
        GCheckBox_962["text"] = "Movie"
        GCheckBox_962.place(x=550,y=220,width=80,height=30)
        GCheckBox_962["offvalue"] = "0"
        GCheckBox_962["onvalue"] = "1"
        GCheckBox_962["command"] = self.GCheckBox_962_command

        GCheckBox_429=tk.Checkbutton(root)
        GCheckBox_429["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_429["font"] = ft
        GCheckBox_429["fg"] = "#333333"
        GCheckBox_429["justify"] = "center"
        GCheckBox_429["text"] = "OVA"
        GCheckBox_429.place(x=550,y=260,width=80,height=30)
        GCheckBox_429["offvalue"] = "0"
        GCheckBox_429["onvalue"] = "1"
        GCheckBox_429["command"] = self.GCheckBox_429_command

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
        GCheckBox_364["command"] = self.GCheckBox_364_command

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
        GCheckBox_238["command"] = self.GCheckBox_238_command

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
        GCheckBox_672["command"] = self.GCheckBox_672_command

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
        GCheckBox_104["command"] = self.GCheckBox_104_command

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
        GCheckBox_6["command"] = self.GCheckBox_6_command

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
        GCheckBox_800["command"] = self.GCheckBox_800_command

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
        GCheckBox_84["command"] = self.GCheckBox_84_command

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
        GCheckBox_46["command"] = self.GCheckBox_46_command

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
        GCheckBox_988["command"] = self.GCheckBox_988_command

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
        GCheckBox_388["command"] = self.GCheckBox_388_command

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
        GCheckBox_957["command"] = self.GCheckBox_957_command

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
        GCheckBox_581["command"] = self.GCheckBox_581_command

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
        GCheckBox_158["command"] = self.GCheckBox_158_command

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
        GCheckBox_314["command"] = self.GCheckBox_314_command

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
        GCheckBox_827["command"] = self.GCheckBox_827_command

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
        GCheckBox_999["command"] = self.GCheckBox_999_command

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
        GCheckBox_152["command"] = self.GCheckBox_152_command

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
        GCheckBox_551["command"] = self.GCheckBox_551_command

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
        GCheckBox_584["command"] = self.GCheckBox_584_command

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
        GCheckBox_147["command"] = self.GCheckBox_147_command

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
        GCheckBox_61["command"] = self.GCheckBox_61_command

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
        GCheckBox_861["command"] = self.GCheckBox_861_command

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
        GCheckBox_820["command"] = self.GCheckBox_820_command

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
        GCheckBox_849["command"] = self.GCheckBox_849_command

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
        GCheckBox_899["command"] = self.GCheckBox_899_command

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
        GCheckBox_498["command"] = self.GCheckBox_498_command

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
        GCheckBox_329["command"] = self.GCheckBox_329_command

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
        GCheckBox_93["command"] = self.GCheckBox_93_command

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
        GCheckBox_357["command"] = self.GCheckBox_357_command

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
        GCheckBox_630["command"] = self.GCheckBox_630_command

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
        GCheckBox_774["command"] = self.GCheckBox_774_command

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
        GCheckBox_567["command"] = self.GCheckBox_567_command

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
        GCheckBox_574["command"] = self.GCheckBox_574_command

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
        GCheckBox_859["command"] = self.GCheckBox_859_command

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
        GCheckBox_752["command"] = self.GCheckBox_752_command

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
        GCheckBox_287["command"] = self.GCheckBox_287_command

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
        GCheckBox_283["command"] = self.GCheckBox_283_command

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
        GCheckBox_918["command"] = self.GCheckBox_918_command

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
        GCheckBox_912["command"] = self.GCheckBox_912_command

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
        GCheckBox_801["command"] = self.GCheckBox_801_command

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
        GCheckBox_343["command"] = self.GCheckBox_343_command

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
        GCheckBox_127["command"] = self.GCheckBox_127_command

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
        GCheckBox_967["command"] = self.GCheckBox_967_command

        GButton_473=tk.Button(root)
        GButton_473["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GButton_473["font"] = ft
        GButton_473["fg"] = "#000000"
        GButton_473["justify"] = "center"
        GButton_473["text"] = "Search"
        GButton_473.place(x=220,y=620,width=183,height=60)
        GButton_473["command"] = self.GButton_473_command

    def GRadio_262_command(self):
        print("command")


    def GRadio_218_command(self):
        print("command")


    def GRadio_956_command(self):
        print("command")


    def GRadio_952_command(self):
        print("command")


    def GRadio_584_command(self):
        print("command")


    def GRadio_394_command(self):
        print("command")


    def GRadio_938_command(self):
        print("command")


    def GRadio_600_command(self):
        print("command")


    def GRadio_51_command(self):
        print("command")


    def GRadio_307_command(self):
        print("command")


    def GRadio_159_command(self):
        print("command")


    def GRadio_41_command(self):
        print("command")


    def GCheckBox_955_command(self):
        print("command")


    def GCheckBox_848_command(self):
        print("command")


    def GCheckBox_962_command(self):
        print("command")


    def GCheckBox_429_command(self):
        print("command")


    def GCheckBox_364_command(self):
        print("command")


    def GCheckBox_238_command(self):
        print("command")


    def GCheckBox_672_command(self):
        print("command")


    def GCheckBox_104_command(self):
        print("command")


    def GCheckBox_6_command(self):
        print("command")


    def GCheckBox_800_command(self):
        print("command")


    def GCheckBox_84_command(self):
        print("command")


    def GCheckBox_46_command(self):
        print("command")


    def GCheckBox_988_command(self):
        print("command")


    def GCheckBox_388_command(self):
        print("command")


    def GCheckBox_957_command(self):
        print("command")


    def GCheckBox_581_command(self):
        print("command")


    def GCheckBox_158_command(self):
        print("command")


    def GCheckBox_314_command(self):
        print("command")


    def GCheckBox_827_command(self):
        print("command")


    def GCheckBox_999_command(self):
        print("command")


    def GCheckBox_152_command(self):
        print("command")


    def GCheckBox_551_command(self):
        print("command")


    def GCheckBox_584_command(self):
        print("command")


    def GCheckBox_147_command(self):
        print("command")


    def GCheckBox_61_command(self):
        print("command")


    def GCheckBox_861_command(self):
        print("command")


    def GCheckBox_820_command(self):
        print("command")


    def GCheckBox_849_command(self):
        print("command")


    def GCheckBox_899_command(self):
        print("command")


    def GCheckBox_498_command(self):
        print("command")


    def GCheckBox_329_command(self):
        print("command")


    def GCheckBox_93_command(self):
        print("command")


    def GCheckBox_357_command(self):
        print("command")


    def GCheckBox_630_command(self):
        print("command")


    def GCheckBox_774_command(self):
        print("command")


    def GCheckBox_567_command(self):
        print("command")


    def GCheckBox_574_command(self):
        print("command")


    def GCheckBox_859_command(self):
        print("command")


    def GCheckBox_752_command(self):
        print("command")


    def GCheckBox_287_command(self):
        print("command")


    def GCheckBox_283_command(self):
        print("command")


    def GCheckBox_918_command(self):
        print("command")


    def GCheckBox_912_command(self):
        print("command")


    def GCheckBox_801_command(self):
        print("command")


    def GCheckBox_343_command(self):
        print("command")


    def GCheckBox_127_command(self):
        print("command")


    def GCheckBox_967_command(self):
        print("command")


    def GButton_473_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
