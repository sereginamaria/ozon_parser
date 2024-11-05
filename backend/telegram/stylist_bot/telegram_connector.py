from telebot import types
from telebot import apihelper
from telegram import bot, logger
from telegram.stylist_bot import config

def send_post(card, products, type):
    logger.info('Start send_post')

    caption = '#ОбразДня'

    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    if type == 'ozon':
        for product in products:
            print(product)
            buttons.append(types.InlineKeyboardButton(product.sub_category, url='https://www.ozon.ru' + product.url))
    if type == 'wb':
        for product in products:
            print(product)
            buttons.append(types.InlineKeyboardButton(product.sub_category, url=product.url))

    markup.add(*buttons)

    try:
        bot.send_photo(config.CHAT_ID, photo=card, reply_markup=markup, caption=caption, timeout=120)
        logger.info('End send_post')
        return True
    except apihelper.ApiTelegramException as e:
        logger.warning(f'Произошла ошибка при отправке сообщения: {str(e)}')
        bot.send_message(config.CHAT_ID, 'Произошла ошибка при отправке сообщения в канал')
        return False
