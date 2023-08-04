# подключаем SQLite
import sqlite3 as sl

def add_to_db(product_name, product_price_original, product_price, product_price_with_ozon_card, product_images,
              product_brand_name, product_brand_link, product_rating, product_categories, product_color,
              product_article,
              product_sizes, product_all_articles
              ):
    # открываем файл с базой данных
    con = sl.connect('../ozon_product_db.db')
    cursor = con.cursor()

    with con:
        # получаем количество таблиц с нужным нам именем
        data = con.execute("select count(*) from sqlite_master where type='table' and name='offset'")
        for row in data:
            # если таких таблиц нет
            print('нет таблиц смещения')
            if row[0] == 0:
                # создаём таблицу для смещения
                with con:
                    con.execute("""
                        CREATE TABLE offset (
                            id INTEGER PRIMARY KEY
                        );
                    """)

        # подготавливаем множественный запрос
        sql = 'INSERT or IGNORE INTO offset (id) values(0)'
        cursor.execute(sql)

    with con:
        # получаем количество таблиц с нужным нам именем
        data = con.execute("select count(*) from sqlite_master where type='table' and name='ozon_products'")
        for row in data:
            # если таких таблиц нет
            print('нет таблиц товаров')
            print(row[0])
            if row[0] == 0:
                # создаём таблицу для товаров
                print('эсоздае таблицу товаров')
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
                            date_of_publication DATE,
                            publication_category TEXT,
                            publishing_platform TEXT,
                            verification BOOLEAN
                        );
                    """)

        # подготавливаем множественный запрос
        sql = 'INSERT or IGNORE INTO ozon_products (product_name, product_price_original, ' \
              'product_price, product_price_with_ozon_card, product_images,' \
              'product_brand_name, product_brand_link, product_rating, ' \
              'product_categories, product_color, product_article, product_sizes,' \
              'product_all_articles) values(?,?,?,?,?,?,?,?,?,?,?,?,?)'

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
             )
        ]

        # добавляем с помощью множественного запроса все данные сразу
        with con:
            con.executemany(sql, data)



        # выводим содержимое таблицы на экран
        # with con:
        #     data = con.execute("SELECT * FROM products")
        #     for row in data:
        #         print(row)
