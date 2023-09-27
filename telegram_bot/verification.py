from telebot import types
import bot_database


def init_bot(message, telegram_bot):
    global bot
    bot = telegram_bot
    verification(message)


def verification(message):
    products = bot_database.verification()
    product_list = products
    if product_list:
        for product in product_list:
            product_id, product_images = product
            main_menu = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(text='Да',
                                              callback_data='verification' + '|' + 'yes' + '|' + str(product_id))
            key2 = types.InlineKeyboardButton(text='Нет',
                                              callback_data='verification' + '|' + 'no' + '|' + str(product_id))
            main_menu.add(key1, key2)

            bot.send_photo(chat_id=message.chat.id, photo=product_images.split(',')[0],
                           caption='Оставляем?\nID: ' + str(product_id),
                           reply_markup=main_menu)

    else:
        bot.send_message(message.chat.id, "Все товары проверифицированы")
