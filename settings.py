import tkinter as tk
import ttkbootstrap as ttk
from test import *




if __name__ == "__main__":
    window = ttk.Window(themename= 'journal')
    dic["master"] = window

    window.title("Settings")
    window.geometry('1920x1080')
    #button
    buttons_frame = ttk.Frame(window)
    title_frame = ttk.Frame(window)
    # Ajout des boutons amenant aux différentes pages
    discussion_button = ttk.Button(
        buttons_frame, text="Discussion", command = dic["open_discussion"])
    discussion_button.pack(side='left', pady=30)

    statistic_button = ttk.Button(
        buttons_frame, text="Stats", command= dic["open_stats"])
    statistic_button.pack(side='left', pady=30)

    settings_button = ttk.Button(
        buttons_frame, text="Settings", command= dic["open_settings"], state= 'disabled')
    settings_button.pack(side='left', pady=30)

    presentation_button = ttk.Button(
        buttons_frame, text="Presentation", command= dic["open_presentation"], state= 'disabled')
    presentation_button.pack(side='left', pady=30)
    buttons_frame.pack(side=TOP)

    #label

    title= ttk.Label(master= window, text='Presentation', font="Helvetica 12" +' bold')
    title.pack()

    #input field
    input_frame = ttk.Frame(master=window)
    text = ttk.Label(master=input_frame, text= 'description', font= "Helvetica 12")
    text.pack()
    input_frame.pack(pady=50)
    window.mainloop()
