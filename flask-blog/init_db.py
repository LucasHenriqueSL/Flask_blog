#importa biblioteca sqlite3
import sqlite3

#Cria o banco de dados relacional
connection = sqlite3.connect('database.db')

#Executa o esquema
with open('schema.sql') as f:
    connection.executescript(f.read())

#Conexão com o banco
cur = connection.cursor()


#Inserts
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
        )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
        )

#fecha a conexão com o banco
connection.commit()
connection.close()
