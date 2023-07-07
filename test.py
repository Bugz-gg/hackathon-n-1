from tkinter import *
import ttkbootstrap as ttk



global dic 
dic = {'master': TypeError}


#Définition des fonctions qui amènent aux différentes pages
def open_discussion(master):
    with open("discussion.py", "r") as file:
        master.destroy()
        code = file.read()
        exec(code)

def discussion():
    open_discussion(dic["master"])

dic["open_discussion"] = discussion

def open_stats(master):
    with open("stats.py", "r") as file:
        master.destroy()
        code = file.read()
        exec(code)

def start():
    open_stats(dic["master"])

dic["open_stats"] = start

def open_settings(master):
    with open("settings.py", "r") as file:
        master.destroy()
        code = file.read()
        exec(code)

def settings():
    open_settings(dic["master"])

dic["open_settings"] = settings


def open_presentation(master):
    master.destroy()
    with open("presentation.py", "r") as file:
        code = file.read()
        exec(code)

def presentation():
    open_presentation(dic["master"])

dic["open_presentation"] = presentation



if __name__ == "__main__":
        #Création de la fenêtre d'accueil
    master = ttk.Window(themename= 'journal')
    dic["master"] = master
    #Personnaliser la fenêtre
    master.title('Main page')
    master.minsize(720,480)
    #master.iconbitmap("images/logo_icon.ico")
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