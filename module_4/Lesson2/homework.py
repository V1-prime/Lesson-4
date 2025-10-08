import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from data import jokes
from random import choice
BOT_TOKEN = '8030795228:AAElF_we7d1FIxoSizydNLzW_-B2EtkXyqA' #бот токен новий не створювала, правильно? i made a new one
bot = telebot.TeleBot(BOT_TOKEN)
# create inline keybord
keyboardInline = InlineKeyboardMarkup(row_width=1)
button = InlineKeyboardButton(text="This is inline-button!", callback_data='btn_types1') #забули де що oh
keyboardInline.add(button)

# create reply keybord
keyboardRp= ReplyKeyboardMarkup(resize_keyboard= True)
button2 = KeyboardButton("Button has been pressed!")
keyboardRp.add(button2)

@bot.message_handler(commands= ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "text", reply_markup=keyboardInline)

@bot.message_handler(commands=['test'])
def send_buttonRP(message):
    bot.send_message(message.chat.id,"do your choice",reply_markup=keyboardRp)

# https://ru.stackoverflow.com/questions/1497471/telebot-inline-buttons 

# https://youtu.be/79DijItQXMM?si=ZFs9WaNVZK_ZMvVw Your Welcome! 
@bot.callback_query_handler(func=lambda call:True) # 
def reply_button(call):
    if call.data == 'btn_types1':# Джанго вільний?)
        bot.send_message(call.message.chat.id,"some text", reply_markup=keyboardInline) 

@bot.message_handler(func=lambda message: True)
def check_user_message(message):
    user_message = message.text
    if  user_message =="Button has been pressed!":
        bot.send_message(message.chat.id," don't click this again)")


bot.polling(none_stop=True, interval=0)