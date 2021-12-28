import telebot
import time

import telegram_send

bot = telebot.TeleBot('5079815623:AAHVa7HEvuNT8M_nH9c2uvDu4tWVaV66O5k')
CHANNEL_NAME = ''
CHANNEL_ID = '-1001698705173'


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Jasur":
        bot.send_message(message.from_user.id, "Sizga mumkin emas uzur")
        bot.send_message(CHANNEL_ID, "Yedi boru lekin")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
