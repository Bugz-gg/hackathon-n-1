import tkinter as tk
import ttkbootstrap as ttk
from test import *

# Création de la fenêtre d'accueil
master = ttk.Window(themename='darkly')

# Personnaliser la fenêtre
master.title('Main page')
master.minsize(720, 480)

# Définition des fonctions qui amènent aux différentes pages
def open_discussion():
    with open("discussion.py", "r") as file:
        code = file.read()
        exec(code)
    ttk.quit()  # Fermer la fenêtre principale

def open_stats():
    with open("stats.py", "r") as file:
        code = file.read()
        exec(code)
    ttk.quit()  # Fermer la fenêtre principale

def open_settings():
    with open("settings.py", "r") as file:
        code = file.read()
        exec(code)
    ttk.quit()  # Fermer la fenêtre principale

def open_presentation():
    with open("presentation.py", "r") as file:
        code = file.read()
        exec(code)
    ttk.quit()  # Fermer la fenêtre principale

# Création des différentes frames
buttons_frame = ttk.Frame(master)
title_frame = ttk.Frame(master)
exit_frame = ttk.Frame(master)

# Ajout du titre
label_title = ttk.Label(title_frame, text="Template Header", font="Helvetica 25")
label_title.pack(pady=10)

# Ajout des boutons amenant aux différentes pages
discussion_button = ttk.Button(buttons_frame, text="Discussion", command=open_discussion)
discussion_button.pack(side='left', pady=30)

statistic_button = ttk.Button(buttons_frame, text="Stats", command=open_stats)
statistic_button.pack(side='left', pady=30)

settings_button = ttk.Button(buttons_frame, text="Settings", command=open_settings)
settings_button.pack(side='left', pady=30)

presentation_button = ttk.Button(buttons_frame, text="Presentation", command=open_presentation)
presentation_button.pack(side='left', pady=30)

# Ajout du bouton quitter
exit_button = ttk.Button(exit_frame, text="Exit", command=ttk.destroy)
exit_button.pack(side=TOP, pady=30)

# Disposition des frames sur la page
buttons_frame.pack(side=TOP)
exit_frame.pack(side=TOP)
title_frame.pack(side=TOP)

# Ajout du sous-titre
label_subtitle = ttk.Label(master, text="Template header to help the user figure out how the interface is looking", font="Helvetica 12")
label_subtitle.pack(side=TOP, pady=50)

# Afficher la fenêtre
master.mainloop()

if __name__ == "__main__":
    print("main")
