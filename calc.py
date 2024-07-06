import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def _init_(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        self.expression = ""
        self.input_text = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(input_frame, font=("arial", 18, "bold"), textvariable=self.input_text, justify="right")
        input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('sqrt', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(buttons_frame, text=text, font=("arial", 18, "bold"), bd=1, relief="ridge",
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        elif char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char in ('sqrt', 'sin', 'cos', 'tan', 'log'):
            try:
                if char == 'sqrt':
                    result = str(math.sqrt(eval(self.expression)))
                elif char == 'sin':
                    result = str(math.sin(math.radians(eval(self.expression))))
                elif char == 'cos':
                    result = str(math.cos(math.radians(eval(self.expression))))
                elif char == 'tan':
                    result = str(math.tan(math.radians(eval(self.expression))))
                elif char == 'log':
                    result = str(math.log10(eval(self.expression)))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if _name_ == "_main_":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
