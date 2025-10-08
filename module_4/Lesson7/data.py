styles = {"Grandma": 'calm, caring, gentle, wise, kind',
          "Robot": 'accurate, logical, emotionless',
          "Superhero": 'epic, motivating, prideful, kind',
          "Clown": 'joking, humorous, lighthearted, happy',
          "Teacher": 'responsible, strict, serious, mindful'}

mode_value = {"detailed": 200, "short": 50}

COHERE_API_KEY = "5ADH4cjb4Uy0aXNPAN1s2F6n7EAq7TNMc2LxMiI4"

COHERE_API_URL = "https://api.cohere.ai/v1/generate"

BOT_TOKEN = '8030795228:AAElF_we7d1FIxoSizydNLzW_-B2EtkXyqA'

message_help = ("Need help?\nFirstly, choose your style '/style' ('/random' if not sure), they can be listed when typed in '/start'.\n"
"'/mode' Then, choose a mode, speak casually or more into things?\n"
"Afterwards, simply chat with this bot!\n"
"Have fun!")




# def set_mode(message):
#     global RESPONSE_MODE
#     if message.text.lower() == "short":
#         RESPONSE_MODE = "short"
#         bot.reply_to(message, "Mode set: short reply.")
#     elif message.text.lower() == "detailed":
#         RESPONSE_MODE = "detailed"
#         bot.reply_to(message, "Mode set: detailed reply.")
#     else:
#         bot.reply_to(message, "Unknown mode. Try again.")

# bot.reply_to(message, "Choose reply mode: short or detailed.")
# bot.register_next_step_handler(message, set_mode)
# зробити логіку через словники
# def set_style(message):
#     global RESPONSE_STYLE
#     if message.text.lower() == "joking":
#         RESPONSE_STYLE = "humorous"
#         bot.reply_to(message, "Style set: humorous.")
#     elif message.text.lower() == "serious":
#         RESPONSE_STYLE = "serious"
#         bot.reply_to(message, "Style set: serious.")
#     elif message.text.lower() == "grandma":
#         RESPONSE_STYLE = "grandma"
#     else:
#         bot.reply_to(message, "Unknown style. Try again.")
# bot.reply_to(message, "Choose the texting style: \n{dict_to_sting(styles)}")
# bot.register_next_step_handler(message, set_style)
#@bot.message_handler(func= lambda call: True)
# def handle_mode(message):
#     if message.text == "Short":
#         bot.send_message(message.chat.id, "Mode set: short reply.")
#     elif message.text == "Detailed":
#         bot.send_message(message.chat.id, "Mode set: detailed reply.")
#     else:
#         bot.send_message(message.chat.id, "Mode not set, please try again.")


# button1 = InlineKeyboardButton("Grandma", callback_data="Grandma")
# button2 = InlineKeyboardButton("Robot", callback_data="Robot")
# button3 = InlineKeyboardButton("Superhero", callback_data="Superhero")
# button4 = InlineKeyboardButton("Clown", callback_data="Clown")
# button5 = InlineKeyboardButton("Teacher", callback_data="Teacher")

# @bot.message_handler(func= lambda call: True)
# def handle_mode(message):
#     for mode in styles.values():
#         bot.send_message(message.chat.id, f'{mode}')