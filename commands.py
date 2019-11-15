import dbhelper
import telegram

db = dbhelper.DBHelper()


def start(update, context):
    """

    :param update: telegram.Update
    :param context: telegram.Context
    """
    update.message.reply_text('send any text and I will add it to your todo list')


def show_items(update, context):
    """

    :param update: telegram.Update
    :param context: telegram.Context
    """
    items = db.get_items(update.message.chat_id)
    keyboard = [[item] for item in items]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text='your todo stuff', reply_markup=reply_markup)
