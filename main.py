import telegram
import dbhelper
import commands
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

db = commands.db

def has_numbers(x):
    return any(char.isdigit() for char in x)

def is_question(x):
    if x[-1] == '?':
        return True
    return False


def is_polynom(x):
    """

    :param x: type string
    :return: True if x is polynom and False if it's not
    """
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - i]:
            return False
    return True


def add_item(update, context):
    """

    :param update: telegram.Update
    :param context: telegram.Context
    """
    items = db.get_items(update.message.chat_id)
    if update.message.text not in items:
        if not is_polynom(update.message.text):
            db.add_item(update.message.text, update.message.chat_id)
    else:
        db.delete_item(update.message.text, update.message.chat_id)


def error(update, context):
    """

    :param update: telegram.Update
    :param context: telegram.Context
    """
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """

    main part of the code
    updater.start_polling sends a request for telegram server to listen on events (long polling)
    """
    db.setup()
    updater = Updater("960888759:AAECyatQetOLUPB660SEJfvc8LUdOUffS4A", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', commands.start))
    dp.add_handler(CommandHandler('showitems', commands.show_items))
    dp.add_handler(MessageHandler(Filters.text, add_item))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
