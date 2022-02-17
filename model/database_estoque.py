import sqlite3


def connect():
    conn = sqlite3.connect('database/estoque.sqlite')
    return conn