import tkinter as tk
def on_button_click(button):

    pass

# Ð¤ÑƒÐ½ÐºÑ†Ñ–Ñ Ð´Ð»Ñ Ð·Ð¼Ñ–Ð½Ð¸ Ñ‚ÐµÐ¼Ð¸:
def set_theme(theme):

    if theme == "light":

        root.config(bg='white')

        display.config(bg='lightgray', fg='black')

    elif theme == "dark":

        root.config(bg='black')

        display.config(bg='gray', fg='white')

    elif theme == 'green':

        root.config(bg='green')

        display.config(bg='gray',fg='white')

    for button in buttons:

        button.config(bg='lightgray' if theme == "light" else 'darkgray' if theme == "dark" else 'lightblue', fg='black' if theme != "dark" else 'white')

# Ð“Ð¾Ð»Ð¾Ð²Ð½Ðµ Ð²Ñ–ÐºÐ½Ð¾
root = tk.Tk()
root.title("ÐšÐ°Ð»ÑŒÐºÑƒÐ»ÑÑ‚Ð¾Ñ€")
root.geometry("400x600")

display = tk.Entry(root, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ÐšÐ½Ð¾Ð¿ÐºÐ¸ ÐºÐ°Ð»ÑŒÐºÑƒÐ»ÑÑ‚Ð¾Ñ€Ð°
buttons = []
button_texts = [

'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'C', '0', '=', '+'

]

row_val = 1
col_val = 0

# Ð¡Ñ‚Ð²Ð¾Ñ€ÑŽÑ”Ð¼Ð¾ ÐºÐ½Ð¾Ð¿ÐºÐ¸:
for text in button_texts:

    button = tk.Button(root, text=text, font=('Arial', 18), width=5, height=2, command=lambda value=text: on_button_click(value))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    col_val += 1
    if col_val > 3:

        col_val = 0
        row_val += 1

# ÐœÐ•ÐÐ®
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Ð¡Ð²Ñ–Ñ‚Ð»Ð° Ñ‚ÐµÐ¼Ð°", command=lambda: set_theme("light"))
theme_menu.add_command(label="Ð¢ÐµÐ¼Ð½Ð° Ñ‚ÐµÐ¼Ð°", command=lambda: set_theme("dark"))
menubar.add_cascade(label="ÐÐ°Ð»Ð°ÑˆÑ‚ÑƒÐ²Ð°Ð½Ð½Ñ", menu=theme_menu)

root.config(menu=menubar)
root.mainloop()