import tkinter as tk

class CalculatorApp:
    def __init__(self, window):
        self.window = window
        self.window.title('Calculator')
        self.window.geometry("350x600")
        self.window.resizable(False, False)

        self.number = ""
        self.expression = ""
        self.obtained_result = False

        self.frm_display = tk.Frame(self.window, height=250)
        self.frm_display.pack(fill=tk.BOTH, expand=True)
        self.lbl_expression = tk.Label(self.frm_display, text=self.expression, font=('Arial', 20, 'bold'), padx=12, anchor=tk.E)
        self.lbl_expression.pack(fill=tk.BOTH, expand=True)
        self.lbl_number = tk.Label(self.frm_display, text=self.number, font=('Arial', 20, 'bold'), padx=12, anchor=tk.E)
        self.lbl_number.pack(fill=tk.BOTH, expand=True)

        self.frm_buttons = tk.Frame(self.window)
        self.frm_buttons.pack(fill=tk.BOTH, expand=True)
        self.frm_buttons.columnconfigure([0, 1,2,3], weight=1)
        self.frm_buttons.rowconfigure([0,1,2,3,4], weight=1)
        
        self._create_buttons()
        self._bind_keys()

    def _bind_keys(self):
        self.window.bind("<Return>", lambda event: self._evaluate())
        for i in range(10):
            self.window.bind(str(i), lambda event, digit=i: self._digit_press(digit))

        for op in ('/', '*', '+', '-'):
            self.window.bind(op, lambda event, operator=op: self._operator_press(operator))

    def _create_buttons(self):
        digit_location = {
            7: (1, 0), 8: (1, 1), 9: (1, 2),
            4: (2, 0), 5: (2, 1), 6: (2, 2),
            1: (3, 0), 2: (3, 1), 3: (3, 2),
            0: (4, 1), '.': (4, 0)
        }
        for digit, location in digit_location.items():
            btn_num = tk.Button(self.frm_buttons, text=str(digit), bg='white', font=('Arial', 20), borderwidth=0, command=lambda x=digit: self._digit_press(x))
            btn_num.grid(row=location[0],column=location[1], sticky=tk.NSEW)
        
        btn_equals = tk.Button(self.frm_buttons, text='=', bg='lightblue', font=('Arial', 20), borderwidth=0, command=lambda:self._evaluate())
        btn_equals.grid(row=4, column=2, columnspan=2, sticky=tk.NSEW)

        for i, operator in enumerate(('/', '*', '+', '-')):
            btn_operator = tk.Button(self.frm_buttons, text=operator, bg='white', font=('Arial', 20), borderwidth=0, command=lambda x=operator: self._operator_press(x))
            btn_operator.grid(row=i,column=3, sticky=tk.NSEW)

        btn_clear = tk.Button(self.frm_buttons, text='Clear', bg='lightgrey', font=('Arial', 20), borderwidth=0, command=lambda:self._clear())
        btn_clear.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)

    def _digit_press(self, digit):
        if self.obtained_result:
            self.number = ''
            self.expression = ''
            self.lbl_expression.config(text=self.expression)
            self.obtained_result = False
        self.number += str(digit)
        self.lbl_number.config(text=self.number)

    def _operator_press(self, operator):
        if self.obtained_result: self.obtained_result = False
        self.expression += self.number
        self.expression += operator
        self.number = ""
        self.lbl_number.config(text=self.number)
        self.lbl_expression.config(text=self.expression)

    def _evaluate(self):
        self.expression += self.number
        self.lbl_expression.config(text=self.expression)
        try:
            self.number = str(eval(self.expression))
            self.expression = ""
        except Exception:
            self.number = "Error"
        finally:
            self.obtained_result = True
            self.lbl_number.config(text=self.number)

    def _clear(self):
        self.expression =""
        self.number = ""
        self.lbl_number.config(text=self.number)
        self.lbl_expression.config(text=self.expression)

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    window = tk.Tk()

    app = CalculatorApp(window)
    app.run()