from telebot import apihelper

from telegram.stylist_bot import bot, logger
from telegram.stylist_bot import config
import random
import io

def send_post(card):
    logger.info('Start send_post')

    try:
        bot.send_photo(config.CHAT_ID, photo=card, timeout=120)
        logger.info('End send_post')
        return True
    except apihelper.ApiTelegramException as e:
        logger.warning(f'Произошла ошибка при отправке сообщения: {str(e)}')
        bot.send_message(config.CHAT_ID, 'Произошла ошибка при отправке сообщения в канал')
        return False
