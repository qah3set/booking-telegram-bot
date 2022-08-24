from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
from Token import Token

def start(update: Update, context: CallbackContext) -> None:
    chat_id = str(update.message.chat_id)
    if "api" not in context.user_data:
        update.message.reply_text(
            'Привет, я мастер по бровям Алина, чем я могу Вам помочь?')
        return

def main() -> None:
    token = Token().get()
    
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()