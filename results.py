import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=623
        height=764
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_191=tk.Label(root)
        GLabel_191["bg"] = "#e38383"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_191["font"] = ft
        GLabel_191["fg"] = "#333333"
        GLabel_191["justify"] = "center"
        GLabel_191["text"] = ""
        GLabel_191.place(x=0,y=0,width=602,height=761)

        GLabel_829=tk.Label(root)
        GLabel_829["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=73)
        GLabel_829["font"] = ft
        GLabel_829["fg"] = "#000000"
        GLabel_829["justify"] = "center"
        GLabel_829["text"] = "Results:"
        GLabel_829.place(x=0,y=0,width=602,height=113)

        GLabel_184=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_184["font"] = ft
        GLabel_184["fg"] = "#333333"
        GLabel_184["justify"] = "center"
        GLabel_184["text"] = "Results are here"
        GLabel_184.place(x=0,y=130,width=602,height=126)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
