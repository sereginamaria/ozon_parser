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
    bot.send_message(message.chat.id, 'start')
    global error_num
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
                                              callback_data='verification_new' + '|' + 'yes' + '|' + str(product_id))
            key2 = types.InlineKeyboardButton(text='Нет',
                                              callback_data='verification_new' + '|' + 'no' + '|' + str(product_id))
            create = types.InlineKeyboardButton(text='Создать карточку',
                                              callback_data='verification_new' + '|' + 'create_card' + '|' + str(
                                                  product_id))

            key3 = types.InlineKeyboardButton(text='Изменить имя',
                                              callback_data='verification_new' + '|' + 'change_name' + '|' + str(product_id))

            del1 = types.InlineKeyboardButton(text='Удалить фото 1',
                                              callback_data='verification_new' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(1))
            del2 = types.InlineKeyboardButton(text='Удалить фото 2',
                                              callback_data='verification_new' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(2))
            del3 = types.InlineKeyboardButton(text='Удалить фото 3',
                                              callback_data='verification_new' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(3))
            del4 = types.InlineKeyboardButton(text='Удалить фото 4',
                                              callback_data='verification_new' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(4))

            main_menu.add(key1, key2, create, key3, del1, del2, del3, del4)

            if product_images[-1] == ',':
                product_images = product_images[:-1]

            if product_images[-1] == ' ':
                product_images = product_images[:-2]

            new_product_images = product_images.split(', ')

            if len(new_product_images) < 4:
                # bot.send_message(message.chat.id, 'В базе данных менее 4 фотографий')

                new_product_images.append(new_product_images[0])

                new_product_images_list = ', '.join(new_product_images)
                bot_database.post_verification_delete_photo(product_id, new_product_images_list)


            # bot.send_message(message.chat.id, str(new_product_images))

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
                bot.send_message(message.chat.id, str(product_id))

                try:
                    for error_num in range(4):
                        # bot.send_message(message.chat.id, len(new_product_images[error_num]))
                        bot.send_photo(chat_id=message.chat.id, photo=new_product_images[error_num])
                        # bot.send_message(message.chat.id, 'error_num')
                        # bot.send_message(message.chat.id, error_num)
                except:
                    bot.send_message(message.chat.id, 'Ошибка в этом фото')
                    bot.send_message(message.chat.id, str(new_product_images[error_num]))
                    # bot.send_message(message.chat.id, len(new_product_images[error_num]))

                    del new_product_images[error_num]

                    new_product_images.append(new_product_images[0])

                    new_product_images_list = ', '.join(new_product_images)

                    bot_database.post_verification_delete_photo(product_id, new_product_images_list)
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

    if product_images_del[-1] == ' ':
        product_images_del = product_images_del[:-2]

    new_product_images_del = product_images_del.split(', ')

    # bot.send_message(message.chat.id, str(new_product_images_del))

    del new_product_images_del[int(del_num)-1]
    new_product_images_list = ', '.join(new_product_images_del)

    # bot.send_message(message.chat.id, str(new_product_images_list))

    bot_database.post_verification_delete_photo(product_id, new_product_images_list)

    verification(message)

def create_card(message, product_id):
    bot.send_message(message.chat.id, 'Ожидайте...')
    product_list = bot_database.create_verification_test_card(product_id)

    if product_list:
        for product in product_list:
            product_id, product_name, product_article, product_sizes, product_price, product_price_with_ozon_card, product_images, publication_category, product_url = product

            Warning_name = ''
            if len(product_name) > 30:
                Warning_name = ('\n'
                                '\nИмя более 30 символов! Рекомендовано изменить имя!')

                new_product_name = product_name[:30]

            # bot.send_message(message.chat.id, product_images.split(',')[0])

            main_menu = types.InlineKeyboardMarkup(row_width=2)
            key1 = types.InlineKeyboardButton(text='Да',
                                              callback_data='verification_new' + '|' + 'yes' + '|' + str(product_id))
            key2 = types.InlineKeyboardButton(text='Нет',
                                              callback_data='verification_new' + '|' + 'no' + '|' + str(product_id))
            create = types.InlineKeyboardButton(text='Создать карточку',
                                                callback_data='verification_new' + '|' + 'create_card' + '|' + str(
                                                    product_id))

            key3 = types.InlineKeyboardButton(text='Изменить имя',
                                              callback_data='verification_new' + '|' + 'change_name' + '|' + str(
                                                  product_id))

            del1 = types.InlineKeyboardButton(text='Удалить фото 1',
                                              callback_data='verification_new' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(1))
            del2 = types.InlineKeyboardButton(text='Удалить фото 2',
                                              callback_data='verification_new' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(2))
            del3 = types.InlineKeyboardButton(text='Удалить фото 3',
                                              callback_data='verification_new' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(3))
            del4 = types.InlineKeyboardButton(text='Удалить фото 4',
                                              callback_data='verification_new' + '|' + 'delete_photo' + '|' + str(
                                                  product_id) + '|' + str(4))

            main_menu.add(key1, key2, create, key3, del1, del2, del3, del4)

            if product_images[-1] == ',':
                product_images = product_images[:-1]

            if product_images[-1] == ' ':
                product_images = product_images[:-2]

            new_product_images = product_images.split(', ')

            if len(new_product_images) < 4:
                # bot.send_message(message.chat.id, 'В базе данных менее 4 фотографий')

                new_product_images.append(new_product_images[0])

                new_product_images_list = ', '.join(new_product_images)
                bot_database.post_verification_delete_photo(product_id, new_product_images_list)

            bot.send_message(message.chat.id, 'Оставляем?\nID: ' + str(product_id) +
                             '\nКатегория: #' + publication_category +
                             '\nИмя: ' + product_name + ' ' +
                             Warning_name, reply_markup=main_menu)

from datetime import date
from datetime import datetime
import datetime as datetime2

def plan_publication(message, product_id):
    global timesheet
    timesheet = {
        'Monday': {
            "Украшения": '6:00',
            "Корсет": '8:00',
            "Кофта": '10:00',
            "Брюки": '12:00',
            "Топ": '14:00',
            "Платье": '16:00',
            "Пиджак": '18:00',
            "Сумка": '20:00',
        },
        'Tuesday': {
            "Аксессуары": '6:00',
            "Шорты": '8:00',
            "Футболка": '10:00',
            "Кофта": '12:00',
            "Костюм": '14:00',
            "Юбка": '16:00',
            "Блузка": '18:00',
            "Обувь": '20:00',
        },
        'Wednesday': {
            "Украшения": '6:00',
            "Верхняя Одежда": '8:00',
            "Рубашка": '10:00',
            "Платье": '12:00',
            "Пиджак": '14:00',
            "Брюки": '16:00',
            "Топ": '18:00',
            "Сумка": '20:00',
        },
        'Thursday': {
            "Аксессуары": '6:00',
            "Корсет": '8:00',
            "Кофта": '10:00',
            "Юбка": '12:00',
            "Блузка": '14:00',
            "Джинсы": '16:00',
            "Футболка": '18:00',
            "Обувь": '20:00',
        },
        'Friday': {
            "Украшения": '6:00',
            "Купальник": '8:00',
            "Пиджак": '10:00',
            "Брюки": '12:00',
            "Обувь": '14:00',
            "Топ": '16:00',
            "Платье": '18:00',
            "Сумка": '20:00',
        },
        'Saturday': {
            "Домашняя Одежда": '6:00',
            "Верхняя Одежда": '8:00',
            "Рубашка": '10:00',
            "Джинсы": '12:00',
            "Футболка": '14:00',
            "Пиджак": '16:00',
            "Брюки": '18:00',
            "Обувь": '20:00',
        },
        'Sunday': {
            "Украшения": '6:00',
            "Корсет": '8:00',
            "Кофта": '10:00',
            "Топ": '12:00',
            "Платье": '14:00',
            "Костюм": '16:00',
            "Юбка": '18:00',
            "Сумка": '20:00',
        }
    }

    current_date = date.today()
    current_date += datetime2.timedelta(days=1)
    # current_date = date(2024,3,22)
    # dt_string = "2024-03-18"
    # current_date = current_date1.strptime(dt_string, "%Y-%m-%d")
    date_name= current_date.strftime("%A")

    # bot.send_message(message.chat.id, current_date)
    # bot.send_message(message.chat.id, date_name)

    # bot.send_message(message.chat.id, str(type(current_date)))
    # bot.send_message(message.chat.id, str(type(date_name)))

    product_list = bot_database.get_product_by_id(product_id)

    product_id, product_name, product_article, product_images, publication_category, sub_category, product_url, few_photos = '', '', '', '', '', '', '', True

    if product_list:
        for product in product_list:
            product_id, product_name, product_article, product_images, publication_category, sub_category, product_url, few_photos = product

    is_planing = False

    while not is_planing:

        current_date, date_name = while_def(message, publication_category, current_date, date_name)
        # bot.send_message(message.chat.id, 'yes')

        # bot.send_message(message.chat.id, '0')
        # bot.send_message(message.chat.id, publication_category)
        # bot.send_message(message.chat.id, current_date)
        # bot.send_message(message.chat.id, timesheet[date_name][publication_category])

        current_date, date_name, check_list = check_products(message, publication_category, current_date,
                       timesheet[date_name][publication_category], date_name, product_id)

        # bot.send_message(message.chat.id, '1')
        # bot.send_message(message.chat.id, publication_category)
        # bot.send_message(message.chat.id, sub_category)

        if publication_category == 'Верхняя Одежда' or publication_category == 'Кофта':
            is_planing = check_sub_category(message, sub_category, check_list)
            if is_planing == False:
                current_date += datetime2.timedelta(days=1)
                date_name = current_date.strftime("%A")

                # bot.send_message(message.chat.id, 'current_date+1')
                # bot.send_message(message.chat.id, current_date)
                # bot.send_message(message.chat.id, date_name)
        else:
            # bot.send_message(message.chat.id, 'true')
            is_planing = True
    if not few_photos:
        bot.send_message(message.chat.id, 'Публикация запланирована на ' + str(current_date) + ' ' + str(timesheet[date_name][publication_category]))
        bot_database.plane_to_db(product_id, current_date, timesheet[date_name][publication_category], 'tg', 'group')
    else:
        bot_database.plane_if_few_photos(product_id)
    verification(message)

def check_category_in_timesheet(message, publication_category, date_name):
    # bot.send_message(message.chat.id, 'check_category_in_timesheet')
    if publication_category in timesheet[date_name]:
        return True
    else:
        return False

def check_products(message, publication_category, current_date, publication_time, date_name, product_id):
    # bot.send_message(message.chat.id, 'check_products')
    check_list = bot_database.get_check_list(publication_category, current_date, publication_time)

    # bot.send_message(message.chat.id, 'hi')
    # bot.send_message(message.chat.id, len(check_list))

    while len(check_list) == 6:
        # bot.send_message(message.chat.id, 'full check list')

        current_date += datetime2.timedelta(days=1)
        date_name = current_date.strftime("%A")

        # bot.send_message(message.chat.id, 'current_date+1')
        # bot.send_message(message.chat.id, current_date)
        # bot.send_message(message.chat.id, date_name)

        current_date, date_name = while_def(message, publication_category, current_date, date_name)
        check_list = bot_database.get_check_list(publication_category, current_date, timesheet[date_name][publication_category])
    return current_date, date_name, check_list

def check_sub_category(message, product_sub_category, check_list):
    # bot.send_message(message.chat.id, 'check_sub_category')
    # bot.send_message(message.chat.id, str(check_list))
    if len(check_list) > 0:
        for product in check_list:
            product_id, product_name, product_article, product_images, product_url, sub_category = product
            # bot.send_message(message.chat.id, '2')
            # bot.send_message(message.chat.id, product_sub_category)
            # bot.send_message(message.chat.id, sub_category)

            if product_sub_category != sub_category:
                return False
    return  True

def while_def(message, publication_category, current_date, date_name):
    # bot.send_message(message.chat.id, 'while_def')
    while not check_category_in_timesheet(message, publication_category, date_name):
        # bot.send_message(message.chat.id, 'while_def')
        # bot.send_message(message.chat.id, 'no')
        current_date += datetime2.timedelta(days=1)
        date_name = current_date.strftime("%A")
        #
        # bot.send_message(message.chat.id, 'current_date+1')
        # bot.send_message(message.chat.id, current_date)
        # bot.send_message(message.chat.id, date_name)

    return current_date, date_name