import json

from telebot import types
from telebot.types import InputMediaPhoto

import bot_database

def init_bot(message, telegram_bot, info_message):
    global bot
    bot = telegram_bot
    if info_message == 'verification':
        verification(message)
    if info_message == 'change_name':
        change_name(message)


def verification(message):
    # bot.send_message(message.chat.id, 'start')
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

            del1 = types.InlineKeyboardButton(text='Удалить фото 1',
                                              callback_data='verification' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(1))
            del2 = types.InlineKeyboardButton(text='Удалить фото 2',
                                              callback_data='verification' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(2))
            del3 = types.InlineKeyboardButton(text='Удалить фото 3',
                                              callback_data='verification' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(3))
            del4 = types.InlineKeyboardButton(text='Удалить фото 4',
                                              callback_data='verification' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(4))

            main_menu.add(key1, key2, key3, del1, del2, del3, del4)

            if product_images[-1] == ',':
                product_images = product_images[:-1]

            new_product_images = product_images.split(', ')

            if len(new_product_images) < 4:
                # bot.send_message(message.chat.id, 'В базе данных менее 4 фотографий, ')
                new_product_images.append(new_product_images[0])

                new_product_images_list = ', '.join(new_product_images)
                bot_database.post_verification_delete_photo(product_id, new_product_images_list)


            # bot.send_message(message.chat.id, str(new_product_images))

            # media_group = []
            # for num in range(4):
            #     media_group.append(InputMediaPhoto('https://cdn1.ozone.ru/s3/multimedia-b/6822645599.jpg'))
            #     # bot.send_message(message.chat.id, str(media_group))
            # bot.send_media_group(chat_id=message.chat.id, media=media_group)

            # j = type(new_product_images[1])
            # bot.send_message(message.chat.id, str(j))
            #
            # bot.send_message(message.chat.id, new_product_images[1])
            #
            # bot.send_message(message.chat.id, 'https://cdn1.ozone.ru/s3/multimedia-6/6822645630.jpg')
            #
            #
            # k = (new_product_images[1] == 'https://cdn1.ozone.ru/s3/multimedia-6/6822645630.jpg')
            #
            # bot.send_message(message.chat.id, str(k))
            # #
            # bot.send_message(message.chat.id, len(new_product_images[1]))
            # bot.send_message(message.chat.id, len('https://cdn1.ozone.ru/s3/multimedia-6/6822645630.jpg'))
            #

            # for i in new_product_images[3]:
            #     bot.send_message(message.chat.id, ',erdf=' + i)

            media_group = []
            for num in range(4):
                # bot.send_message(message.chat.id, len(new_product_images[num]))
                # bot.send_message(message.chat.id, len('https://cdn1.ozone.ru/s3/multimedia-l/6822645671.jpg'))
                media_group.append(InputMediaPhoto(new_product_images[num]))


            try:

                # bot.send_message(message.chat.id, str(media_group))
                bot.send_media_group(chat_id=message.chat.id, media=media_group)

                bot.send_message(message.chat.id, 'Оставляем?\nID: ' + str(product_id) +
                                       '\nКатегория: #' + product_category +
                                       '\nПодкатегория: #' + sub_category +
                                       '\nИмя: ' + product_name + ' ' +
                                       Warning_name, reply_markup=main_menu)

                # bot.send_message(chat_id=message.chat.id,
                #                caption='Оставляем?\nID: ' + str(product_id) +
                #                        '\nКатегория: #' + product_category +
                #                        '\nПодкатегория: #' + sub_category +
                #                        '\nИмя: ' + product_name + ' ' +
                #                        Warning_name,
                #                reply_markup=main_menu)


                # bot.send_photo(chat_id=message.chat.id, photo=product_images.split(',')[0],
                #            caption='Оставляем?\nID: ' + str(product_id) +
                #                    '\nКатегория: #' + product_category +
                #                    '\nПодкатегория: #' + sub_category +
                #                    '\nИмя: ' + product_name + ' ' +
                #                    Warning_name,
                #            reply_markup=main_menu)

            except:
                bot.send_message(message.chat.id, "Ошибка")
                # bot_database.callback_verification('verification' + '|' + 'no' + '|' + str(product_id))
                bot.send_message(message.chat.id, str(product_id))
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


def delete_photo(message, product_list, del_num, product_id):
    global product_images_del

    # bot.send_message(message.chat.id, '67890-')

    product_images_del = ''.join(product_list[0])

    # bot.send_message(message.chat.id, str(product_images_del))

    if product_images_del[-1] == ',':
        product_images_del = product_images_del[:-1]

    new_product_images_del = product_images_del.split(', ')

    # bot.send_message(message.chat.id, str(new_product_images_del))

    del new_product_images_del[int(del_num)-1]
    new_product_images_list = ', '.join(new_product_images_del)

    # bot.send_message(message.chat.id, str(new_product_images_list))

    bot_database.post_verification_delete_photo(product_id, new_product_images_list)

    verification(message)