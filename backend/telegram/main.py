import logging
import sys
import time

import requests

from main_config import BASE_URL
from telegram import bot
from threading import Thread
from telegram.ozon_bot import autoposting as autoposting_ozon
from telegram.wb_bot import autoposting as autoposting_wb

th_ozon = Thread(target=autoposting_ozon.autop)
th_ozon.start()

import time

time.sleep(5)


th_wb = Thread(target=autoposting_wb.autop)
th_wb.start()


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == "/get_videos":
        requests.get("http://" + BASE_URL + ":5001/create_videos")
    else:
        bot.send_message(message.from_user.id, 'Не понимаю')
while True:
    try:
        bot.polling(none_stop=True, timeout=123)
    except:
        print('bolt')
        logging.error('error: {}'.format(sys.exc_info()[0]))
        time.sleep(5)