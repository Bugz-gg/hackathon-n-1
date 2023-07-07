from tkinter import *
import ttkbootstrap as ttk


class Page:
    def __init__(self, master, title, content):
        self.master = master
        self.title = title
        self.create_widgets(title, content)

    def load_buttons(self, button_frame, disabled: str = None):
        for title in ["Discussion", "Stats", "Settings", "Presentation"]:
            if disabled == title:
                print("tamaga desu")
                button = ttk.Button(button_frame, text=title, command=lambda x=title:open_page(title), state="disabled")
            else:
                button = ttk.Button(button_frame, text=title, command=lambda x=title:open_page(title), state="enabled")
            button.pack(side=LEFT)

    def create_widgets(self, title, content):
        #Personnaliser la fenêtre
        self.master.title(title)
        self.master.minsize(720,480)
        #self.master.config(background='#41B77F')

        #Définition des fonctions qui amènent aux différentes pages


        #Création du header, donc de la frame
        button_frame=Frame(self.master)
        button_frame.pack(side=TOP, pady = 20)

        frame=Frame(self.master)
        frame.pack(side=TOP, pady= 20)


        #Ajout de texte (penser à mettre le même fond que la fenêtre pour ne pas voir le rectangle)
        #Catégories Discussion, Statistiques, Réglages, Présentation
        label_title = Label(frame, text="Template Header", font=("Helvetica", 40))
        label_title.pack()

        label_subtitle = Label(self.master, text="Template header to help the user figure out how the interface is looking", font=("Helvetica", 20), bg='#41B77F', fg='black')
        label_subtitle.pack(side=TOP, pady=25)

        #Ajout des boutons amenant aux différentes pages
        self.load_buttons(button_frame, self.title)

        content()

def main_content():
    label_subtitle = Label(root.master, text="Appuyez sur une touche. (Ça ne fait rien et c'est normal.)",
                           font=("Helvetica", 20), bg='#41B77F', fg='black')
    label_subtitle.pack(side=TOP, pady=25)
    pass

def discussion_content():
    label_subtitle = Label(displayed_page.master, text="Nani ga.",
                           font=("Helvetica", 20), bg='#41B77F', fg='black')
    label_subtitle.pack(side=TOP, pady=25)
    pass

def stats_content():
    label_subtitle = Label(displayed_page.master, text="Check your stats.",
                           font=("Helvetica", 20), bg='#41B77F', fg='black')
    label_subtitle.pack(side=TOP, pady=25)
    pass
def settings_content():
    label_subtitle = Label(displayed_page.master, text="Settings are here.",
                           font=("Helvetica", 20), bg='#41B77F', fg='black')
    label_subtitle.pack(side=TOP, pady=25)
    pass
def presentation_content():
    #label_subtitle.pack_forget()
    label_subtitle = Label(displayed_page.master, text="Presentation time.",
                           font=("Helvetica", 20), bg='#41B77F', fg='black')
    label_subtitle.pack(side=TOP, pady=25)
    pass


get_content = {"Main": main_content, "Discussion": discussion_content, "Stats": stats_content, "Settings": settings_content, "Presentation": presentation_content}


#Création de la fenêtre d'accueil
root = ttk.Window(themename='darkly')
displayed_page = Page(root, "Main page", main_content)


def open_discussion(master):
    master.destroy() # Fermer la fenêtre principale

    new_window = ttk.Window(themename='darkly')
    Page(new_window, "Discussion")
    new_window.mainloop()

def open_stats(master):
    master.destroy() # Fermer la fenêtre principale

    new_window = ttk.Window(themename='darkly')
    Page(new_window, "Stats")
    new_window.mainloop()

def open_settings(master):
    master.destroy() # Fermer la fenêtre principale

    new_window = ttk.Window(themename='darkly')
    Page(new_window, "Settings")
    new_window.mainloop()

def open_page(title):
    global displayed_page
    displayed_page.master.destroy() # Fermer la fenêtre principale
    new_window = ttk.Window(themename='darkly')
    displayed_page = Page(new_window, title, get_content[title])
    new_window.mainloop()





root.mainloop()