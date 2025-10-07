import tkinter as tk

buttons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/', '*', '-', '+', '+']
button_texts = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', 'C', '0', '=', '+']
row_val = 1
col_val = 0

theme = ['light', 'dark', 'blue', 'green', 'red']


def on_button_click(text):
    current = display.cget(
        "text")  # cget("text") викликаєтся до віджета і повертає той параметр, який ми йому передамо (width,bg)
    new_text = str(current) + text
    display.configure(text=new_text)


def math_result():
    current = display.cget("text")
    try:
        result = eval(current)
        display.configure(text=result)
    except ZeroDivisionError:
        display.configure(text='Cannot divide by 0')
    except SyntaxError:
        display.configure(text="Don't.")


def clear_display():
    display.configure(text='')


# Create a dictionary of themes. Each theme has a name and a list of colors: [background color, text color].
# You can add more themes by adding a new key with a list of two colors.


# name theme: listColors [root_color, widget_bg_color, widget_text_color]
themes = {
    'light theme': ['white', 'lightgray', 'black'],
    'dark theme': ['black', "#3D3D3D", 'white'],
    'green theme':["#00b828","#3bff6c","#003f10"],
    'red theme':["#b80009","#ff555d","#5E0005"],
    'purple theme':["#a12fff","#c954ff","#600079"],
    'blue theme':["#0011ff","#5590ff","#09003b"],
    'yellow theme':["#ffbb00","#ffef5c","#5a4d00"]
}


def set_theme(colors):  
    root_color = colors[0]
    bg_color = colors[1]
    text_color = colors[2]

    root.config(bg=root_color)
    display.config(bg=bg_color, fg=text_color)

    for button in buttons:
        button.config(bg=bg_color, fg=text_color)
   


root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

display = tk.Label(root, font=('Comic Sans MS', 24), justify='right', bg='gray')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='we')

buttons = []
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*', '1', '2', '3', '-',
    'C', '0', '=', '+']

row_val = 1
col_val = 0

for text in button_texts:
    if text == '=':
        button = tk.Button(root, text=text, font=('Comic Sans MS', 18), width=5, height=2, command=math_result)

    elif text == 'C':
        button = tk.Button(root, text=text, font=('Comic Sans MS', 18), width=5, height=2, command=clear_display)

    else:
        button = tk.Button(root, text=text, font=('Comic Sans MS', 18), width=5, height=2,
                           command=lambda text=text: on_button_click(text))  # передаємо текст кнопці

    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)

# Loop through the themes and add each one as a command to the theme_menu.
# When a theme is selected, it calls the set_theme function with the corresponding colors.
for theme_name in themes:
    theme_menu.add_command(label=theme_name, command=lambda colors=themes[theme_name]: set_theme(colors))

# theme_menu.add_command(label="Light theme", command=lambda: set_theme("light"))
# theme_menu.add_command(label="Dark theme", command=lambda: set_theme("dark"))# Here, you add 2 theme. You need to add all themes, you can create dict themes = {name:[color_bd,text_color]} 
menubar.add_cascade(label="Theme", menu=theme_menu)

root.config(menu=menubar)
root.mainloop()