import tkinter as tk

from database import DatabaseHandler


class TodoApp:
    def __init__(self, window:tk.Tk, db_handler):
        self.db_handler = db_handler

        self.window = window
        self.window.title('Todo')
        self.window.geometry('550x700')

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(2, weight=1)

        lbl_title = tk.Label(text='TODO', font=('Arial', 17, 'bold'))
        lbl_title.grid(row=0, column=0, sticky=tk.NSEW, pady=20)

        frm_todo_entry = tk.Frame(self.window)
        frm_todo_entry.grid(row=1, column=0, sticky=tk.NSEW, padx=40)
        frm_todo_entry.columnconfigure(0, weight=1)

        self.ent_todo = tk.Entry(frm_todo_entry, font=('Arial', 12), relief=tk.FLAT, borderwidth=5)
        self.ent_todo.grid(row=0, column=0, pady=40, sticky=tk.NSEW)

        btn_add = tk.Button(frm_todo_entry, text='+', command=self._add, borderwidth=0, bg='lightgreen', padx=5, font=('Arial', 12))
        btn_add.grid(row=0, column=1)

        self._list()
        self._bind_keys()

    def _bind_keys(self):
        self.ent_todo.bind('<Return>', lambda event: self._add())

    def _fetch_todos(self):
        self.todos = self.db_handler.get_all()

    def run(self):
        self.window.mainloop()

    def _list(self):
        try:
            self.frm_todos.destroy()
        except AttributeError:
            pass
        finally:
            self.frm_todos = tk.Frame(master=self.window, bg='white', pady=10)
            self.frm_todos.grid(row=2, column=0, sticky=tk.NSEW)
            self.frm_todos.columnconfigure(0, weight=1)

        self._fetch_todos()

        i=None
        for i, todo in enumerate(self.todos):
            if not todo[2]:
                frm_todo = tk.Frame(self.frm_todos)
                frm_todo.grid(row=i, column=0, sticky=tk.NSEW, padx=40, pady=2)
                frm_todo.columnconfigure(0, weight=1)

                lbl_todo = tk.Label(master=frm_todo, text=todo[1], bg='lightblue', font=('Arial', 12))
                lbl_todo.grid(row=0, column=0, sticky=tk.NSEW)

                btn_delete = tk.Button(
                    master=frm_todo, text='✔', command=lambda index=i: self._completed(index), borderwidth=0, bg='lightgreen', padx=5, font=('Arial', 12))
                btn_delete.grid(row=0, column=1)

        next_row = 0 if i is None else i+1
        lbl_completed = tk.Label(master=self.frm_todos, text="Completed", bg='white', font=('Arial', 12, 'bold'))
        lbl_completed.grid(row=next_row, column=0, sticky=tk.NSEW, pady=20)

        for j, todo in enumerate(self.todos, start=1):
            if todo[2]:
                frm_todo = tk.Frame(self.frm_todos)
                frm_todo.grid(row=next_row+j, column=0, sticky=tk.NSEW, padx=40, pady=2)
                frm_todo.columnconfigure(0, weight=1)

                lbl_todo = tk.Label(master=frm_todo, text=todo[1], bg='lightblue', font=('Arial', 12))
                lbl_todo.grid(row=0, column=0, sticky=tk.NSEW)

                btn_delete = tk.Button(
                    master=frm_todo, text='x', command=lambda index=j-1: self._delete(index), borderwidth=0, bg='red', padx=5, font=('Arial', 12))
                btn_delete.grid(row=0, column=1)

    def _delete(self, index):
        self.db_handler.delete(self.todos[index][0])
        self._list()

    def _completed(self, index):
        self.db_handler.update(self.todos[index][0], completed=True)
        self._list()

    def _add(self):
        todo = self.ent_todo.get()
        if todo:
            self.ent_todo.delete(0, tk.END)
            self.db_handler.insert(todo)
            self._list()


if __name__ == '__main__':
    window = tk.Tk()
    db_handler = DatabaseHandler()

    app = TodoApp(window, db_handler)
    app.run()
