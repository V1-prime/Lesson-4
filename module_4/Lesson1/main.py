import telebot
import random
BOT_TOKEN = '8210652306:AAH7m8M343EtI9wIEJwVmvs_PiMU7TMK2EA'

bot = telebot.TeleBot(BOT_TOKEN)
# Команда /start: відправляє привітання, коли користувач пише /start
jokes = [
    "What’s the smartest insect? A spelling bee!",
    "How does the ocean say hi? It waves!",
    "What do birds give out on Halloween? Tweets.",
    "What do you call a duck that gets good grades? A wise quacker.",
    "How do billboards talk? Sign language."
    "What do you call a tired bull? A bulldozer.",
    "Why are pizza jokes the worst? They’re too cheesy.",
    "Why did the peanut get into a rocket? He wanted to be an astro-nut!",
    "What did the ghost call his Mum and Dad? His transparents.",
    "How do you talk to a giant? Use big words.",
    "What animal is always at a baseball game? A bat.",
    "What kind of music do mummies listen to? Wrap music.",
    "Why didn’t the lamp sink? It was too light."
        ]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я твій новий бот 😃")

# Команда /help: відправляє повідомлення з підказками
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я можу допомогти тобі з основними командами: /start, /help, /joke, /info")

#jokes
@bot.message_handler(commands=['joke'])
def joke(message):
    bot.reply_to(message, random.choice(jokes))

#info
@bot.message_handler(commands=['info'])
def tell_joke(message):
    bot.reply_to(message, "'/start' is to start talking to the bot \n '/help' to view what you can do with this bot \n '/joke' to hear a really funny joke!")

# Запуск бота
bot.polling()