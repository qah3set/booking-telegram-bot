import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from src.Token import Token
from src.template.Markup import Markup
from src.template.Month import Month
from src.template.Service import Service
from src.template.Smile import Smile
from src.template.Admin import Admin


token = Token().get()
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['admin'])
def enter_admin_dashboard(message: list) -> None:
    if message.from_user.id not in [admin.value for admin in Admin]:
        message = bot.send_message(
            message.chat.id,
            'У вас не хватает прав для выполнения данной команды'
        )
        return

    message = bot.send_message(
        message.chat.id,
        'привет админ'
    )
        
@bot.message_handler(commands=['start'])
def welcome(message: list) -> None:
    # TODO: create user if doesnt exist
    username = message.from_user.first_name
    message = bot.send_message(
        message.chat.id,
        'Привет, %s! Для дальнейшей работы с ботом сообщите ваш ник-нейм в instagram. Например: @alina_desyukevich' % (username,)
    )
    bot.register_next_step_handler(message, instagram_account)
    
def welcome_with_instagram(message: list) -> None:
    username = message.from_user.first_name
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(
        KeyboardButton(Markup.Price.value),
        KeyboardButton(Markup.Schedule.value)
    )
    message = bot.send_message(
        message.chat.id,
        'Привет, %s! Что хотите сделать?' % (username,),
        reply_markup = markup
    )
    bot.register_next_step_handler(message, instagram_account)
    
def instagram_account(message: list) -> None:
    # TODO: make validation for english characters
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(
        KeyboardButton(Markup.Price.value),
        KeyboardButton(Markup.Schedule.value)
    )
    
    bot.send_message(
        message.chat.id, 
        'Спасибо, {0.first_name}! Чем я могу помочь?'.format(message.from_user), reply_markup = markup
    )
    
    bot.register_next_step_handler(message, menu)
    
def menu(message) -> None:
    if message.text == '/start':
        welcome(message)
        return
    
    if message.text not in [
        Markup.Price.value,
        Markup.Schedule.value
    ]:    
        markup = ReplyKeyboardMarkup(resize_keyboard = True)
        markup.add(
            KeyboardButton(Markup.Price.value),
            KeyboardButton(Markup.Schedule.value)
        )
        
        bot.send_message(
            message.chat.id, 
            'Недопустимый ввод, выберите, пожалуйста, вариант из списка', reply_markup = markup
        )
        bot.register_next_step_handler(message, menu)
        return
        
    if message.text == Markup.Price.value:
        services_info = [service.value for service in Service]
        text = map(
            lambda service : service['name'] + ' - *' + str(service['price']) + 'р.*', 
            services_info
        )
        bot.send_message(
            message.chat.id, 
            '\n'.join(text),
            parse_mode = 'Markdown'
        )
        
        markup = ReplyKeyboardMarkup(resize_keyboard = True)
        markup.add(
            'Да',
            'Нет'
        )
        bot.send_message(
            message.chat.id, 
            'Желаете записаться?', 
            reply_markup = markup
        )
        
        bot.register_next_step_handler(message, make_appointment)
    else:
        services = [service.value['name'] for service in Service]
        # TODO: refactor with array_diff
        beaufied_numbers = [
            Smile.NumberOne.value,
            Smile.NumberTwo.value,
            Smile.NumberThree.value,
            Smile.NumberFour.value,
            Smile.NumberFive.value,
            Smile.NumberSix.value,
            Smile.NumberSeven.value
        ]
        text = [beaufied_numbers[i] + ' ' + service for i, service in enumerate(services)]
        markup = ReplyKeyboardMarkup(resize_keyboard = True)
        markup.add(*beaufied_numbers)
            
        bot.send_message(
            message.chat.id, 
            'Выберите номер услуги из списка\n' + \
                '\n'.join(text),
            reply_markup = markup
        )
        
        bot.register_next_step_handler(message, service_choose)
        
def make_appointment(message: list) -> None:
    if message.text not in ['Да', 'Нет']:
        markup = ReplyKeyboardMarkup(resize_keyboard = True)
        markup.add(
            'Да',
            'Нет'
        )
        bot.send_message(
            message.chat.id, 
            'Недопустимый ввод, выберите, пожалуйста, вариант из списка', reply_markup = markup
        )
        bot.register_next_step_handler(message, make_appointment)
        return
        
    if message.text.lower() == 'да':
        services = [service.value['name'] for service in Service]
        # TODO: refactor with array_diff
        beaufied_numbers = [
            Smile.NumberOne.value,
            Smile.NumberTwo.value,
            Smile.NumberThree.value,
            Smile.NumberFour.value,
            Smile.NumberFive.value,
            Smile.NumberSix.value,
            Smile.NumberSeven.value
        ]
        text = [beaufied_numbers[i] + ' ' + service for i, service in enumerate(services)]
        markup = ReplyKeyboardMarkup(resize_keyboard = True)
        markup.add(*beaufied_numbers)
            
        bot.send_message(
            message.chat.id, 
            'Выберите номер услуги из списка\n' + \
                '\n'.join(text),
            reply_markup = markup
        )
        
        bot.register_next_step_handler(message, service_choose)
    else:
        welcome_with_instagram(message)
        
def service_choose(message: list) -> None:
    if message.text not in [
        Smile.NumberOne.value,
        Smile.NumberTwo.value,
        Smile.NumberThree.value,
        Smile.NumberFour.value,
        Smile.NumberFive.value,
        Smile.NumberSix.value,
        Smile.NumberSeven.value
    ]:
        services = [service.value['name'] for service in Service]
        # TODO: refactor with array_diff
        beaufied_numbers = [
            Smile.NumberOne.value,
            Smile.NumberTwo.value,
            Smile.NumberThree.value,
            Smile.NumberFour.value,
            Smile.NumberFive.value,
            Smile.NumberSix.value,
            Smile.NumberSeven.value
        ]
        text = [beaufied_numbers[i] + ' ' + service for i, service in enumerate(services)]
        markup = ReplyKeyboardMarkup(resize_keyboard = True)
        markup.add(*beaufied_numbers)
            
        bot.send_message(
            message.chat.id, 
            'Выберите номер услуги из списка\n' + \
                '\n'.join(text),
            reply_markup = markup
        )
        
        bot.register_next_step_handler(message, service_choose)
        return
        
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(
        Month.August.value,
        Month.September.value
    )
    bot.send_message(
        message.chat.id, 
        'Выберите месяц для записи', 
        reply_markup = markup
    )
    bot.register_next_step_handler(message, month_choose)

def month_choose(message: list) -> None:
    if message.text not in [
        Month.August.value,
        Month.September.value
    ]:
        markup = ReplyKeyboardMarkup(resize_keyboard = True)
        markup.add(
            Month.August.value,
            Month.September.value
        )
        bot.send_message(
            message.chat.id, 
            'Недопустимый ввод, выберите, пожалуйста, вариант из списка', reply_markup = markup
        )
        bot.register_next_step_handler(message, month_choose)
        return
        
    day = 'августа' if message.text == Month.August.value else 'сентября'
    formatted_days = [str(i + 1) + ' ' + day for i in range(30)]
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(*formatted_days)
        
    bot.send_message(
        message.chat.id, 
        'Выберите удобный для вас день', 
        reply_markup = markup
    )
    bot.register_next_step_handler(message, day_choose)
    
def day_choose(message: list) -> None:
    # TODO: validate chosen day
    time = ['15:30', '16:30', '17:30']
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(*time)
        
    bot.send_message(
        message.chat.id, 
        'Выберите удобное время', 
        reply_markup = markup
    )
    bot.register_next_step_handler(message, validate_booking)
    
def validate_booking(message: list) -> None:
    # TODO: validate chosen time
    # TODO: validate all chosen user data and ask a question
    options = ['Да', 'Нет']
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(*options)
    
    chosen_data = [
        'Услуга: перманент',
        'Стоимость: 40р',
        'Дата: 29.08.2022 15:30'
    ]

    bot.send_message(
        message.chat.id,
        'Данные о записи:\n' + '\n'.join(chosen_data) + '\nВсе ли правильно?',
        reply_markup = markup
    )
    bot.register_next_step_handler(message, booking_success)
    
def booking_success(message: list) -> None:
    # TODO: validate no answer
    bot.send_message(
        message.chat.id,
        'Запись сохранена, ожидайте, за 24ч до сеанса с Вами свяжутся для подтверждения.'
    )
    welcome_with_instagram(message)

bot.infinity_polling()