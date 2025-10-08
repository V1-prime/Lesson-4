import telebot

#
BOT_TOKEN = '8030795228:AAElF_we7d1FIxoSizydNLzW_-B2EtkXyqA'
bot = telebot.TeleBot(BOT_TOKEN)
extras = ["Chocolate", "Strawberry", "Caramel", "Hot Fudge"]

data_icecream = {'ice cream': ["Vanilla base", "Chocolate base"]}

total = []


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     'Hello! This is Summershack bot order, please enter your name first to label your order: ')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,
                     'Type in your item name to add it to your order \n Type in "image (your item)" to view the picture of the chosen item! \n To remove your item, type in "remove (your item)"!')


# it works kind of weirdly, but it does, when i type in my name is says thanks for the order
# тобто ти пишешь своє ім'я і воно прощається?
# better create dict, where you have user text, and you answer or answers like
# {"bye":["Have a good day",'See u soon', "Bye-bye!)"} та діставати рандомне значення з варіантів, так бот буде більш варіативний, потім ти в перевіряєш чи є репліка користувача в словнику, якщо ні, то можешь запропонувати з'єднати з людиною)


@bot.message_handler(func=lambda message: True)
def handle(message):
    answers = {
        "ice cream": f'I can introduce you {", ".join(map(str, extras))}!',
        "user_text": "answer",
        "image": "not now",
        "my test": 'You can see this text if you know that code)',
        "buy": f' This will be your total {total}!',
        }

    # "Hello i wanna some ice cream"

    user_text = message.text.lower().strip()
    if user_text in answers:
        bot.send_message(message.chat.id, answers[user_text])

    if "ice cream" in user_text or 'order' in user_text:
        bot.send_message(message.chat.id, '')

    if "remove" in user_text:
        bot.send_message(message.chat.id, f'Would you like to remove this item?')
        if "yes" in user_text:
            bot.send_message(message.chat.id, f'This item has been removed from your order.')

    elif 'thank you' in user_text or 'goodbye' in user_text:
        # elif "thank you" or "goodbye" in user_text:
        bot.send_message(message.chat.id,
                         f'We thank you for your order! Have a good day!')

    elif 'goodbye' in user_text:
        bot.send_message(message.chat.id, f'Goodbye, have a great day!')


# Button is cool) i like it really!)


bot.polling()
