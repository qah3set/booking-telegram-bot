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
            
        elif message.text == 'Август':
            bot.send_message(message.chat.id, 'Выберите удобный для вас день')
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('1 августа')
            item2 = types.KeyboardButton('2 августа')
            item3 = types.KeyboardButton('3 августа')
            item4 = types.KeyboardButton('4 августа')
            item5 = types.KeyboardButton('5 августа')
            item6 = types.KeyboardButton('6 августа')
            item7 = types.KeyboardButton('7 августа')
            item8 = types.KeyboardButton('8 августа')
            item9 = types.KeyboardButton('9 августа')
            item10 = types.KeyboardButton('10 августа')
            item11 = types.KeyboardButton('11 августа')
            item12= types.KeyboardButton('12 августа')
            item13 = types.KeyboardButton('13 августа')
            item14 = types.KeyboardButton('14 августа')
            item15 = types.KeyboardButton('15 августа')
            item16 = types.KeyboardButton('16 августа')
            item17 = types.KeyboardButton('17 августа')
            item18 = types.KeyboardButton('18 августа')
            item19 = types.KeyboardButton('19 августа')
            item20 = types.KeyboardButton('20 августа')
            item21 = types.KeyboardButton('21 августа')
            item22 = types.KeyboardButton('22 августа')
            item23 = types.KeyboardButton('23 августа')
            item24 = types.KeyboardButton('24 августа')
            item25 = types.KeyboardButton('25 августа')
            item26 = types.KeyboardButton('26 августа')
            item27 = types.KeyboardButton('27 августа')
            item28 = types.KeyboardButton('28 августа')
            item29 = types.KeyboardButton('29 августа')
            item30 = types.KeyboardButton('30 августа')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21,  item22, item23, item24, item25, item26, item27, item28, item29, item30)
            bot.send_message(message.chat.id, 'Желаете записаться?' , reply_markup = markup)

        elif message.text == 'Сентябрь':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('1 сентября')
            item2 = types.KeyboardButton('2 сентября')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Выберите удобный для вас день')


bot.infinity_polling()