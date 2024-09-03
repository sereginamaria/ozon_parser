from telegram import bot
from telegram.wb_bot import config


def not_enough_products_in_db(json):
    bot.send_message(config.CHAT_ID, f"Недостаточно товаров в базе данных (WB) для формировния поста для категории: {json['category']}")
