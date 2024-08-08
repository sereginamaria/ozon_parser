from telebot.types import InputMediaPhoto
from telebot import types
from telebot import apihelper
from telegram import bot, config, mass_of_stikers
import random
import io
from telegram import logger

def send_post(cards_list, json, product_links, sub_category):
    logger.info('Start send_post')
    publication_category = ''.join(json['category'].split())
    if (publication_category == 'ВерхняяОдежда' or publication_category == 'Кофта'):
        caption = ("#" + publication_category + ' #' + sub_category)
    else:
        caption = ("#" + publication_category)

    media_group = [(InputMediaPhoto(io.BytesIO(card), caption = caption if cards_list.index(card) == 0 else ''))
                   for card in cards_list]

    text = ''
    for stiker in random.sample(mass_of_stikers, 4):
        text += stiker
    text += 'ㅤ'

    markup = types.InlineKeyboardMarkup(row_width=3)
    buttons = []
    i = 0
    for product_link in product_links:
        buttons.append(types.InlineKeyboardButton(str(i + 1), url='https://www.ozon.ru' + product_link))
        i += 1

    markup.add(*buttons)

    try:
        bot.send_media_group(config.CHAT_ID, media=media_group, timeout=120)
        bot.send_message(config.CHAT_ID, text, reply_markup=markup)
        logger.info('End send_post')
    except apihelper.ApiTelegramException as e:
        logger.warning(f'Произошла ошибка при отправке сообщения: {str(e)}')
        bot.send_message(config.CHAT_ID, 'Произошла ошибка при отправке сообщения в канал')