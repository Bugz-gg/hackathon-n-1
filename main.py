from tkinter import *

#Création de la fenêtre d'accueil
master = Tk()

#Personnaliser la fenêtre
master.title('Main page')
master.minsize(720,480)
#master.iconbitmap("images/logo_icon.ico")
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

label_title = Label(frame, text="Template Header", font=("Helvetica", 40), bg='#41B77F', fg='black')
label_title.pack(pady=10)

#Ajout des boutons amenant aux différentes pages
discussion_button=Button(frame, text="Discussion", font=("Helvetica", 25), bg='#41B77F', fg='black', command=open_discussion)
discussion_button.pack(side='left', pady=30)

statistic_button=Button(frame, text="Stats", font=("Helvetica", 25), bg='#41B77F', fg='black', command=open_stats)
statistic_button.pack(side='left', pady=30)

settings_button=Button(frame, text="Settings", font=("Helvetica", 25), bg='#41B77F', fg='black', command=open_settings)
settings_button.pack(side='left', pady=30)

presentation_button=Button(frame, text="Presentation", font=("Helvetica", 25), bg='#41B77F', fg='black', command=open_presentation)
presentation_button.pack(side='left', pady=30)
frame.pack(side=TOP)


label_subtitle = Label(master, text="Template header to help the user figure out how the interface is looking", font=("Helvetica", 20), bg='#41B77F', fg='black')
label_subtitle.pack(side=TOP, pady=50)

#Afficher la fenêtre
master.mainloop()

if __name__ == "__main__":
    print("main")