# подключаем SQLite
import sqlite3 as sl
import requests

telegram_url = "https://api.telegram.org/bot6449461079:AAFLbOPkGMwVzTmuWBielCBuILSm4xfIeY0"

def add_to_db(product_name, product_price_original, product_price, product_price_with_ozon_card, product_images,
            product_brand_name, product_brand_link, product_rating, product_categories, product_color, product_article,
            product_sizes, product_all_articles, add_date
            ):
    # открываем файл с базой данных
    con = sl.connect('ozon_product_db.db')

    with con:
        # получаем количество таблиц с нужным нам именем
        data = con.execute("select count(*) from sqlite_master where type='table' and name='ozon_products'")
        for row in data:
            # если таких таблиц нет
            if row[0] == 0:
                # создаём таблицу для товаров
                with con:
                    con.execute("""
                        CREATE TABLE ozon_products (
                            product_id INTEGER PRIMARY KEY,
                            product_name TEXT,
                            product_price_original TEXT,
                            product_price TEXT,
                            product_price_with_ozon_card TEXT,
                            product_images TEXT,
                            product_brand_name TEXT,
                            product_brand_link TEXT,
                            product_rating TEXT,
                            product_categories TEXT,
                            product_sizes TEXT,
                            product_color TEXT,
                            product_article TEXT unique on conflict fail,
                            product_all_articles TEXT,
                            add_date DATE,
                            verification BOOLEAN 
                        );
                    """)

        # подготавливаем множественный запрос
        sql = 'INSERT or IGNORE INTO ozon_products (product_name, product_price_original, ' \
              'product_price, product_price_with_ozon_card, product_images,' \
              'product_brand_name, product_brand_link, product_rating, ' \
              'product_categories, product_color, product_article, product_sizes,' \
              'product_all_articles, add_date) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        # указываем данные для запроса
        data = [
            (product_name,
             product_price_original,
             product_price,
             product_price_with_ozon_card,
             product_images,
             product_brand_name,
             product_brand_link,
             product_rating,
             product_categories,
             product_color,
             product_article,
             product_sizes,
             product_all_articles,
             add_date
             )
        ]

        # добавляем с помощью множественного запроса все данные сразу
        with con:
            con.executemany(sql, data)

        print(telegram_url + '/sendMessage?chat_id=6181726421&text=done')
        requests.post(telegram_url + '/sendMessage?chat_id=6181726421&text=done')
        # выводим содержимое таблицы на экран
        # with con:
        #     data = con.execute("SELECT * FROM products")
        #     for row in data:
        #         print(row)