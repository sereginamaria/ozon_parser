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
            product_id, product_images, sub_category = product

            # bot.send_message(message.chat.id, product_images.split(',')[0])

            main_menu = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(text='Да',
                                              callback_data='verification' + '|' + 'yes' + '|' + str(product_id))
            key2 = types.InlineKeyboardButton(text='Нет',
                                              callback_data='verification' + '|' + 'no' + '|' + str(product_id))
            # key2 = types.InlineKeyboardButton(text='Изменить имя',
            #                                   callback_data='verification' + '|' + 'change_name' + '|' + str(product_id))
            main_menu.add(key1, key2)

            try:
                bot.send_photo(chat_id=message.chat.id, photo=product_images.split(',')[0],
                           caption='Оставляем?\nID: ' + str(product_id) +
                                   '\nКатегория: #' + sub_category,
                           reply_markup=main_menu)
            except:
                bot.send_message(message.chat.id, "Ошибка")
                bot_database.callback_verification('verification' + '|' + 'no' + '|' + str(product_id))
                continue

    else:
        bot.send_message(message.chat.id, "Все товары проверифицированы")
