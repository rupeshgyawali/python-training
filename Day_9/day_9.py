# python -m tkinter
import tkinter as tk

window = tk.Tk()
window.title('Hello World!')

# label_hello = tk.Label(text='Hello World!', fg='white', background='black', width=10, height=5)
# label_hello.pack()

entry_name = tk.Entry(fg='black', bg='white', width=10)
entry_name.pack()

def say_hello():
    name = entry_name.get()
    label_hello = tk.Label(text=f'Hello {name}')
    label_hello.pack()

# button_greet = tk.Button(text="Greet", width=5, height=2, fg='#f2f2f2', bg='#222222', command=lambda : print('Clicked!'))
button_greet = tk.Button(text="Greet", width=5, height=2, fg='#f2f2f2', bg='#222222', command=say_hello)
button_greet.pack()

window.mainloop()