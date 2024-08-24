import logging
import sys
import time

import requests

from main_config import BASE_URL
from telegram.wb import bot

# from threading import Thread
# import autoposting
#
# th_1 = Thread(target=autoposting.autop)
# th_1.start()

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, 'Привет')
    # elif message.text == "/get_videos":
    #     requests.get("http://" + BASE_URL + ":5001/create_videos")
    else:
        bot.send_message(message.from_user.id, 'Не понимаю')
while True:
    try:
        bot.polling(none_stop=True, timeout=123)
    except:
        print('bolt')
        logging.error('error: {}'.format(sys.exc_info()[0]))
        time.sleep(5)