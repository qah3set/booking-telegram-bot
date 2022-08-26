from email import message
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from src.Token import Token
from src.template.Markup import Markup
from src.template.Month import Month
from src.template.Service import Service
from src.template.Smile import Smile
from src.template.Admin import Admin
from src.template.Text import Text

SERVICE_NUMBERS = [
    Smile.NumberOne.value,
    Smile.NumberTwo.value,
    Smile.NumberThree.value,
    Smile.NumberFour.value,
    Smile.NumberFive.value,
    Smile.NumberSix.value,
    Smile.NumberSeven.value
]
WELCOME_OPTIONS = [
    #Markup.Price.value,
    #Markup.Schedule.value,

]
YES_NO_OPTIONS = [
    Markup.Yes.value,
    Markup.No.value
]

token = Token().get()
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['command'])
def welcome_with_instagram(message: list) -> None:
    username = message.from_user.first_name
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(*WELCOME_OPTIONS)
    message = bot.send_message(
        message.chat.id,
        'Привет, %s! Что хотите сделать?' % (username,),
        reply_markup = markup
    )
    bot.register_next_step_handler(message)

    

#data = [('1', '5501002', 'Долговременная укладка без окрашивания', '40.0', '2022-08-26' '16:00:00'), 
#            ('2', '7447110', 'Перманентный макияж бровей', '60.0', '2022-08-27' '17:00:00')]

bot.infinity_polling()