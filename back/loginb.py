import sqlite3 as sq

def loging(log, passwd):
    connection = sq.connect('database/main.db')

    cursor = connection.cursor()

    request_to_read_data = "SELECT * FROM users"

    cursor.execute(request_to_read_data)

    data = cursor.fetchall()

    for i in data:
        if str(log) == str(i[1]) and str(passwd) == str(i[3]):
            return i
