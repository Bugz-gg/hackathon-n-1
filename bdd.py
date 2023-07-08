import sqlite3 as sql
from datetime import *

#Création de la BDD
bdd = sql.connect('chat.bd')

#Création du curseur qui va permettre de faire des requetes SQL 
c = bdd.cursor()

#Création de la table (elle est maintenant déjà créée)
# c.execute("""CREATE TABLE discussions(
#           id_conversation INTEGER,
#           id_utilisateur INTEGER,
#           id_message_conversation INTEGER,
#           text_message TEXT,
#           timestamp_message TEXT
#           )""")

#Instructions SQL pour insérer des données dans la BDD (j'ai inséré le premier message)
# c.execute("INSERT INTO discussions VALUES (1,1,1, 'premier message', '2020-01-01 00:00')")

c.execute("SELECT * FROM discussions")
print (c.fetchall())

bdd.commit()
bdd.close()