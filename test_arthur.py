from tkinter import *
import ttkbootstrap as ttk

class MainPage:
    def __init__(self, master, title):
        self.master = master
        self.create_widgets(title)

    def create_widgets(self, title):
        #Personnaliser la fenêtre
        self.master.title(title)
        self.master.minsize(720,480)
        #self.master.config(background='#41B77F')

        #Définition des fonctions qui amènent aux différentes pages
        def open_discussion():
            self.master.destroy() # Fermer la fenêtre principale

            new_window = ttk.Window(themename='darkly')
            Page(new_window, "Discussion")
            new_window.mainloop()

        def open_stats():
            self.master.destroy() # Fermer la fenêtre principale

            new_window = ttk.Window(themename='darkly')
            Page(new_window, "Stats")
            new_window.mainloop()

        def open_settings():
            self.master.destroy() # Fermer la fenêtre principale

            new_window = ttk.Window(themename='darkly')
            Page(new_window, "Settings")
            new_window.mainloop()

        def open_presentation():
            self.master.destroy() # Fermer la fenêtre principale

            new_window = ttk.Window(themename='darkly')
            Page(new_window, "Presentation")
            new_window.mainloop()

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
        discussion_button=ttk.Button(button_frame, text="Discussion", command=open_discussion)
        discussion_button.pack(side=LEFT)

        statistic_button=ttk.Button(button_frame, text="Stats", command=open_stats)
        statistic_button.pack(side=LEFT)

        settings_button=ttk.Button(button_frame, text="Settings", command=open_settings)
        settings_button.pack(side=LEFT)

        presentation_button=ttk.Button(button_frame, text="Presentation", command=open_presentation)
        presentation_button.pack(side=LEFT)


class Page:
    def __init__(self, master, title):
        self.master = master
        self.create_widgets(title)

    def create_widgets(self, title):
        """

        :param title: The title of the widget.
        :param content_func: A function that
        :return:
        """
        #Personnaliser la fenêtre
        self.master.title(title)
        self.master.minsize(720,480)
        #self.master.config(background='#41B77F')

        # ...


#Création de la fenêtre d'accueil
root = ttk.Window(themename='darkly')
main_page = MainPage(root, "Main page")
root.mainloop()
