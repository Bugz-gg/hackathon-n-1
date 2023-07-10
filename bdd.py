import sqlite3 as sql
from datetime import *


def create_table():
    bdd = sql.connect('chat.bd')
    c = bdd.cursor()
    c.execute("""CREATE TABLE discussions(id_conversation INTEGER,
    id_utilisateur TEXT,
    id_message_conversation INTEGER,
    text_message TEXT,
    timestamp_message TEXT
    )""")
    bdd.commit()
    bdd.close()

if __name__=="__main__":
    create_table()
    # Création de la BDD
    bdd = sql.connect('chat.bd')

    # Création du curseur qui va permettre de faire des requetes SQL
    c = bdd.cursor()

    # Instructions SQL pour insérer des données dans la BDD (j'ai inséré le premier message)
    # c.execute("INSERT INTO discussions VALUES (1,1,1, 'premier message', '2020-01-01 00:00')")

    c.execute("SELECT * FROM discussions")
    print(c.fetchall())

    bdd.commit()
    bdd.close()