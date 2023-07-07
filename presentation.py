import tkinter as tk
from tkinter import ttk



# (void) -> string
# This function contain the text about our project.

def Description():
    return 'Voici la description de notre projet'

def police():
    return 'Calibri 24'

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Presentation")
    window.geometry('1920x1080')
    string = {str : Description, 'plc' : police}
    #label

    title= ttk.Label(master= window, text='Presentation', font=string['plc']() +' bold')
    title.pack()

    #input field
    input_frame = ttk.Frame(master=window)
    text = ttk.Label(master=input_frame, text= string[str](), font= string['plc']())
    text.pack()
    input_frame.pack(pady=50)
    window.mainloop()
