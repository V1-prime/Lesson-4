import tkinter as tk
from tkinter import messagebox
import mouse
import time
import keyboard

running = False
delay = 0

def start_clicker():

    global running, delay
    clicks_per_second = int(entry.get())
    delay = int(1000 / clicks_per_second) # Розрахунок затримки між кліками
    messagebox.showinfo("Auto Clicker", "Auto Clicker started. Click 'ESC' to stop.")
    running = True

# Запуск процесу кліків
    schedule_click()

def schedule_click():

    if running:

        mouse.click() # Симуляція лівого клацання миші
        root.after(delay, schedule_click) # Запуск кліку через задану затримку

def exit_app():

    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    root.destroy() # Закриття вікна Tkinter

def show_info(event):

    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")


# Основна програма
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x220")
root.configure(bg="#e0f7fa") # Світло-блакитний фон

root.bind('i', show_info)

# Заголовок
title_label = tk.Label(root, text="Auto Clicker", font=("Trebuchet MS", 16, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.pack(pady=10) # Додати відступ

# Мітка для кліків на секунду
label = tk.Label(root, text="Кліків на секунду:", font=("Trebuchet MS", 12), bg="#e0f7fa", fg="#00796b")
label.pack(pady=5)

# Поле введення для кількості кліків на секунду
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Рамка для кнопок
button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30)) # Збільшити відступ знизу

# Кнопка "Почати"
start_button = tk.Button(button_frame, text="Почати", command=start_clicker, bg="#4caf50", fg="white", font=("Trebuchet MS", 12))
start_button.grid(row=0, column=0, padx=10) # Додати горизонтальний відступ

# Кнопка "Вийти"
exit_button = tk.Button(button_frame, text="Вийти", command=exit_app, bg="#f44336", fg="white", font=("Trebuchet MS", 12))
exit_button.grid(row=0, column=1, padx=10) # Додати горизонтальний відступ

# Додати гарячу клавішу для виходу
keyboard.add_hotkey('esc', exit_app)

root.protocol("WM_DELETE_WINDOW", exit_app) # Вихід з програми при закритті вікна
root.mainloop()