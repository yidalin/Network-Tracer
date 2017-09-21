def sqlite_connnect(db):
    import sqlite3
    global connection
    global cursor
    connection = sqlite3.connect(db)
    cursor = connection.cursor()


def sqlite_close():
    cursor.close()
    connection.commit()
    connection.close()


def sqlite_create_table(table, column):
    create_table = "CREATE TABLE IF NOT EXISTS {}({})".format(table, column)
    cursor.execute(create_table)


def sqlite_insert_data(table, data):
    cursor.execute("INSERT INTO {} VALUES ({})".format(table, data))


def sqlite_query_all(table):
    cursor.execute("SELECT * FROM {}".format(table))
    values = cursor.fetchall()
    return values
