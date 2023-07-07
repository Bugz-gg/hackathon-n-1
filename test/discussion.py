from tkinter import *
import ttkbootstrap as ttk
from test import *
import sys

if __name__ == "__main__":
    if dic["master"] is None:
        # La fenêtre principale n'a pas encore été définie
        exit()

    window = dic["master"]
    window.title("Presentation")
    window.attributes('-fullscreen', True)

    buttons_frame = ttk.Frame(window)
    title_frame = ttk.Frame(window)

    discussion_button = ttk.Button(
        buttons_frame, text="Discussion", command=dic["open_discussion"])
    discussion_button.pack(side='left', pady=30)

    statistic_button = ttk.Button(
        buttons_frame, text="Stats", command=dic["open_stats"])
    statistic_button.pack(side='left', pady=30)

    settings_button = ttk.Button(
        buttons_frame, text="Settings", command=dic["open_settings"])
    settings_button.pack(side='left', pady=30)

    presentation_button = ttk.Button(
        buttons_frame, text="Presentation", command=dic["open_presentation"], state='disabled')
    presentation_button.pack(side='left', pady=30)
    buttons_frame.pack(side=TOP)

    title = ttk.Label(master=window, text='Presentation', font="Helvetica 12 bold")
    title.pack()

    input_frame = ttk.Frame(master=window)
    text = ttk.Label(master=input_frame, text='description', font="Helvetica 12")
    text.pack()
    input_frame.pack(pady=50)

    window.mainloop()


##############################################################################################################

from tkinter import *

import ttkbootstrap as ttk



global dic 
dic = {'master': None}


#Définition des fonctions qui amènent aux différentes pages
def open_discussion(master):
    discussion_window = Toplevel(master)
    master.destroy()
    dic['master'] = discussion_window
    with open("discussion.py", "r") as file:
        code = file.read()
        exec(code, globals(), {'master': discussion_window})


def discussion():
    open_discussion(dic["master"])

dic["open_discussion"] = discussion

def open_stats(master):
    stats_window = Toplevel(master)
    dic['master'] = stats_window
    with open("stats.py", "r") as file:
        code = file.read()
        exec(code, globals(), {'master': stats_window})


def start():
    open_stats(dic["master"])

dic["open_stats"] = start

def open_settings(master):
    settings_window = Toplevel(master)
    dic['master'] = settings_window
    with open("settings.py", "r") as file:
        code = file.read()
        exec(code, globals(), {'master': settings_window})


def settings():
    open_settings(dic["master"])

dic["open_settings"] = settings


def open_presentation(master):
    presentation_window = Toplevel(master)
    dic['master'] = presentation_window
    master.destroy()
    with open("presentation.py", "r") as file:
        code = file.read()
        exec(code, globals(), {'master': presentation_window})

def presentation():
    open_presentation(dic["master"])

dic["open_presentation"] = presentation



if __name__ == "__main__":
        #Création de la fenêtre d'accueil
    master = ttk.Window(themename= 'journal')
    dic["master"] = master
    #Personnaliser la fenêtre
    master.title('Main page')
    master.attributes('-fullscreen', True)
    #Création du header, donc de la frame
    buttons_frame=ttk.Frame(master)
    title_frame=ttk.Frame(master)

    label_title = ttk.Label(title_frame, text="Template Header", font="Helvetica 25")
    label_title.pack(pady=10)

    #Ajout des boutons amenant aux différentes pages
    discussion_button= ttk.Button(buttons_frame, text="Discussion", command= dic["open_discussion"])
    discussion_button.pack(side='left', pady=30)

    statistic_button=ttk.Button(buttons_frame, text="Stats", command= dic["open_stats"])
    statistic_button.pack(side='left', pady=30)

    settings_button=ttk.Button(buttons_frame, text="Settings", command= dic["open_settings"])
    settings_button.pack(side='left', pady=30)

    presentation_button=ttk.Button(buttons_frame, text="Presentation", command= dic["open_presentation"])
    presentation_button.pack(side='left', pady=30)

    buttons_frame.pack(side=TOP)
    title_frame.pack(side=TOP)

    label_subtitle = ttk.Label(master, text="Template header to help the user figure out how the interface is looking", font="Helvetica 12")
    label_subtitle.pack(side=TOP, pady=50)

    #Afficher la fenêtre
    master.mainloop()