import sqlite3


def connect():
    conn = sqlite3.connect('database/vendas.sqlite')
    return conn