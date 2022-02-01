import sqlite3

#Conexão do banco de dados.
def connect():
    conn = sqlite3.connect('database/funcionarios.sqlite')
    return conn