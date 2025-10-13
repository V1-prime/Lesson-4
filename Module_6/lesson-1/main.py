import os
from customtkinter import CTk, CTkLabel, CTkButton,CTkEntry
# os.mkdir('folder_name') — створює папку;
# os.remove('file_name') — видаляє файл;
# os.rename('old_name', 'new_name') — перейменовує файл чи папку;
# os.listdir('path') — повертає список файлів і папок у вказаній директорії;
# os.path.exists('file_or_folder') — перевіряє, чи існує файл або папка.

# Напиши програму, яка створює папку з назвою "SecretFolder";
# потім додає в неї файл "secret.txt" із текстом "Це таємний файл!"
# і виводить повідомлення: "Таємний сховок створено!".
#
# Перевір, чи справді твій файл створився на твоєму комп'ютері.


my_dir ='secret_folder'
# os.mkdir(my_dir)

file_name = 'Lezus-builder.txt'
#read, write, append
with open(file_name,"w") as file:
    file.write("Hello World\nHello, Varvara!")

with open(file_name,"r") as file:
    for line in file.readlines():
        print(line)

with open(file_name, 'a+') as file:
    file.write("Jetrocket KABOOM")

with open(file_name,"r") as file:
    for line in file.readlines():
        print(line)

# Завдання 1. Записуємо дані в файл
# 📋 Створи програму, яка записує список твоїх улюблених games у файл games.txt.
#
# Підказка. Використовуй режим запису ("w") і додавай кожен фільм у новому рядку.

class Application:
    def __init__(self):
        self.root = CTk()
        self.root.geometry('500x300')
        self.root.title("Your cool app")
        self.inputText = CTkEntry(self.root)
        self.inputText.pack()
        self.saveButton = CTkButton(self.root,text='Save',command=self.save)
        self.saveButton.pack()

    def save(self):
        game = self.inputText.get()
        # записати назву гри в файл
        print(game)

    def app(self):
        self.root.mainloop()

my_app = Application()
#my_app.app()


# Завдання 2 Читаємо текст із файлу
# 📋 У тебе є файл quotes.txt, який містить цитати. Напиши програму, яка...
#
# Читає всі цитати з файлу.
# Виводить лише ті, що містять слово "щастя".
#
# Підказка. Використовуй in або методи рядків, як-от .find()

my_dic = "Quotes"
quotes_name = "quotes.txt"

with open(quotes_name, "w") as file:
    file.write("\nBe yourself; everyone else is already taken. - Oscar Wilde"
               "\nFolks are usually about as happy as they make their minds up to be. - Abraham Lincoln"
               "\nHappiness is not something ready made. It comes from your own actions. - Dalai Lama XIV"
               "\nYou only live once, but if you do it right, once is enough. - Mae West")

with open(quotes_name,"r") as file:
    pass

# Завдання 3. Робота з директоріями
# 📋 Використовуючи модуль os, створи папку my_folder, а всередині неї — ще одну папку sub_folder.
#
# Перевір, чи папка my_folder вже існує. Якщо ні, створи її.
# Виведи список усіх файлів і папок у директорії, в якій ти працюєш.
#
# Підказка. Використовуй методи os.makedirs() і os.listdir().
#
# Завдання 4. Розмір файлу
# 📋 Напиши програму, яка визначає розмір файлу data.txt у байтах. Якщо файл займає більше, ніж 1 КБ, виведи попередження: "Файл занадто великий!".
#
# Підказка. Використовуй метод os.path.getsize().
#
# Завдання 5. Очищення папки
# 📋 Напиши програму, яка видаляє всі .tmp файли з папки temp_data.
#
# Підказка. Використовуй os.listdir() для перевірки файлів і os.remove() для видалення.