
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "5745521063:AAHMTiEUlPNi2o2Ek2PGhaTdlaRZsS5N6GM"

def start(update: Update, context: CallbackContext) -> None:
    chat_id = str(update.message.chat_id)
    if "api" not in context.user_data:
        update.message.reply_text(
            'Привет, я мастер по бровям Алина, чем я могу Вам помочь?')
        return

def main() -> None:
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()