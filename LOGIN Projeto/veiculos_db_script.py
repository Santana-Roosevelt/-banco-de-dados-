import sqlite3

def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS veiculos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    modelo TEXT NOT NULL,
                    placa TEXT NOT NULL,
                    status TEXT
                )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
