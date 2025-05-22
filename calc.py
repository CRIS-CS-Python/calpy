from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        expr = feet_entry.get()
        result = eval(expr)
        result_var.set(result)
    except Exception:
        result_var.set("Error")

#Size of the window

root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#A frame to input the equation

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=28, textvariable=feet)
feet_entry.grid(column=1, row=1, sticky=(W, E))

#Text display

result_var = StringVar()
result_label = ttk.Label(mainframe, textvariable=result_var)
result_label.grid(column=1, row=2, sticky=(W, E))

meters = StringVar()

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
