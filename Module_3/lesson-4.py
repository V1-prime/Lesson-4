import tkinter as tk

root = tk.Tk()

# Отримуємо розміри екрана
screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenheight()

# Завдання 2. Напиши програму, яка буде виводити розміри твого екрана у Label.
    
# Розраховуємо нові розміри вікна
new_width = screen_width // 2 # Половина ширини екрану
new_height = screen_height # Вся висота екрану
label = tk.Label(root,text = f"{screen_width}x,{screen_height}").pack()
# Задаємо нові розміри вікна
root.geometry(f"{new_width}x{new_height}")

root.mainloop()