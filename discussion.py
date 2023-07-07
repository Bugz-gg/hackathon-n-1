from tkinter import *

#Création de la fenêtre d'accueil
master = Tk()

#Personnaliser la fenêtre
master.title('Main page')
master.minsize(720,480)
master.iconbitmap("images/logo_icon.ico")
master.config(background='#41B77F')

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
frame=Frame(master, bg='#41B77F')
frame.pack(side=TOP)

#Ajout de texte (penser à mettre le même fond que la fenêtre pour ne pas voir le rectangle)
#Catégories Discussion, Statistiques, Réglages, Présentation
label_title = Label(frame, text="Discussion", font=("Helvetica", 40), bg='#41B77F', fg='black')
label_title.pack()

label_subtitle = Label(master, text="Discussion page with the robot", font=("Helvetica", 20), bg='#41B77F', fg='black')
label_subtitle.pack(side=TOP, pady=25)

#Ajout des boutons amenant aux différentes pages
discussion_button=Button(frame, text="Discussion", font=("Helvetica", 25), bg='#41B77F', fg='black', command=open_discussion)
discussion_button.pack()

statistic_button=Button(frame, text="Stats", font=("Helvetica", 25), bg='#41B77F', fg='black', command=open_stats)
statistic_button.pack()

settings_button=Button(frame, text="Settings", font=("Helvetica", 25), bg='#41B77F', fg='black', command=open_settings)
settings_button.pack()

presentation_button=Button(frame, text="Presentation", font=("Helvetica", 25), bg='#41B77F', fg='black', command=open_presentation)
presentation_button.pack()

#Afficher la fenêtre
master.mainloop()

if __name__ == "__main__":
    print("main")