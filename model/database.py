import sqlite3

#Conexão do banco de dados.
def connect():
    #Cria a conexão.
    conn = sqlite3.connect('database/clientes.sqlite')
    return conn