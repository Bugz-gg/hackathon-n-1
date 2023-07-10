from tkinter import *
import ttkbootstrap as ttk
import sqlite3 as sql
from datetime import *
from chat import *
import sys

#Définition des variables utiles au chat avec le bot afin d'éviter des erreurs
global text_sent_messages 
reconnect = True
#Classe principale de la page
class Page:
    def __init__(self, master, title, content):
        self.master = master
        self.title = title
        self.create_widgets(title, content)

    def create_widgets(self, title, content):
        #Personnaliser la fenêtre
        self.master.title(title)
        self.master.attributes("-fullscreen", True)
        #self.master.minsize(720,480)

        #Création du header, donc de la frame
        button_frame=Frame(self.master)
        button_frame.pack(side=TOP, pady = 30)

        for button_title in ["Discussion", "Stats", "Settings", "Presentation"]:
            if button_title == title:
                #Permet de désactiver le bouton de la page lorsque l'on est déjà dessus
                button = ttk.Button(button_frame, text=button_title, command=lambda x=button_title:open_page(x), state="disabled")
            else:
                button = ttk.Button(button_frame, text=button_title, command=lambda x=button_title:open_page(x), state="enabled")
            button.pack(side=LEFT)
        button = ttk.Button(button_frame, text="Exit", command=lambda :self.master.destroy(), state="enable")
        button.pack(side=LEFT)

        frame=Frame(self.master)
        frame.pack(side=TOP, pady= 20)

        # Set the flag variables to track initialization
        label_title_initialized = False
        # label_subtitle_initialized = False

        if not label_title_initialized:
            label_title = Label(frame, text=self.title, font=("Helvetica", 40))
            label_title.pack()

        content()
        

#Ce qui s'affiche lorsqu'on lance l'application pour la première fois
def main_content():
    label_subtitle = Label(root.master, text="Click on Discussion to start learning english with an amazing english teacher\n  Or click on presentation if you want to learn more about the fluencia project.", font=("Helvetica", 12))
    label_subtitle.pack(side=TOP, pady=50)
    pass

#Fonction qui gère la BDD de la page de discussion
def discussion_content():
    def save_data():
        global reconnect
        entry_value = entry_string.get()

        formatted_timestamp = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S').strftime('%m-%d %H:%M')
        formatted_message = f"[{formatted_timestamp}] You -- {entry_value}"
        text_sent_messages.configure(state='normal')
        text_sent_messages.insert(END, formatted_message + "\n")
        text_sent_messages.see(END)
        text_sent_messages.configure(state='disabled')
        text_sent_messages.update()
        past = ""
        if reconnect:
            bdd = sql.connect('chat.bd')
            c = bdd.cursor()
            c.execute("SELECT text_message, id_utilisateur FROM discussions ORDER BY id_message_conversation ASC")
            messages = c.fetchall()[-6:]  # Donne les 6 derniers messages au bot.
            bdd.close()

            if messages is not None:
                past = "These are the last messages you've exchanged with the user in case the user asks. There may be more. "
                for message in messages:
                    if message[1] != "Bot":
                        past += f"The user said : {message[0]}\n"
                    else:
                        past += f"You replied : {message[0]}\n"
                past += "Now the user says :"
            #print(past)
            reconnect = False
        output_value = science_tutoring(chat_input= past+entry_value).text + "\n"
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
        entry_string.set("")
        entry.config(textvariable=entry_string)
    global l, i , tab
    l, i, tab = 0, 0, []
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
    text_sent_messages = Text(frame_sent_messages, font="Calibri 14 bold", foreground="red")
    text_sent_messages.pack(fill=BOTH)

    display_messages(text_sent_messages)
    # text_sent_messages.tag_config("color", foreground="green")
    # for k in tab:
    #     text_sent_messages.tag_add("color", "{}.0".format(k[0]), "{}.{}".format(k[0], k[1]))
    pass

#Fonction affichant les messages envoyés (id_utilisateur de l'usager =1)
def display_messages(text_widget):
    bdd = sql.connect('chat.bd')
    c = bdd.cursor()
    c.execute("SELECT text_message, timestamp_message, id_utilisateur FROM discussions")

    messages = c.fetchall()
    bdd.close()
    text_widget.configure(state='normal')
    text_widget.delete('1.0', END)
    for message in messages:
        content = message[0]
        timestamp = message[1]
        nom_utilisateur = message[2]
        formatted_timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%m-%d %H:%M')
        formatted_message = f"[{formatted_timestamp}] {nom_utilisateur} -- {content}"
        text_widget.insert(END, formatted_message + "\n")
        # if (nom_utilisateur == "Bot"):
        #     #print(content, nom_utilisateur)
        #     global l, i
        #     l = len(content)
        #     tab.append([i, l]) 
        #     #print(l)
        # i+=1
    text_widget.see(END)
    text_widget.configure(state='disabled', wrap=WORD)

#Fonction définissant le contenu de la page stats
def stats_content():
    label_subtitle = Label(root.master, text="Coming soon.", font=("Helvetica", 20))
    label_subtitle.pack(side=TOP, pady=25)

#Fonction définissant le contenu de la page de réglages
def settings_content():
    label_subtitle = Label(root.master, text="Coming soon.", font=("Helvetica", 20))
    label_subtitle.pack(side=TOP, pady=25)
def presentation_content():
    def txt():
        return """
AI-Powered English Conversation Learning Program

Hello everyone! Today, we are excited to present our AI-powered English conversation learning program. With this innovative application, we aim to provide an immersive and interactive way for users to improve their English language skills.

Learning a new language, particularly English, can be a challenging task. Traditional methods often lack real-world context and fail to engage learners effectively. As a result, many individuals struggle to develop their conversational skills and build confidence in using English in practical situations.

Our AI-based program tackles this problem by offering a conversation-based approach to language learning. The program simulates real-life dialogues and engages users in interactive conversations.

Key Features:
1. Personalized Conversations: The program adapts to each user's proficiency level and provides tailored conversations that match their learning needs. Whether you're a beginner or an advanced learner, the program offers suitable challenges to enhance your skills.

2. (Futur feature) Speech Recognition: Our application utilizes advanced speech recognition technology to accurately analyze and evaluate users' spoken responses. This feature provides instant feedback, enabling learners to improve their pronunciation and fluency.

3. Grammar and Syntax Assistance: Our AI assistant helps users improve their grammar and sentence structure by providing suggestions and corrections during conversations. This feature ensures that learners develop accurate and grammatically correct English communication skills.

4. (Working on it) Progress Tracking: The program keeps track of users' progress, recording their performance in different conversation scenarios. Users can monitor their improvement over time, motivating them to continue practicing and achieving their language learning goals.

In conclusion, our AI-powered English conversation learning program revolutionizes the way individuals learn English. By offering an immersive and interactive experience, we aim to make language learning enjoyable, engaging, and effective. We believe that our application will empower users to gain confidence in their English speaking abilities and unlock new opportunities in their personal and professional lives.

Thank you for your attention!
"""

    label_subtitle = Label(root.master, text="Presentation time.", font=("Helvetica", 12))
    label_subtitle.pack(side=TOP, pady=25)
    label_subsubtitle = Text(root.master,  wrap=WORD)
    label_subsubtitle.insert(END, txt())
    label_subsubtitle.pack( fill=Y)
    label_subsubtitle.configure(state='disabled')
    pass


get_content = {"Main": main_content, "Discussion": discussion_content, "Stats": stats_content, "Settings": settings_content, "Presentation": presentation_content}


#Création de la fenêtre d'accueil
root = ttk.Window(themename='darkly')
displayed_page = Page(root, "Welcome to Fluencia", main_content)


def open_page(title):
    global displayed_page
    displayed_page.master.destroy() # Fermer la fenêtre principale
    displayed_page = Page(ttk.Window(themename='darkly'), title, get_content[title])
    displayed_page.master.mainloop()

root.mainloop()