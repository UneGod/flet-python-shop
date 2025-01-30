import sqlite3 as sq

def register(*user):

    connection = sq.connect('database/main.db')

    cursor = connection.cursor()


    users = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        user_email TEXT NOT NULL,
        user_pass TEXT NOT NULL,
        is_admin TEXT NOT NULL,
        photo_url TEXT,
        UNIQUE (user_name, user_email)
    )
    '''

    cursor.execute(users)

    connection.commit()

    request_to_insert_data = '''
    INSERT INTO users (user_name, user_email, user_pass, is_admin, photo_url) VALUES (?, ?, ?, ?, ?);
    '''

    try:
        cursor.execute(request_to_insert_data, user)
        connection.commit()
    except Exception as e:
        return 0

    cursor.close()
    connection.close()