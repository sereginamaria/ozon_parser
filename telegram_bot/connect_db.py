# подключаем SQLite
import io
import sqlite3 as sl

import requests
import telebot
from telebot import types

bot = telebot.TeleBot('6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og')

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"


def verification(message):
    print('ver')
    print(message.text)

    # открываем файл с базой данных
    con = sl.connect('ozon_product_db.db')

    # выводим содержимое таблицы на экран
    with con:
        data = con.execute("select product_images from ozon_products where product_id >= (select id from offset)")
        for row in data:
            print(str(row))
            new_row = str(row[0]).split(',')
            print(new_row)
            print('row')
            print(row)
            print(row[0])

            mainmenu = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
            key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
            mainmenu.add(key1, key2)
            # bot.send_message(a.chat.id, 'Это главное меню!', reply_markup=mainmenu)

            remote_image = requests.get(new_row[0])
            photo = io.BytesIO(remote_image.content)
            photo.name = 'img.png'
            files = {'photo': photo}

            bot.send_photo(chat_id=message.chat.id, photo=new_row[0],
                           caption = 'messageText', reply_markup = mainmenu)

            # requests.post(
            #     url=telegram_url + '/sendPhoto',
            #     data={'chat_id': 6181726421, 'caption': 'msg_txt', 'reply_markup': mainmenu}, files=files
            # )

            # requests.post("http://127.0.0.1:5000/create_card", str(row))
