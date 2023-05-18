
import sqlite3


def create_db():
    conn = sqlite3.connect("baza.db")
    cursor = conn.cursor()

def create_table_users():
    conn = sqlite3.connect("baza.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists Users (\
                    username varchar(150), \
                    telegram_id int, \
                    phone_number varchar(20) \
                    )"
                    )


def insert_users(username, telegram_id, phone_number):
    conn = sqlite3.connect("baza.db")
    cursor = conn.cursor()
    cursor.execute("insert into Users values ('{}', {}, '{}')".format(username, telegram_id, phone_number))
    conn.commit()

def select_users(telegram_id):
    conn = sqlite3.connect("baza.db")
    cursor = conn.cursor()
    cursor.execute("select * from Users where telegram_id={}".format(telegram_id))
    return cursor.fetchone()


def create_table_category():
    conn = sqlite3.connect("baza.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists Book_categories ( \
                    category_id INTEGER PRIMARY KEY autoincrement, \
                    category_name varchar(50) \
                    )"
                    )

def create_table_books():
    conn = sqlite3.connect("baza.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists Books ( \
                    id INTEGER PRIMARY KEY autoincrement, \
                    category_id int, \
                    book_name varchar(50), \
                    book_description text, \
                    book_photo text \
                    )"
                    )
