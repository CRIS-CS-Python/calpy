from tkinter import *
from tkinter import ttk
import re

def left_to_right_eval(expr):
    # Split numbers and operators
    tokens = re.findall(r'\d+\.?\d*|[+\-*/]', expr.replace(' ', ''))
    if not tokens:
        return "Error"
    try:
        result = float(tokens[0])
        i = 1
        while i < len(tokens) - 1:
            op = tokens[i]
            num = float(tokens[i + 1])
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            elif op == '*':
                result *= num
            elif op == '/':
                result /= num
            else:
                return "Error"
            i += 2
        return result
    except Exception:
        return "Error"

def calculate(*args):
    expr = feet_entry.get()
    result = left_to_right_eval(expr)
    result_var.set(result)

def insert_text(value):
    feet_entry.insert(END, value)

#Size of the window

root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#A frame to input the equation

feet = StringVar()
feet_entry = ttk.Entry(mainframe, textvariable=feet)
feet_entry.grid(column=1, row=1, columnspan=4, sticky=(W, E))

#Text display

result_var = StringVar()
result_label = ttk.Label(mainframe, textvariable=result_var)
result_label.grid(column=4, row=2, sticky=(W, E))

#Button for numbers to create the equation

ttk.Button(mainframe, text="1", command=lambda: insert_text("1")).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="2", command=lambda: insert_text("2")).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="3", command=lambda: insert_text("3")).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="4", command=lambda: insert_text("4")).grid(column=1, row=4, sticky=W)
ttk.Button(mainframe, text="5", command=lambda: insert_text("5")).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="6", command=lambda: insert_text("6")).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="7", command=lambda: insert_text("7")).grid(column=1, row=5, sticky=W)
ttk.Button(mainframe, text="8", command=lambda: insert_text("8")).grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text="9", command=lambda: insert_text("9")).grid(column=3, row=5, sticky=W)
ttk.Button(mainframe, text="0", command=lambda: insert_text("0")).grid(column=2, row=6, sticky=W)

#Button for operators to create the equation

ttk.Button(mainframe , text="÷", command=lambda: insert_text("/")).grid(column=4, row=3, sticky=W)
ttk.Button(mainframe , text="×", command=lambda: insert_text("*")).grid(column=4, row=4, sticky=W)
ttk.Button(mainframe , text="-", command=lambda: insert_text("-")).grid(column=4, row=5, sticky=W)
ttk.Button(mainframe , text="+", command=lambda: insert_text("+")).grid(column=4, row=6, sticky=W)
ttk.Button(mainframe , text="=", command=calculate).grid(column=4, row=7, sticky=W)
ttk.Button(mainframe , text="AC", command=lambda: feet_entry.delete(0, END)).grid(column=1, row=6, sticky=W)
ttk.Button(mainframe , text="Del", command=lambda: feet_entry.delete(len(feet_entry.get())-1, END)).grid(column=1, row=7, sticky=W)
ttk.Button(mainframe , text="x^" , command=lambda: insert_text("**")).grid(column=2, row=7, sticky=W)
ttk.Button(mainframe , text=".", command=lambda: insert_text(".")).grid(column=3, row=6, sticky=W)
ttk.Button(mainframe , text="√ ", command=lambda: insert_text("UNFINISHED")).grid(column=3, row=7, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
