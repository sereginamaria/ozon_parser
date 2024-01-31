from telebot import types
import bot_database


def init_bot(message, telegram_bot, info_message):
    global bot
    bot = telegram_bot
    if info_message == 'verification':
        verification(message)
    if info_message == 'change_name':
        change_name(message)


def verification(message):
    products = bot_database.verification()

    product_list = products
    if product_list:
        for product in product_list:
            product_id, product_images, product_category, sub_category, product_name = product

            Warning_name = ''
            if len(product_name) > 30:
                Warning_name = ('\n'
                                '\nИмя более 30 символов! Рекомендовано изменить имя!')

                new_product_name = product_name[:30]

            # bot.send_message(message.chat.id, product_images.split(',')[0])

            main_menu = types.InlineKeyboardMarkup(row_width = 2)
            key1 = types.InlineKeyboardButton(text='Да',
                                              callback_data='verification' + '|' + 'yes' + '|' + str(product_id))
            key2 = types.InlineKeyboardButton(text='Нет',
                                              callback_data='verification' + '|' + 'no' + '|' + str(product_id))
            key3 = types.InlineKeyboardButton(text='Изменить имя',
                                              callback_data='verification' + '|' + 'change_name' + '|' + str(product_id))
            main_menu.add(key1, key2, key3)

            try:
                bot.send_photo(chat_id=message.chat.id, photo=product_images.split(',')[0],
                           caption='Оставляем?\nID: ' + str(product_id) +
                                   '\nКатегория: #' + product_category +
                                   '\nПодкатегория: #' + sub_category +
                                   '\nИмя: ' + product_name + ' ' +
                                   Warning_name,
                           reply_markup=main_menu)
            except:
                bot.send_message(message.chat.id, "Ошибка")
                bot_database.callback_verification('verification' + '|' + 'no' + '|' + str(product_id))
                continue

    else:
        bot.send_message(message.chat.id, "Все товары проверифицированы")

def init_change_name(message, telegram_bot, data):
    global change_name_data
    change_name_data = data
    init_bot(message, telegram_bot, 'change_name')

def change_name(message):
    product_name = bot_database.verification_change_name(change_name_data)

    # tt = type(product_name)
    # bot.send_message(message.chat.id, product_name)
    # print(product_name)
    # print(type(product_name))
    #
    # print(product_name[0])
    # print(type(product_name[0]))
    #
    new_tt = ''.join(product_name[0])
    #
    print(new_tt)
    print(type(new_tt))


    new_product_name = new_tt[:30]

    print(new_product_name)
    print(type(new_product_name))

    bot.send_message(message.chat.id, 'Название товара (первые 30 символов): ')
    bot.send_message(message.chat.id, new_product_name)
    bot.send_message(message.chat.id, 'Введите новое название товара: ')
    bot.register_next_step_handler(message, get_new_name)

def get_new_name(message):
    bot_database.verification_add_new_name(change_name_data, message.text)

    bot.send_message(message.chat.id, 'Имя изменено!')

    verification(message)

