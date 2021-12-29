import sqlite3


class DatabaseHandler:
    def __init__(self):
        conn = sqlite3.connect("todo.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Todos(
            id integer primary key,
            desc text,
            completed integer
        )""")
        conn.commit()
        conn.close()

    def insert(self, todo):
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("""INSERT INTO Todos VALUES(NULL, ?, ?)""", (todo, 0))
        conn.commit()
        conn.close()

    def get_all(self):
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("""SELECT * FROM Todos""")
        todos = c.fetchall()
        conn.close()
        return todos

    def update(self, id, completed=True):
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("""UPDATE Todos SET completed=? WHERE id=?""", (completed, id))
        conn.commit()
        conn.close()

    def delete(self, id):
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("""DELETE FROM Todos WHERE id=?""", (id,))
        conn.commit()
        conn.close()
