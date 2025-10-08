import telebot
#
BOT_TOKEN = '8030795228:AAElF_we7d1FIxoSizydNLzW_-B2EtkXyqA'  # бот токен новий не створювала, правильно? i made a new one
bot = telebot.TeleBot(BOT_TOKEN)
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id,message.text)
bad_words = ["first", "second", ""]

user_message = "Привіт, прИвіт, як твої сПрави "


# return True
def check_not_valid_message(message):
    pass


user_words = user_message.split(" ")

for word in user_words:
    if word.lower() in bad_words:
        print(word)


def baned(user):
    print("Ban ", user)


# bot.polling()

students = "'Андрій', 'Олена', 'Микола', 'Світлана', 'Юлія', 'Дмитро', Varvara"

studentz = students.split(", ")

half = len(students) // 2

first_part = students[0:half]
second_part = studentz[half: len(students) + 1]
# print(students)
# print(first_part)
# print(second_part)
#
# Команда 1: ['Андрій', 'Олена', 'Микола']
#
# Команда 2: ['Світлана', 'Юлія', 'Дмитро']

#task2
dates = "25.12.2021, 01.01.2020, 5.15.2023"
                                #  01 2 34 5 6789                   5678
#['25.12.2021', '01.01.2020', '5.15.2023']
years = []
def get_last_char(text,count_last_char):
    dates_splits = text.split(", ")
    for data in dates_splits:
        last_idx = len(data)
        years.append(data[last_idx-count_last_char:last_idx])
    # data_list = data.split('.')#[25,12,2021]
    # years.append(data_list[2])



#task3
URL = "https://example.com?page=5&sort=asc&filter=new"

def separate_link(link):
    return link.split("?")[1].split("&")

print(separate_link(URL))