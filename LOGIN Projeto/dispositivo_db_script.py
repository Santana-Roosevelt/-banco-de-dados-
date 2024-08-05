import sqlite3

def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dispositivo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL,
                    localizacao TEXT NOT NULL,
                    status TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()