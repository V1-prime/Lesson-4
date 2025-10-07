import tkinter as tk
from random import choice
# #1. Вітальне вікно

# Створи просту програму на Tkinter, яка запитує твоє ім'я через віджет Entry.

# Додай кнопку з текстом "Привітатись".

# Коли натиснеш кнопку, програма повинна показувати привітання у Label, наприклад, "Привіт, [ім'я]!".

def greeting_button(entry,label_hello):
    name = entry.get()
    entry.delete(0, tk.END)
    label_hello.config(text= f'Greetings, {name}!')
    
def first():

    root = tk.Tk()
    root.title("buttons and labels")
    root.geometry("500x500")

    entry = tk.Entry(root)
    entry.pack()
    label_hello = tk.Label(root, text='here can be your text: ')
    label_hello.pack()



    button = tk.Button(root, text='Greet...', command = lambda: greeting_button(entry,label_hello))
    button.pack()

    root.mainloop()
    

# 2. Випадкова зміна кольору

# Напиши програму на Tkinter, яка змінює колір фону вікна на випадковий колір, коли натискаєш кнопку.

# Створи список кольорів та використай модуль random, щоб обирати випадкові кольори зі списку.

# Скористайся методом root.config(bg='колір') для зміни кольору фону вікна.

# Вимоги

#  Додай кнопку Button з текстом "Магія (змінити колір)".

#  Створи Label з інструкцією, наприклад, "Натисни кнопку, щоб змінити колір фону!".

root = tk.Tk()
root.title('Changing colour window')
root.geometry('700x700')
colours = ['red','blue','purple','green','white','orange','black','pink','cyan']

frame = tk.Frame(root, bg='black')
frame.pack()
def colour_change():
    root.config(bg = choice(colours))


button = tk.Button(frame, text='Press to change the colour: ',font=('Comic Sans MS',30),fg='yellow',bg='black',command=colour_change)
button.pack()

root.mainloop()

