import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import jokes
from random import choice
BOT_TOKEN = '8210652306:AAH7m8M343EtI9wIEJwVmvs_PiMU7TMK2EA'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard =  InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Tell joke", callback_data="get_joke")
    button2 = InlineKeyboardButton("Відкрити сайт", url="https://youtu.be/Uuy5oZeLLgI?si=ELXWu3XyawF3F5Gu")
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, "Обери дію:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "get_joke")
def handle_callback(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, choice(jokes))

bot.polling(none_stop=True, interval=0)