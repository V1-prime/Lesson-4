import telebot
from pathlib import Path
from random import choice



BOT_TOKEN = '8030795228:AAElF_we7d1FIxoSizydNLzW_-B2EtkXyqA'
bot = telebot.TeleBot(BOT_TOKEN)
base = Path(__file__).parent

path_audio = base / 'audio'
path_meme = base / 'Memes'

if path_meme.exists():
    print("Папка найдена!")


commands = {'start':"Hello, i can send and save your Meme"}

# function get a path_folder, create list path like:  path_folder/name_file
# and return list paths
def get_paths(path_folder):
    folder = Path(path_folder)
    return [str(file) for file in folder.iterdir() if file.is_file()]


memes = get_paths(path_meme)
 # send memes to user you need to get one meme_path and use in bot.send_photo() тобто потрібно реалізувати функцію
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, i can send and save your Memes")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Having trouble? '/start' is to get bot to work \n '/photo, /video, /audio', one of these will make the bot focus on, when you send whatever you chose of the three \n '/meme' is to get a random meme in your chat \n And '/countMeme' is to make bot count all the memes you have saved, Have fun!")


#TODO
# Change to saving file to list memes
@bot.message_handler(content_types=['photo','video','audio'])
def receive_meme(message):

    if message.photo:
        file_id = message.photo[-1].file_id
        file_name = f'photo_{file_id}.jpg'
    elif message.audio:
        file_id = message.audio.file_id
        file_name = message.audio.file_name if message.audio.file_name else f'track_{file_id}.mp3'

    try:
        file_info = bot.get_file(file_id)
        downloaded_file =bot.download_file(file_info.file_path)

        with open(Path(path_meme / file_name), 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, f'File "{file_name}" downloaded successfully')
    except Exception as e:
        bot.reply_to(message,f'Error downloading file: {e}')
    print(file_name)
    memes.append(file_name)
    bot.send_message(message.chat.id, 'Meme is saved')


@bot.message_handler(commands=['meme'])
def send_random_meme(message):
    if memes:
        meme = choice(memes)
        with open (meme,'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.reply_to(message, "No Memes yet! Please add some now or later!")

# то потім) і так він приймає і відправлю меми, один момент наче я баг зловив) запусти бота кинь йому пару картинок та декілька разів викличи /meme
# it sends only images out of memes folder, it should be like that? а ти нові відправляла?
# i'm sorry i have to go now, i'll come back when i'll get time
@bot.message_handler(commands=['countMeme'])
def info(message):
    bot.reply_to(message, f"count memes: {len(memes)}")


# @bot.message_handler(commands=['help'])
# def send_help(message):
#     pass
# @bot.message_handler(commnads =['gif'])
# def send_gif(message):
#     pass
#     # bot.send_animation(message.chat.id,)

def app():
    bot.polling()

app()
# запустив, перевіряй у тг. Зберігає, подивись в папці картинки) краще певно змінити назву збереження. у папці Memes у мене там 3 показує, це все в середині цього проекту
# i don't see any new images in my "pictures", i send picturesw to bot and it saves where? in pycharm or my folder?