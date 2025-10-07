from tkinter import Label, Button, Entry, Tk, Frame, PhotoImage
from tkinter import messagebox
from os import path 
from PIL import Image, ImageTk
import keyboard, time, mouse
from random import randint
running = True
delay = 0

def schedule_click():

    if running:
        mouse.click()
        time.sleep(delay) # затримка між кліками
    schedule_click() # функція знову викликає сама себе

def start_clicker():

    global running, delay # "знаходимо" змінні, що існують поза функцією
    clicks_per_second = int(entry.get())
    delay = 1 / clicks_per_second # рахуємо затримку між кліками
    messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу.")
    running = True

    # Запуск процесу кліків
    schedule_click()

root = Tk()

def exit_app():
    global running
    running = False
    messagebox.showinfo("AutoClicker","Autoclicker stopped \n Thanks for using!")
    root.destroy()

def exit_app_2():
    global running
    running = False
    messagebox.showinfo("AutoClicker","Autoclicker stopped \n Thanks for using!")
    root.destroy()

keyboard.add_hotkey('1+Delete',exit_app)

root.title('C00lgui')
root.geometry('700x500')
root.configure(bg="#000000")

label1 = Label(root, text='AUTOCLICKER',font=('Comic Sans MS',45),fg="#FF0000",bg="#000000",pady=10,padx=5).pack()

label2 = Label(root, text='Clicks per second:',font=('Comic Sans MS',35),fg="#FF0000",bg="#000000",pady=5,padx=5).pack()

entry = Entry(root,font=('Comic Sans MS',25),fg="#000000",bg="#FFFFFF")
entry.pack(pady=5)
frame = Frame(root)
frame.pack()

def click_button_start():
    messagebox.showinfo("AUTOCLICKER", "Autoclicker is working")

def Show_information():
    messagebox.showinfo('How to use AUTOCLICKER', ' 1: Enter number of click per second in Entry \n 2:Press "Start" \n 3: Click "OK" and move your mouse to spot where you want the Autoclicker to click.')

start_button = Button(frame,text='Start', font=('Comic Sans MS',25),fg="#FD0000",bg="#000000",padx=5, command=start_clicker)
start_button.grid(row= 0, column=0)

exit_button = Button(frame,text='Exit', font=('Comic Sans MS',25),fg="#FF0000",bg="#000000",padx=5, command=exit_app_2)
exit_button.grid(row= 0, column=1)

info_Button = Button(frame, text="I",  font=('Comic Sans MS',25), fg="#FF0000",bg="#000000", padx=5, command=Show_information)
info_Button.grid(row=0,column=2)

# path_image = path.join("Module_3","image.png")
# print(path_image)

# image_i = PhotoImage(file=path_image)
# button_i = Button(root, image= image_i, command=show_info)
# button_i.pack()

root.mainloop()
#=тут?) yea давай за мною) okay