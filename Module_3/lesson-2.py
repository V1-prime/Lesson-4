import tkinter as tk
from random import randint

root = tk.Tk()
root.title('MY PROGRAM')
root.geometry('500x400')

label1 = tk.Label(root, text='Label 1',font=('Arial',25),fg='white',bg='cyan')
label1.pack(fill='x')

label2 = tk.Label(root, text='Label 2',font=('Arial',25),fg='black',bg='green')
label2.pack(fill= 'x',padx=5,pady=5)

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  

def change_welcome():
    rgb = _from_rgb((randint(0,255), randint(0,255),randint(0,255)))
    label1.config(text ='Just wasted your time lol' , bg = rgb)
    
button1 = tk.Button(root, text='Button 1',font=('Caveat',15),fg='black',bg='yellow',command=change_welcome)
button1.pack(side= tk.LEFT,fill="y", padx=5,pady=5)

button2 = tk.Button(root, text='Button 2',font=('Caveat',15),fg='black',bg='red',command=change_welcome)
button2.pack(side= tk.RIGHT, fill="y", padx=5, pady=5)# TOP, tk.BOTTOM, LEFT, RIGHT

label3 = tk.Label(root, text='Label 3', font=('Arial',15),fg='pink',bg='gray')
label3.pack(side= tk.BOTTOM,fill='x',padx=10,pady=10)

root.mainloop()




# # #Створення головного вікна simple grid 

#from  tkinter  import Tk, Label, Button, Entry

root = tk.Tk()
root.title("Практика з grid")
root.configure(bg="white")

# # Додавання міток
# Label(root, text="Текст 1", bg="lightgreen", font=14, padx=20, pady=10).grid(row= 0, column=0)
# Label(root, text="Текст 2", bg="lightblue", font=14, padx=20, pady=10).grid(row=0, column= 1)
# Label(root, text="Текст 3", bg="salmon", font=14, padx=20, pady=10).grid(row=1, column=0, columnspan= 2)

# # Додавання кнопок
# Button(root, text="Кнопка 1", bg="orange", fg="white", font=14, width=15).grid(row=2, column=0)
# Button(root, text="Кнопка 2", bg="blue", fg="white", font=14, width=15).grid(row=2, column=1)

# # Запуск головного циклу
# #root.mainloop()

# #from  tkinter  import Tk, Label, Button, Entry

# # Створення головного вікна
# root = Tk()
# root.title("Приклад place")
# root.geometry("400x300") # Ширина x Висота

# # Додавання лейблів
# Label(root, text="Мітка 1", width=15, height=2, font=("Arial", 14)).place(x=20, y=50)
# Label(root, text="Мітка 2", width=15, height=2, font=("Arial", 14)).place(relx=0.5, rely=0.2,  anchor="center")
# Label(root, text="Мітка 3", width=15, height=2, font=("Arial", 14)).place(x=150, y=100)

# # Додавання поля введення
# Entry(root, width=20, font=("Arial", 14)).place(relx=0.5, rely=0.5, anchor="center") # Центровано по відношенню до вікна

# # Додавання кнопок
# Button(root, text="Кнопка 1", width=15, font=("Arial", 14)).place(x=50,y=200)
# Button(root, text="Кнопка 2", width=15, font=("Arial", 14)).place(relx=0.5,rely=0.7, anchor="center")

# Запуск головного циклу
#root.mainloop()