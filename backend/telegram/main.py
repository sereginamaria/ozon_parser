import logging
import sys
import time
from telegram import bot

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, 'Привет')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю')
while True:
    try:
        bot.polling(none_stop=True, timeout=123)
    except:
        print('bolt')
        logging.error('error: {}'.format(sys.exc_info()[0]))
        time.sleep(5)