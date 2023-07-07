from tkinter import *
import ttkbootstrap as ttk

class Application:
    def __init__(self, title):
        self.master = ttk.Window(themename='journal')
        self.master.title(title)
        self.master.attributes('-fullscreen', True)

        self.buttons_frame = ttk.Frame(self.master)
        self.title_frame = ttk.Frame(self.master)
        self.main_frame = ttk.Frame(self.master)

        

    def open_discussion(self):
        self.master.destroy()
        self.master = Application('Discussion')

    def open_stats(self):
        self.master.destroy()
        self.master = Application('Statistiques')
        

    def open_settings(self):
        self.master.destroy()
        self.master = Application('Paramètres')

    def open_presentation(self):
        self.master.destroy()
        self.master = Application('Présentation')

    def build_buttons(self):
        ttk.Button(self.buttons_frame, text="Discussion", command=self.open_discussion).pack(side=LEFT)
        ttk.Button(self.buttons_frame, text="Statistiques", command=self.open_stats).pack(side=LEFT)
        ttk.Button(self.buttons_frame, text="Paramètres", command=self.open_settings).pack(side=LEFT)
        ttk.Button(self.buttons_frame, text="Présentation", command=self.open_presentation).pack(side=LEFT)
   
    def run(self):
        self.build_buttons()
        self.buttons_frame.pack(side=TOP)
        self.title_frame.pack(side=TOP)
        self.main_frame.pack(side=TOP, fill = X)#fill=BOTH, expand=True)
        self.master.mainloop()

if __name__ == "__main__":
    app = Application('random')
    app.run()
