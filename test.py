from tkinter import *
import ttkbootstrap as ttk
import sqlite3 as sql
from datetime import *
from chat import *

#Définition des variables utiles au chat avec le bot afin d'éviter des erreurs
global text_sent_messages 
text_sent_messages = None
global text_received_messages
text_received_messages = None

#Classe principale de la page
class Page:
    def __init__(self, master, title, content):
        self.master = master
        self.title = title
        self.create_widgets(title, content)

    def create_widgets(self, title, content):
        #Personnaliser la fenêtre
        self.master.title(title)
        self.master.minsize(720,480)
        #self.master.config(background='#41B77F')

        #Création du header, donc de la frame
        button_frame=Frame(self.master)
        button_frame.pack(side=TOP, pady = 20)
        for button_title in ["Discussion", "Stats", "Settings", "Presentation"]:
            if button_title == title:
                print("tamaga desu")
                #Permet de désactiver le bouton de la page lorsque l'on est déjà dessus
                button = ttk.Button(button_frame, text=button_title, command=lambda x=button_title:open_page(x), state="disabled")
            else:
                button = ttk.Button(button_frame, text=button_title, command=lambda x=button_title:open_page(x), state="enabled")
            button.pack(side=LEFT)

        frame=Frame(self.master)
        frame.pack(side=TOP, pady= 20)


        #Ajout de texte (penser à mettre le même fond que la fenêtre pour ne pas voir le rectangle)
        #Catégories Discussion, Statistiques, Réglages, Présentation
        
        # Set the flag variables to track initialization
        label_title_initialized = False
        # label_subtitle_initialized = False

        if not label_title_initialized:
            label_title = Label(frame, text=self.title , font=("Helvetica", 40), bg='#41B77F', fg='black')
            label_title.pack()
            label_title_initialized = True
        else:
            label_title.pack_forget()

        # if not label_subtitle_initialized:
        #     label_subtitle = Label(frame, text="Template header to help the user figure out how the interface is looking", font=("Helvetica", 20), bg='#41B77F', fg='black')
        #     label_subtitle.pack(side=TOP, pady=25)
        #     label_subtitle_initialized = True
        # else:
        #     label_subtitle.pack_forget()


        #Ajout des boutons amenant aux différentes pages

        content()

#Ce qui s'affiche lorsqu'on lance l'application pour la première fois
def main_content():
    label_subtitle = Label(root.master, text="Appuyez sur une touche. (Ça ne fait rien et c'est normal.)",
                           font=("Helvetica", 20), bg='#41B77F', fg='black')
    label_subtitle.pack(side=TOP, pady=25)
    pass

#Fonction qui gère la BDD de la page de discussion
def discussion_content():
    output_string = StringVar()

    def save_data():
        nonlocal output_string
        entry_value = entry_string.get()
        output_value = science_tutoring(chat_input= entry_value).text + "\n"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        bdd = sql.connect('chat.bd')
        c = bdd.cursor()
        c.execute("SELECT MAX(id_message_conversation) FROM discussions")
        result = c.fetchone()
        if result[0] is not None:
            current_id = result[0] + 1
        else:
            current_id = 1
        c.execute("INSERT INTO discussions(id_conversation, id_utilisateur, id_message_conversation, text_message, timestamp_message) VALUES (?, ?, ?, ?, ?)",
                  (1, "You", current_id, entry_value, timestamp))
        c.execute("INSERT INTO discussions(id_conversation, id_utilisateur, id_message_conversation, text_message, timestamp_message) VALUES (?, ?, ?, ?, ?)",
                  (1, "Bot", current_id + 1, output_value, timestamp))
        bdd.commit()
        bdd.close()
        display_messages(text_sent_messages)

    new_lab = Label(root.master)

    entry_string = StringVar()
    entry = ttk.Entry(new_lab, textvariable=entry_string)
    submit_button = ttk.Button(new_lab, text='submit', command=save_data)
    entry.pack(side='left')
    submit_button.pack(side='left', padx=10)
    new_lab.pack(side=TOP)

    global text_sent_messages
    frame_sent_messages = Frame(root.master)
    frame_sent_messages.pack(side=TOP, pady=20)
    text_sent_messages = Text(frame_sent_messages, height=10, width=50)
    text_sent_messages.pack()

    global text_received_messages
    frame_received_messages = Frame(root.master)
    frame_received_messages.pack(side=TOP, pady=20)
    text_received_messages = Text(frame_received_messages, height=10, width=50)
    text_received_messages.pack()


    display_messages(text_sent_messages)
    pass

#Fonction affichant les messages envoyés (id_utilisateur de l'usager =1)
def display_messages(text_widget):
    bdd = sql.connect('chat.bd')
    c = bdd.cursor()
    c.execute("SELECT text_message, timestamp_message, id_utilisateur FROM discussions")
    messages = c.fetchall()
    text_widget.delete('1.0', END)
    for message in messages:
        content = message[0]
        timestamp = message[1]
        nom_utilisateur = message[2]
        formatted_timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%m-%d %H:%M')
        formatted_message = f"[{formatted_timestamp}] {nom_utilisateur} -- {content}"
        text_widget.insert(END, formatted_message + "\n")
    bdd.close()

#Fonction définissant le contenu de la page stats
def stats_content():
    label_subtitle = Label(root.master, text="Check your stats.",
                           font=("Helvetica", 20), bg='#41B77F', fg='black')
    label_subtitle.pack(side=TOP, pady=25)
    pass

#Fonction définissant le contenu de la page de réglages
def settings_content():
    label_subtitle = Label(root.master, text="Settings are here.",
                           font=("Helvetica", 20), bg='#41B77F', fg='black')
    label_subtitle.pack(side=TOP, pady=25)
    pass
def presentation_content():
    #label_subtitle.pack_forget()
    label_subtitle = Label(root.master, text="Presentation time.",
                           font=("Helvetica", 20), bg='#41B77F', fg='black')
    label_subtitle.pack(side=TOP, pady=25)
    pass


get_content = {"Main": main_content, "Discussion": discussion_content, "Stats": stats_content, "Settings": settings_content, "Presentation": presentation_content}


#Création de la fenêtre d'accueil
root = ttk.Window(themename='darkly')
displayed_page = Page(root, "Main page", main_content)


def open_page(title):
    global displayed_page
    displayed_page.master.destroy() # Fermer la fenêtre principale
    displayed_page = Page(ttk.Window(themename='darkly'), title, get_content[title])
    displayed_page.master.mainloop()

root.mainloop()