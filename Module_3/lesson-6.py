import tkinter as tk

def simple():
    root = tk.Tk()
    root.title("My app")
    menubar = tk.Menu(root)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Exit", command=root.quit)

    file_menu2 = tk.Menu(menubar, tearoff=0)
    file_menu2.add_command(label="Copy")
    file_menu2.add_command(label="Cut")
    file_menu2.add_command(label="Paste")
    menubar.add_cascade(label="file", menu=file_menu)
    menubar.add_cascade(label="change", menu=file_menu2)
    root.config(menu=menubar)
    root.mainloop()
#simple()

root = tk.Tk()
def change_bg(color):
    root.configure(bg=color)


def application():
  
    root.title('Colour App')
    menubar = tk.Menu(root)
    
    file_menu = tk.Menu(menubar, tearoff=0)
    colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "magenta", "grey"]
    
    for color in colors:
        file_menu.add_command(label=color,command=lambda:change_bg(color))
    # file_menu.add_command(label='Green') 
    # file_menu.add_command(label='Red',command=lambda:change_bg('red'))
    # file_menu.add_command(label='Yellow')
    # file_menu.add_command(label='Orange')
    # file_menu.add_command(label='Purple')
    # file_menu.add_command(label='Blue')

    menubar.add_cascade(label='colors',menu=file_menu)
    root.config(menu=menubar)
    root.mainloop()
application()
def toogle_color_frame(frame):
    if frame.winfo_viewable():
        frame.pack_forget()
    else:
        frame.pack(pady=10)

def app_collor():
    root = tk.Tk()
    root.title("Colors")
    root.geometry('300x300')
    colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "magenta", "grey"]
    color_frame = tk.Frame(root)
    buttons = []
    for i in range(len(colors)):
        color_button = tk.Button(color_frame, bg=colors[i], command=lambda c=colors[i]: root.config(bg=c), width=2,
                                 height=1)
        color_button.grid(row=0, column=i)  # Кнопки укладываются вертикально
        buttons.append(color_button)

    menubar = tk.Menu(root)

    file_menu_color = tk.Menu(menubar, tearoff=0)
    file_menu_color.add_command(label="colors", command=lambda: toogle_color_frame(color_frame))
    menubar.add_cascade(label="view", menu=file_menu_color)
    root.config(menu=menubar)
    root.mainloop()


# app_collor()
