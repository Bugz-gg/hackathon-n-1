from tkinter import *

#Création de la fenêtre d'accueil
master = Tk()

#Personnaliser la fenêtre
master.title('Accueil')
master.minsize(720,480)
master.iconbitmap("images/logo_icon.ico")
master.config(background='#41B77F')

#Création du header, donc de la frame
frame=Frame(master, bg='#41B77F')
frame.pack(side=TOP)

#Ajout de texte (penser à mettre le même fond que la fenêtre pour ne pas voir le rectangle)
#Catégories Discussions, Statistiques, Réglages, Présentation
label_title = Label(frame, text="Discussions", font=("Helvetica", 40), bg='#41B77F', fg='black')
label_title.pack(side="top")

label_title = Label(frame, text="Statistiques", font=("Helvetica", 40), bg='#41B77F', fg='black')
label_title.pack(side="top")

label_title = Label(frame, text="Règlages", font=("Helvetica", 40), bg='#41B77F', fg='black')
label_title.pack(side="top")

label_title = Label(frame, text="Présentartion", font=("Helvetica", 40), bg='#41B77F', fg='black')
label_title.pack(side="top")

#Afficher la fenêtre
master.mainloop()

if __name__ == "__main__":
    print("main")