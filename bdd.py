import sqlite3 as sql

#Création de la BDD
bdd = sql.connect('chat.bd')

#Création du curseur qui va permettre de faire des requetes SQL 
c = bdd.cursor()

#Création de la table (elle est maintenant déjà créée)
# c.execute("""CREATE TABLE discussions(
#           id_conversation int,
#           id_utilisateur int,
#           id_message_conversation int,
#           text_message text
#           )""")

#Instructions SQL pour insérer des données dans la BDD (j'ai inséré le premier message)
# c.execute("INSERT INTO discussions VALUES (1,1,1, 'premier message')")

c.execute("SELECT * FROM discussions")
print (c.fetchall())

bdd.commit()
bdd.close()