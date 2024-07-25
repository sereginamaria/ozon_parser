from telebot.types import InputMediaPhoto
from telebot import types
from backend.telegram import bot, config, mass_of_stikers
import random
import io

def send_post(cards_list, json, product_links):
    publication_category = ''.join(json['category'].split())
    if (publication_category == 'ВерхняяОдежда' or publication_category == 'Кофта'):
        caption = ("#" + publication_category + ' #' + json['sub_category'])
    else:
        caption = ("#" + publication_category)

    media_group = [(InputMediaPhoto(io.BytesIO(card), caption = caption if cards_list.index(card) == 0 else ''))
                   for card in cards_list]

    bot.send_media_group(config.CHAT_ID, media=media_group, timeout=120)

    text = ''
    for stiker in random.sample(mass_of_stikers, 4):
        text += stiker
    text += 'ㅤ'

    markup = types.InlineKeyboardMarkup(row_width=3)
    buttons = []
    i = 0
    for product_link in product_links:
        buttons.append(types.InlineKeyboardButton(str(i+1), url='https://www.ozon.ru' + product_link))
        i += 1

    markup.add(*buttons)
    bot.send_message(config.CHAT_ID, text, reply_markup=markup)