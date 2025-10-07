import tkinter as tk
root = tk.Tk()
root.title("my program")
root.geometry("400x600")
frame1 = tk.Frame(root,bg='lightblue')
frame1.pack(padx=10,pady=10)


frame2 = tk.Frame(root,bg='lightgreen')
frame2.pack(padx=10,pady=10)


label = tk.Label(frame1, text="Here can be your advertising",font=("Arial",16),fg='blue',bg='green')
label.pack()
entry = tk.Entry(frame1)
entry.pack()


def changeCollor():
    label.configure(bg='red')

def show_text():

    text = entry.get()

    print(f"Введено: {text}")

def on_click_button():
    print("Someone click button")
button = tk.Button(frame2, text="Clich on me!",font=("Arial",16),fg='blue',bg='green',command=changeCollor)
button.pack()




def change_to_yellow():
    label.config(fg="yellow")

button1 = tk.Button(frame2, text="green", font=("Times New Romance",50),fg='white',bg='black',command=change_to_yellow)
button1.pack()


def change_text():
    new_text = entry.get()
    label.config(text=new_text)

button_get_text = tk.Button(frame1, text="get text", font=("Times New Romance",50),fg='black',bg='white',command=change_text)
button_get_text.pack()



root.mainloop()
