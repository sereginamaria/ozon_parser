import logging
import sys
import time

import requests

from main_config import BASE_URL
from telegram.stilist_bot import bot

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == "/get_stile":
        requests.get("http://" + BASE_URL + ":5001/wb/get_stile_card")
    else:
        bot.send_message(message.from_user.id, 'Не понимаю')
while True:
    try:
        bot.polling(none_stop=True, timeout=123)
    except:
        print('bolt')
        logging.error('error: {}'.format(sys.exc_info()[0]))
        time.sleep(5)