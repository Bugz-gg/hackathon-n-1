import tkinter as tk
from tkinter import ttk



# (void) -> string
# This function contain the text about our project.

def Description():
    return 'Voici la description de notre projet'

def police():
    return 'Calibri' + sizepolice()

def sizepolice():
    return '24'

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Présentation")
    string = {str : Description, 'plc' : police}
    label = ttk.Label(master= window, text=string[str](), font=string['plc']())
    label.pack()
    window.mainloop()
