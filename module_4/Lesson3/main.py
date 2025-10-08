import schedule
import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from random import choice

BOT_TOKEN = '8030795228:AAElF_we7d1FIxoSizydNLzW_-B2EtkXyqA'  # бот токен новий не створювала, правильно? i made a new one
bot = telebot.TeleBot(BOT_TOKEN)
# create inline keybord

users_id = [1552947969]  # 388164104


def send_reminder(user_id, message):
    bot.send_message(user_id, message)


# Заплановані нагадування
for user_id in users_id:
    message = "Programing time! 🤖"
    (schedule.every().wednesday.at("16:55").do(lambda: send_reminder(user_id, message)))
    schedule.every().saturday.at("12:55").do(lambda: send_reminder(user_id, message))
    schedule.every(5).minutes.do(lambda: send_reminder(user_id, message))

    message = "Check on yo CRK/TT streak! 🍪"
    schedule.every().day.at("11:00").do(lambda: send_reminder(lambda: user_id, message))
    schedule.every(5).minutes.do(lambda: send_reminder(user_id, message))

    message = ("DIE OF DEATH! DIE OF DEATH! DIE OF DEATH! DIE OF DEATH! DIE OF DEATH! DIE OF DEATH!"
               "DIE OF DEATH! DIE OF DEATH! DIE OF DEATH! DIE OF DEATH! DIE OF DEATH! DIE OF DEATH! 💥💥💥💥💥💥💥💥💥💥")
    schedule.every().day.at("14:00").do(lambda: send_reminder(user_id, message))
    schedule.every(5).minutes.do(lambda: send_reminder(user_id, message))
    message = "Curtan'Wall 🎶🎼🎧"
    schedule.every().day.at("12:00").do(lambda: send_reminder(user_id, message))
    schedule.every(5).minutes.do(lambda: send_reminder(user_id, message))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Hello, i send you message, when you need this.")
# Основний цикл
while True:

    try:
        schedule.run_pending()
        time.sleep(1)

    except Exception as e:
        print(f"Помилка: {e}")
        time.sleep(5)

# IDEAS LIST:
# 1: Reminder for small things you keep forgetting (ex: grab glasses when going outside during summer,
# or check on the game to get the every-day rewards)
# 2: Reminding about homework, and add 'lamba' so it keeps repeating until you get annoyed and do it
# 3: Reminding to do chores, shower, and etc
# 4: Tell good and encouraging words when you're in a period you don't feel well (ex: depression, sickness,
# loneliness, #etc)
# 5: Reminder to do your activities, hobbies, and just go outside
