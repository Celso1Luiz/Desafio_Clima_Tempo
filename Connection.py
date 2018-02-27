import sqlite3

conn = sqlite3.connect('climatempo.db')
cursor = conn.cursor()


def criar_tabela():
    
    cursor.execute('''
        Create table if not exists climatempo
        (
            id INTEGER NOT NULL ,
            cidade TEXT NOT NULL ,
            estado VARCHAR(2) NOT NULL,
            pais TEXT NOT NULL,
            data TEXT NOT NULL,
            tempMax TEXT NOT NULL,
            tempMin TEXT NOT NULL
        );
    ''')
    print '''------------------------------------------
|              Tabela Criada             |
------------------------------------------\n'''

def apagar():
    cursor.execute("drop table if exists climatempo")
apagar()
criar_tabela()
