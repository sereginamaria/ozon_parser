from backend.telegram import bot, config

def not_enough_products_in_db(json):
    bot.send_message(config.CHAT_ID, f"Недостаточно товаров в базе данных для формировния поста для категории: {json['category']}")

def availability_of_products(message):
    bot.send_message(config.CHAT_ID, message)