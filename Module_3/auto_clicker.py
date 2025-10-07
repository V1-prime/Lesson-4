from tkinter import Label, Button, Entry, Tk, Frame, PhotoImage
from tkinter import messagebox
from os import path 
from PIL import Image, ImageTk
import keyboard, time, mouse
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

keyboard.add_hotkey('Ctrl+Return',exit_app)

root.title('Autoclicker')
root.geometry('600x300')
root.configure(bg="#1100ff")

label1 = Label(root, text='AUTOCLICKER',font=('Comic Sans MS',25),fg="#0f9fe2",bg="#000264",pady=10 ).pack()

label2 = Label(root, text='Clicks per second:',font=('Comic Sans MS',15),fg="#0f9fe2",bg="#000264",pady=5).pack()

entry = Entry(root,font=('Comic Sans MS',15),fg="#000000",bg="#FFFFFF")
entry.pack(pady=5)
frame = Frame(root)
frame.pack()

def click_button_start():
    messagebox.showinfo("AUTOCLICKER", "Autoclicker is working")
def show_info():
    pass


start_button = Button(frame,text='Start', font=('Comic Sans MS',15),fg="#38ac55",bg="#00240E",padx=5, command=start_clicker)
start_button.grid(row= 0, column=0)

exit_button = Button(frame,text='Exit', font=('Comic Sans MS',15),fg="#000000",bg="#AD0000",padx=5)
exit_button.grid(row= 0, column=1)


path_image = path.join("Module_3","image.png")
print(path_image)

# image_i = PhotoImage(file=path_image)
# button_i = Button(root, image= image_i, command=show_info)
# button_i.pack()

root.mainloop()