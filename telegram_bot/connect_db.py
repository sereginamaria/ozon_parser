# подключаем SQLite
import sqlite3 as sl
import requests

def verification(message):
    print('ver')
    print(message.text)

    # открываем файл с базой данных
    con = sl.connect('ozon_product_db.db')

    # выводим содержимое таблицы на экран
    with con:
        data = con.execute("select product_images from ozon_products where product_id >= (select id from offset)")
        for row in data:
            print(row)
            print(type(row))
            print(str(row))
            print(type(str(row)))
            requests.post("http://127.0.0.1:5000/card_creator", str(row))
