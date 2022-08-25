import telebot
from src.Token import Token

token = Token().get()
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    mesg = bot.send_message(message.chat.id,'Привет, {0.first_name}! Для дальнейшей работы с ботом сообщите ваш ник-нейм в instagram ⬇️'.format(message.from_user))
    bot.register_next_step_handler(mesg,test)
    
def test(message):
    d = {'user_name': message.from_user.username, 'chat_id': message.from_user.id, 'instagram': message.text}
    
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = telebot.types.KeyboardButton('Прайс 💵')
    item2 = telebot.types.KeyboardButton('Расписание 🕐')
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Спасибо, {0.first_name}! Чем я могу помочь?'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Прайс 💵':
            bot.send_message(message.chat.id, 'Перманенентный макияж бровей- *250р.* \nДолговременная укладка с окрашиванием и коррекцией - *50р.* \nДолговременная укладка без окрашивания - *30р.* \nОкрашивание и коррекция - *30р.* \nОкрашивание - *20р.* \nКоррекция (пинцет\воск) - *15р.* \nДепиляция верхней губы - *5р.*', parse_mode= "Markdown")
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = telebot.types.KeyboardButton('Август')
            item2 = telebot.types.KeyboardButton('Сентябрь')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Желаете записаться?' , reply_markup = markup)

        elif message.text == 'Расписание 🕐':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = telebot.types.KeyboardButton('Август')
            item2 = telebot.types.KeyboardButton('Сентябрь')
            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'На какой месяц желаете записаться?' , reply_markup = markup)

bot.infinity_polling()