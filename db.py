import sqlite3


def connect_db():
    db = sqlite3.connect('database.db')
    db.cursor().execute('CREATE TABLE IF NOT EXISTS info '
                        '(username VARCHAR(10) PRIMARY KEY, '
                        'password VARCHAR(10), '
                        'address TEXT, '
                        'phone VARCHAR(15))')
    records = [('Adam', 'mada', 'Brooklyn', '1234567'),
               ('Ben', 'neb', 'Manhattan', '2345678'),
               ('Cathy', 'yhtac', 'Queens', '3456789')]
    db.cursor().executemany('INSERT OR IGNORE INTO info (username, password, address, phone) '
                            'VALUES (?, ?, ?, ?);', records)
    db.commit()
    return db


def get_info(user_name=None, password=None):
    db = connect_db()
    get_all_query = 'SELECT username, address, phone FROM info ' \
                    'WHERE username = \'' + user_name + '\' and password = \'' + password + '\''
    return db.cursor().execute(get_all_query).fetchall()
