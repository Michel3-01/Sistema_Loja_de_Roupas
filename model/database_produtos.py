import sqlite3

def connect():
    conn = sqlite3.connect('database/produtos.sqlite')
    return conn