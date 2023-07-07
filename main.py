from tkinter import *
import ttkbootstrap as ttk


#Création de la fenêtre d'accueil
master = ttk.Window(themename= 'darkly')

#Personnaliser la fenêtre
master.title('Main page')
master.minsize(720,480)
#master.iconbitmap("images/logo_icon.ico")


#Définition des fonctions qui amènent aux différentes pages
def open_discussion():
    with open("discussion.py", "r") as file:
        code = file.read()
        exec(code)

def open_stats():
    with open("stats.py", "r") as file:
        code = file.read()
        exec(code)

def open_settings():
    with open("settings.py", "r") as file:
        code = file.read()
        exec(code)

def open_presentation():
    with open("presentation.py", "r") as file:
        code = file.read()
        exec(code)

#Création du header, donc de la frame
frame=ttk.Frame(master)

label_title = ttk.Label(frame, text="Template Header", font="Helvetica 25")
label_title.pack(pady=10)

#Ajout des boutons amenant aux différentes pages
discussion_button= ttk.Button(frame, text="Discussion", command=open_discussion)
discussion_button.pack(side='left', pady=30)

statistic_button=ttk.Button(frame, text="Stats", command=open_stats)
statistic_button.pack(side='left', pady=30)

settings_button=ttk.Button(frame, text="Settings", command=open_settings)
settings_button.pack(side='left', pady=30)

presentation_button=ttk.Button(frame, text="Presentation", command=open_presentation)
presentation_button.pack(side='left', pady=30)
frame.pack(side=TOP)

label_subtitle = ttk.Label(master, text="Template header to help the user figure out how the interface is looking", font="Helvetica 12")
label_subtitle.pack(side=TOP, pady=50)

#Afficher la fenêtre
master.mainloop()

if __name__ == "__main__":
    print("main")