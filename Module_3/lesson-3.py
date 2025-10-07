from tkinter import Tk, Label, PhotoImage
from random import choice

def on_click(event):
    event.widget.config(text="have been pressed")

root = Tk()
label = Label(root, text='press on me!',bg='lightblue')
label.pack(padx=20, pady=20)

label1 = Label(root, text='Click enter for change color!',bg="#f7f7f7")
label1.pack(padx=20, pady=20)

def change_background_color(event):
    colors = ["#FD5E52", "#33FF57", "#40008A", "#F0E68C", "#FF33A1"]
    event.widget.config(bg=choice(colors))

label.bind('<Button-1>', on_click)


root.bind('<Return>', change_background_color)

root.mainloop()