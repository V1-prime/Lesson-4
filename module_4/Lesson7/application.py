import telebot
import requests
from random import choice
from data import *
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(BOT_TOKEN)
RESPONSE_MODE = 'short'
RESPONSE_STYLE = 'Grandma'

#GET list name button
#DO searches through the list/s and creates each 'item' a button (can be added more)
#return markup with buttons
def createInileMarkup(list):
    markup = InlineKeyboardMarkup()
    for name in list:
        markup.add(InlineKeyboardButton(name, callback_data=name))
    return markup

style_mode_markup = createInileMarkup(styles.keys())
mode_markup = createInileMarkup(mode_value.keys())

# alphabet = ["a", "b", "c", "d"]
# alphabet_markup = createInileMarkup(alphabet)
#
# @bot.message_handler(commands=['test'])
# def test_button(message):
#     bot.send_message(message.chat.id,'',reply_markup=alphabet_markup)


@bot.message_handler(commands=["style"])
def select_style(message):
    bot.send_message(message.chat.id, "Hey! Select your style", reply_markup=style_mode_markup)

@bot.message_handler(commands=["mode"])
def select_mode(message):
    bot.send_message(message.chat.id, "Hey! Select your mode", reply_markup=mode_markup)

# GET dictionary items and it's values/keys
# DO searches through the dictionary and gives key and it's value/s
# RETURN lines with a key and a value
def dict_to_sting(dict):
    lines = ""
    for key, value in dict.items():
        lines = lines + f"{key} : {value}\n"
    return lines

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     f'Hello!\nI use AI agent COHERE to answer and talk with you, and i think you`d like to change '
                     f'the style to your own liking right now! Which are:\n{dict_to_sting(styles)}')

@bot.message_handler(commands=['random'])
def send_random(message):
    global RESPONSE_STYLE
    RESPONSE_STYLE = choice([*styles])
    bot.send_message(message.chat.id, RESPONSE_STYLE)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, message_help)

# GET API key code
# DO makes style and mode response and brainstorms it
# RETURN response with specific lenght/long or short response is and what mode and style were chosen
def generate_text(prompt):
    max_token = mode_value[RESPONSE_MODE]

    headers = {
        "Authorization": f"Bearer {COHERE_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "command",
        "prompt": f'Make this answer {styles[RESPONSE_STYLE]}  {prompt}',
        "max_tokens": max_token,
        "temperature": 0.8,
        "p": 0.75,
        "k": 0
    }
    try:
        response = requests.post(COHERE_API_URL, json=data, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            generation = response_data['generations'][0]['text']
            return generation
    except Exception as e:
        return e


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id
    user_choice = call.data.split(" ")[0]
    if user_choice in styles.keys():
        global RESPONSE_STYLE
        RESPONSE_STYLE = styles[user_choice]
    elif user_choice in mode_value.keys():
        global RESPONSE_MODE
        RESPONSE_MODE = mode_value[user_choice]

@bot.message_handler(func=lambda message: True)
def handle(message):  # 'some txt'
    user_text = message.text.lower().strip()
    bot.reply_to(message, "Generate answers... ")
    answerAI = generate_text(user_text)
    bot.send_message(message.chat.id, answerAI)


bot.polling()
