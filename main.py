import telebot
from telebot import types
from Token import Token

token = Token().get()
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    mesg = bot.send_message(message.chat.id,'Привет, {0.first_name}! Для дальнейшей работы с ботом сообщите ваш ник-нейм в instagram ⬇️'.format(message.from_user))
    bot.register_next_step_handler(mesg,test)
    
def test(message):
    d = {'user_name': message.from_user.username, 'chat_id': message.from_user.id, 'instagram': message.text}
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Прайс 💵')
    item2 = types.KeyboardButton('Расписание 🕐')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Спасибо, {0.first_name}! Чем я могу помочь?'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Прайс 💵':
            bot.send_message(message.chat.id, 'Долговременная укладка - 50р. Коррекция бровей - 35р. Перманент бровей - 300р.')
        elif message.text == 'Расписание 🕐':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item3 = types.KeyboardButton('Август')
            item4 = types.KeyboardButton('Сентябрь')
            
            markup.add(item3, item4)

            bot.send_message(message.chat.id, 'На какой месяц желаете записаться?')

bot.infinity_polling()