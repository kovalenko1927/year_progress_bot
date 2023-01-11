import telebot
from telebot import types
from progress_bar_mod import progress_bar

bot = telebot.TeleBot('***********************')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    start_button = types.KeyboardButton("/start")
    markup.add(start_button)

    bot.send_message(message.chat.id, f"<b>{progress_bar(prefix = 'Progress:', suffix = 'of the year have already passed!', length = 40)}</>", parse_mode="html", reply_markup=markup)


bot.polling(none_stop=True)
