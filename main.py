import telebot
import time

import telegram_send

bot = telebot.TeleBot('5079815623:AAHVa7HEvuNT8M_nH9c2uvDu4tWVaV66O5k')
CHANNEL_NAME = ''
CHANNEL_ID = '-1001698705173'

members = [
    {
        'name': 'FERUZBEK',
        'id': 100001
    },
    {
        'name': 'BEKZOD',
        'id': 100002
    },
    {
        'name': 'JASUR',
        'id': 100003
    },
    {
        'name': 'ABDULAZIZ',
        'id': 100004
    },
    {
        'name': 'AZIZ',
        'id': 100005
    },
    {
        'name': 'OTABEK',
        'id': 100006
    },
    {
        'name': 'DIYOR',
        'id': 100007
    },
    {
        'name': 'SHAXZOD',
        'id': 100008
    },
    {
        'name': 'SHUHRAT',
        'id': 100009
    },
    {
        'name': 'JAVOXIR',
        'id': 100010
    },
    {
        'name': 'NAJIYULLOH',
        'id': 100011
    },
    {
        'name': 'DONIYOR',
        'id': 100012
    },
    {
        'name': 'SHAMSIDDIN',
        'id': 100013
    },
    {
        'name': 'ALIAKBAR',
        'id': 100014
    },
    {
        'name': "G'ULOM",
        'id': 100015
    },
    {
        'name': "XASAN",
        'id': 100016
    },
    {
        'name': "XUSAN",
        'id': 100017
    },
    {
        'name': "ULUG'BEK",
        'id': 100018
    },
]


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Please enter your name(UPPERCASE)")
        bot.register_next_step_handler(message, check_name)


def check_name(message):
    global a
    global noww
    for member in members:
        if message.text == member['name']:
            a = True
            noww = member['id']
            bot.send_message(message.from_user.id, f"Hello Mr. {member['name']}.\nThis is your id: \n{member['id']}")
            bot.send_message(message.from_user.id, "Now you can send your Idea")
            bot.register_next_step_handler(message, get_idea)
            break
        else:
            a = False
            continue
    if a == False:
        bot.send_message(message.from_user.id, "Uzur siz klub azosi emassiz")


def get_idea(message):
    bot.send_message(CHANNEL_ID, f"From {noww}\n{message.text}")


bot.polling(none_stop=True, interval=0)
