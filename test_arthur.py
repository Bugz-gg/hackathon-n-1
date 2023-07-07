from tkinter import *
import ttkbootstrap as ttk

class MainPage:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        #Personnaliser la fenêtre
        self.master.title('Main page')
        self.master.minsize(720,480)
        self.master.config(background='#41B77F')

        #Définition des fonctions qui amènent aux différentes pages
        def open_discussion():
            self.master.destroy()  # Fermer la fenêtre principale

            new_window = Tk()
            DiscussionPage(new_window)
            new_window.mainloop()

        def open_stats():
            self.master.destroy()  # Fermer la fenêtre principale

            new_window = Tk()
            StatsPage(new_window)
            new_window.mainloop()

        def open_settings():
            self.master.destroy()  # Fermer la fenêtre principale

            new_window = Tk()
            SettingsPage(new_window)
            new_window.mainloop()

        def open_presentation():
            self.master.destroy()  # Fermer la fenêtre principale

            new_window = Tk()
            PresentationPage(new_window)
            new_window.mainloop()

        #Création du header, donc de la frame
        frame=Frame(self.master, bg='#41B77F')
        frame.pack(side=TOP)

        #Ajout de texte (penser à mettre le même fond que la fenêtre pour ne pas voir le rectangle)
        #Catégories Discussion, Statistiques, Réglages, Présentation
        label_title = Label(frame, text="Template Header", font=("Helvetica", 40), bg='#41B77F', fg='black')
        label_title.pack()

        label_subtitle = Label(self.master, text="Template header to help the user figure out how the interface is looking", font=("Helvetica", 20), bg='#41B77F', fg='black')
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

class DiscussionPage:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        #Personnaliser la fenêtre
        self.master.title('Discussion')
        self.master.minsize(720,480)
        self.master.config(background='#41B77F')

        # ...

class StatsPage:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        #Personnaliser la fenêtre
        self.master.title('Stats')
        self.master.minsize(720,480)
        self.master.config(background='#41B77F')

        # ...

class SettingsPage:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        #Personnaliser la fenêtre
        self.master.title('Settings')
        self.master.minsize(720,480)
        self.master.config(background='#41B77F')

        # ...

class PresentationPage:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        #Personnaliser la fenêtre
        self.master.title('Presentation')
        self.master.minsize(720,480)
        self.master.config(background='#41B77F')

        # ...

#Création de la fenêtre d'accueil
root = Tk()
main_page = MainPage(root)
root.mainloop()
