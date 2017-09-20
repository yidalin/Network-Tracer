import sqlite3


connection = sqlite3.connect('sqlite.db')

cursor = connection.cursor()

create_table = 'create table books (tit)'