import random
import string
import os
   
from bot_logic import gen_pass
from bot_logic import emoji_pass
import telebot
print(os.listdir('images'))
 # Инициализация бота с использованием его токена
bot = telebot.TeleBot("")
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
        bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! Пожалуйста введи команду commands.')
@bot.message_handler(commands=['math'])
def send_math(message):
    # А вот так можно подставить имя файла из переменной
        math = os.listdir('math')
        math_name = random.choice(math) 
        with open(f'math/{math_name}', 'rb') as f:
                bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=['heh'])
def send_heh(message):
        count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
        bot.reply_to(message, "he" * count_heh)
           # Обработчик команды '/start' и '/hello'
                

@bot.message_handler(commands=['proveyourereal'])
def send_proveyourereal(message):
        bot.reply_to(message, "Я настоящий. Повернись.")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    # А вот так можно подставить имя файла из переменной
        images = os.listdir('images')
        img_name = random.choice(images) 
        with open(f'images/{img_name}', 'rb') as f:
                
                bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=['ecomeme'])
def send_ecomeme(message):
    # А вот так можно подставить имя файла из переменной
        ecologymemes = os.listdir('ecologymemes')
        eco_name = random.choice(ecologymemes) 
        with open(f'ecologymemes/{eco_name}', 'rb') as f:
                
                bot.send_photo(message.chat.id, f) 
@bot.message_handler(commands=['angrybirds'])
def send_mem(message):
    # А вот так можно подставить имя файла из переменной
        birds = os.listdir('birds')
        bird_name = random.choice(birds) 
        with open(f'birds/{bird_name}', 'rb') as f:
                
                bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=['ihateyou'])
def send_ihateyou(message):
        bot.reply_to(message, "Это было очень грубо!")

@bot.message_handler(commands=['info'])
def send_info(message):
        bot.reply_to(message, "Я являюсь тестовым ботом студента из школы Kodland!")

@bot.message_handler(commands=['funnyvideo'])
def send_funnyvideo(message):
        bot.reply_to(message, "Если хочешь посмеятся, посмотри https://www.youtube.com/watch?v=hNTiJ5QEhl0&t=3")

@bot.message_handler(commands=['commands'])
def send_commands(message):
        bot.reply_to(message, "Команды: hello, heh, bye, ihateyou, proveyorereal, genpassword, genemoji, mem, info, funnyvideo, angrybirds, ecomeme")

@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока!")
    
@bot.message_handler(commands=['genpassword'])
def send_genpassword(message):
        bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['genemoji'])
def send_genemoji(message):
        bot.reply_to(message, emoji_pass(1))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    


    
    # Обработчик команды '/heh'

    
    # Запуск бота
    
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать

bot.polling()
