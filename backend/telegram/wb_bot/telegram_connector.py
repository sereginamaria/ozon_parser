from telebot.types import InputMediaPhoto
from telebot import types
from telebot import apihelper
from telegram import bot, mass_of_stikers, logger
from telegram.wb_bot import config
import random
import io

def send_post(cards_list, json, product_links, unique_sub_categories):
    logger.info('Start send_post')
    publication_category = ''.join(json['category'].split())
    caption = ("#" + publication_category)

    for unique_sub_category in unique_sub_categories:
        if unique_sub_category != publication_category:
            caption += " #" + unique_sub_category

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
        buttons.append(types.InlineKeyboardButton(str(i + 1), url=product_link))
        i += 1

    markup.add(*buttons)

    try:
        bot.send_media_group(config.CHANNEL_ID, media=media_group, timeout=120)
        bot.send_message(config.CHANNEL_ID, text, reply_markup=markup)
        logger.info('End send_post')
        return True
    except apihelper.ApiTelegramException as e:
        logger.warning(f'Произошла ошибка при отправке сообщения: {str(e)}')
        bot.send_message(config.CHAT_ID, 'Произошла ошибка при отправке сообщения в канал')
        return False

def send_video(video):
    bot.send_video(config.CHAT_ID, video, timeout=60)