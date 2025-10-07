#                                                          -MONEY CONVECTOR PROGRAM-

from customtkinter import *

# BTC_TO_UAH = 2000000 # Наприклад, 1 BTC = 110 0000 UAH
# ETH_TO_UAH = 112000 # Наприклад, 1 ETH = 112 000 UAH
# USDT_TO_UAH = 41.77 # Наприклад, 1 USDT = 38 UAH

# Set the appearance mode to dark
set_appearance_mode("light")

currency_dict = {'BTC':3486887,
"ETH":81936,
"USDT":41.77,
"UAH" :1,
"CAD":159895,
"USD":117130.90}

#--- Uses dictionary to find the currency of the chosen value, and multiples or divides it by the amount the user input---#
#-----Then prints the amount user input on one side, and the amount of of other value on other side-----#
def convert():
    try:
        amount = float(entry_amount.get())
   
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        amount_in_uah = amount * currency_dict[from_currency]
        converted_amount = amount_in_uah / currency_dict[to_currency]
        result_label.configure(text=f"{amount} {from_currency} = {converted_amount:.4f} {to_currency}")
    except ValueError as e:
        result_label.configure(text=e)
app = CTk()
app.title("Money convector")
app.geometry('400x300')
BTC_FROM_USDT = 117799.76 
ETH = 3541.13
UAH = 41.77
CAD = 159895
USD = 117,130.90
USDT = 1
title_label = CTkLabel(app, text='Money convector',font=('Comic Sans MS', 18), fg_color='lightblue',text_color='black')
title_label.pack(pady=10)


#Where the user input amount of value chosen in first box
entry_amount = CTkEntry(app, placeholder_text='Enter your value')
entry_amount.pack(pady=10)


from_currency_var = StringVar(value='BTC') #First chosen value in 1st box (before user changes it)
from_currency_menu = CTkOptionMenu(app, fg_color='lightblue',text_color='black', variable=from_currency_var, values=['BTC','ETH','USDT','UAH','CAD','USD'])
from_currency_menu.pack(pady=5)
    
to_currency_var = StringVar(value='UAH') #First chosen value in 2nd box (before user changes it)
to_currency_menu = CTkOptionMenu(app, fg_color='lightblue',text_color='black', variable=to_currency_var,values=['BTC','ETH','USDT','UAH','CAD',])
to_currency_menu.pack(pady=5)

conver_button = CTkButton(app,text='Convert', fg_color='lightblue',text_color='black',command=convert)
conver_button.pack(pady=5)

result_label = CTkLabel(app,text="") #No text untill the user asks for result
result_label.pack(pady=10)

app.mainloop()

#ERRORS:

    #Typing letters (example: f, ten): 🔽

# File "c:\Users\Oksana\OneDrive\Desktop\Python project\Module_3\lesson-5.py", line 22, in convert
# amount = float(entry_amount.get())
# ValueError: could not convert string to float: 'f'

    #Typing in symbols (ecample: #, ^): 🔽
 
# File "c:\Users\Oksana\OneDrive\Desktop\Python project\Module_3\lesson-5.py", line 22, in convert
# amount = float(entry_amount.get())
# ValueError: could not convert string to float: '#'

    #Typing in space: 🔽

# File "c:\Users\Oksana\OneDrive\Desktop\Python project\Module_3\lesson-5.py", line 22, in convert
#     amount = float(entry_amount.get())
# ValueError: could not convert string to float: ' '

    #Typing in questions (example: 5 + 6, 10/5): 🔽

# File "c:\Users\Oksana\OneDrive\Desktop\Python project\Module_3\lesson-5.py", line 22, in convert
# amount = float(entry_amount.get())
# ValueError: could not convert string to float: '5 + 6'