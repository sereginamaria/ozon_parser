import telebot
from telebot import types
import requests

import sqlite3 as sl

bot = telebot.TeleBot('6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og')

# открываем файл с базой данных
con = sl.connect('ozon_product_db.db', check_same_thread=False)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/get_products_from_page":
        bot.send_message(message.from_user.id, "Введите ссылку на категорию/список страниц с товарами")
        bot.register_next_step_handler(message, get_page_url)
    elif message.text == "/get_product":
        bot.send_message(message.from_user.id, "Введите ссылку на товар")
        bot.register_next_step_handler(message, get_product_url)
    elif message.text == "/verification":
        verification_message(message)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Список команд:")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def get_product_url(message):
    requests.post("http://127.0.0.1:5000/get_product", message.text)
    bot.send_message(message.from_user.id, "Выполнение завершено!")


def get_page_url(message):
    requests.post("http://127.0.0.1:5000/get_products_from_page", message.text)
    bot.send_message(message.from_user.id, "Выполнение завершено!")


def verification_message(message):
    print('ver')
    print(message.text)

    with con:
        products = con.execute(
            "select product_images from ozon_products where product_id >= (select id from offset)")
    for product in products:
        # print(product)
        # print(type(product))
        # print(len(product))
        # print(product[0])
        # print(type(product[0]))
        # product_image = str(product_image[0]).split(',')

        main_menu = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
        main_menu.add(key1, key2)

        bot.send_photo(chat_id=message.chat.id, photo=product[0].split(',')[0], caption='Оставляем?',
                       reply_markup=main_menu)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "yes":
        print()
        with con:
            con.execute("update ozon_products set verification = true where product_id == (select id from offset)")
    elif call.data == "no":
        with con:
            con.execute("delete from ozon_products where product_id == (select id from offset)")
    con.execute("UPDATE offset SET id = id + 1")

bot.polling(none_stop=True, interval=0)

