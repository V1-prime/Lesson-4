import tkinter as tk
from tkinter import messagebox
import keyboard, time, mouse

root = tk.Tk()
root.title('Deltarune chat')
root.geometry('500x580')
root.config(bg="#97FF9C")

label1 = tk.Label(root, text='Contacts',font=('Comic Sans MS',30),fg="#000000",bg="#007E26",pady=10)
label1.pack(side= tk.TOP, fill='x')

frame_contacts = tk.Frame(root, width=200, height=500, borderwidth=3, bg="#97FF9C", padx=10, pady=10)
frame_contacts.pack(side= tk.LEFT,fill="y")

frame_chat = tk.Frame(root, width=300, height=500, borderwidth=1, bg="#D2FF97", padx=10, pady=10)
frame_chat.pack(side= tk.RIGHT,fill="y")
text_font = 'Comic Sans MS'
def change_font(font):
    entry.configure(font= font)
    
entry= tk.Entry(frame_chat, text='Enter your message:',font=(text_font,15),fg="#000000",bg="#9AFFB8")
entry.pack(side= tk.BOTTOM, padx=5,pady=5)

label2 = tk.Label(frame_chat, text='"Your text"',font=('Comic Sans MS',15),fg="#000000",bg="#88FFAC")
label2.pack(side= tk.RIGHT, pady=10)

label3 = tk.Label(frame_chat, text='"Person`s text"',font=('Comic Sans MS',15),fg="#000000",bg="#88FFAC")
label3.pack(side= tk.TOP, fill='x', pady=20)


button1 = tk.Button(frame_contacts, text='Susie',font=('Comic Sans MS',15),fg="#000000",bg="#8B00C2")
button1.pack(side= tk.TOP,  fill='x', pady=5)

button2 = tk.Button(frame_contacts, text='Kris',font=('Comic Sans MS',15),fg="#000000",bg="#234BFF")
button2.pack(side= tk.TOP,  fill='x', pady=5)

button3 = tk.Button(frame_contacts, text='Ralsei',font=('Comic Sans MS',15),fg="#000000",bg="#00FF55")
button3.pack(side= tk.TOP,  fill='x', pady=5)

button4 = tk.Button(frame_contacts, text='Sans',font=('Comic Sans MS',15),fg="#000000",bg="#88FBFF")
button4.pack(side= tk.TOP,  fill='x', pady=5)

button5 = tk.Button(frame_contacts, text='Pyparus',font=('Comic Sans MS',15),fg="#000000",bg="#FF8888")
button5.pack(side= tk.TOP,  fill='x', pady=5)

button6 = tk.Button(frame_contacts, text='Toriel',font=('Comic Sans MS',15),fg="#000000",bg="#6588BB")
button6.pack(side= tk.TOP,  fill='x', pady=5)

button7 = tk.Button(frame_contacts, text='Roaring Knight',font=('Comic Sans MS',15),fg="#FFFFFF",bg="#000000")
button7.pack(side= tk.TOP,  fill='x', pady=5)

button8 = tk.Button(frame_contacts, text='Rouxls Kaard',font=('Comic Sans MS',15),fg="#FFFFFF",bg="#001AFF")
button8.pack(side= tk.TOP,  fill='x', pady=5)

root.mainloop()