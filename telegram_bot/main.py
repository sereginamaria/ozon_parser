import telebot
from telebot import types
import requests

import sqlite3 as sl

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
    with con:
        global products
        products = con.execute(
            "select product_id, product_images from ozon_products where (product_id >= (select id from offset)) and (verification != true) limit 1")
    # print(type(products))
    # print(list(products.fetchall()))
    produst_list = products.fetchall()

    if produst_list:
        for product in produst_list:
            print('1234')
            print(product)
            print(type(product))
            print(len(product))
            product_id, product_images = product
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

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if len(list(products.fetchall())) != 0:
        if call.data == "yes":
            with con:
                con.execute("update ozon_products set verification = true where product_id == (select id from offset)")
        elif call.data == "no":
            with con:
                con.execute("delete from ozon_products where product_id == (select id from offset)")
        with con:
            con.execute("UPDATE offset SET id = id + 1")

        verification_message(call.message)

bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    verification_message("asdasd")
