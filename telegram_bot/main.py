import json
import os

import telebot
from telebot import types
import requests

import sqlite3 as sl
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

bot = telebot.TeleBot('6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og')

# открываем файл с базой данных
con = sl.connect('ozon_product_db.db', check_same_thread=False)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "/get_products_from_page":
        bot.send_message(message.from_user.id, "Введите название категории для публикации")
        bot.register_next_step_handler(message, get_page_url_message)
        #
        # bot.send_message(message.from_user.id, "Введите ссылку на категорию/список страниц с товарами")
        # bot.register_next_step_handler(message, get_page_url, publication_category)
    elif message.text == "/get_product":
        bot.send_message(message.from_user.id, "Введите ссылку на товар")
        bot.register_next_step_handler(message, get_product_url)
    elif message.text == "/verification":
        verification_message(message)
    elif message.text == "/create_post":
        publishing_platform_message(message)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Список команд:")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def get_page_url_message(message):
    global publication_category
    publication_category = message.text
    bot.send_message(message.from_user.id, "Введите ссылку на категорию/список страниц с товарами")
    bot.register_next_step_handler(message, get_products_from_page_message)


def get_products_from_page_message(message):
    global page_url
    page_url = message.text
    data = {"publication_category": publication_category, "page_url": page_url}
    requests.post("http://127.0.0.1:5000/get_products_from_page", json=data)
    bot.send_message(message.from_user.id, "Выполнение завершено!")


def get_product_url(message):
    requests.post("http://127.0.0.1:5000/get_product", message.text)
    bot.send_message(message.from_user.id, "Выполнение завершено!")


def verification_message(message):
    print(type(message))
    global current_id
    with con:
        products = con.execute(
            "select product_id, product_images from ozon_products where (verification != true) limit 1")
    # print(type(products))
    # print(list(products.fetchall()))
    product_list = products.fetchall()

    if product_list:
        for product in product_list:
            product_id, product_images = product
            current_id = product_id
            # print(product_id)
            # print(product_images)
            # print(type(product_id))
            # print(product_images.split(','))

            # product_image = str(product_image[0]).split(',')

            main_menu = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
            key2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
            main_menu.add(key1, key2)

            bot.send_photo(chat_id=message.chat.id, photo=product_images.split(',')[0],
                           caption='Оставляем?\nАртикул: ' + str(product_id),
                           reply_markup=main_menu)

    else:
        bot.send_message(message.chat.id, "Все товары проверифицированы")


def publishing_platform_message(message):
    main_menu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Вконтакте', callback_data='vk')
    key2 = types.InlineKeyboardButton(text='Телеграмм', callback_data='tg')
    key3 = types.InlineKeyboardButton(text='Инстаграмм', callback_data='inst')
    main_menu.add(key1, key2, key3)
    bot.send_message(message.chat.id, 'Выберите платформу для публикации', reply_markup=main_menu)


def date_of_publication(message):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(message.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)


def create_card_message(message):
    global post_data
    with con:
        product = con.execute(
            "select product_name, product_article, product_sizes, product_price, product_price_with_ozon_card, product_images from ozon_products where verification == true")

    product_list = product.fetchall()

    print(product_list)
    print(type(product_list))

    requests.post("http://127.0.0.1:5000/create_card", json=json.dumps(product_list))

    bot.send_message(message.chat.id, "Выберите нужные карточки")


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def call(call):
    result, key, step = DetailedTelegramCalendar().process(call.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        print(f"Дата публикации: {result}")
        create_card_message(call.message)
        # bot.edit_message_text(f"Вы ввели: {result}",
        #                       c.message.chat.id,
        #                       c.message.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "yes":
        with con:
            con.execute("update ozon_products set verification = true where product_id ==" + str(current_id))
        verification_message(call.message)
    if call.data == "no":
        with con:
            con.execute("delete from ozon_products where product_id == " + str(current_id))
        verification_message(call.message)

    if call.data == "vk":
        print('vk')
        date_of_publication(call.message)
    if call.data == "tg":
        print('tg')
        date_of_publication(call.message)
    if call.data == "inst":
        print('inst')
        date_of_publication(call.message)

bot.polling(none_stop=True, interval=0)
