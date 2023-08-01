# # подключаем SQLite
# import sqlite3 as sl
#
# def connect(product_name, product_price_original, product_price, product_price_with_ozon_card, product_images,
#             product_brand_name, product_brand_link, product_rating, product_categories, product_color, product_article,
#             product_sizes, product_all_articles
#
#             ):
#     # print('connect name')
#     # print(product_name)
#     # открываем файл с базой данных
#     con = sl.connect('product_db.db')
#
#     with con:
#         # получаем количество таблиц с нужным нам именем
#         data = con.execute("select count(*) from sqlite_master where type='table' and name='products'")
#         for row in data:
#             # если таких таблиц нет
#             if row[0] == 0:
#                 # # создаём таблицу для товаров
#                 # with con:
#                 #     con.execute("""
#                 #         CREATE TABLE products (
#                 #              product_name TEXT PRIMARY KEY
#                 #         );
#                 #     """)
#
#                 # создаём таблицу для товаров
#                 with con:
#                     con.execute("""
#                         CREATE TABLE products (
#                             product_id INTEGER PRIMARY KEY,
#                             product_name TEXT,
#                             product_price_original TEXT,
#                             product_price TEXT,
#                             product_price_with_ozon_card TEXT,
#                             product_images TEXT,
#                             product_brand_name TEXT,
#                             product_brand_link TEXT,
#                             product_rating TEXT,
#                             product_categories TEXT,
#                             product_sizes TEXT,
#                             product_color TEXT,
#                             product_article TEXT unique on conflict fail,
#                             product_all_articles TEXT
#                         );
#                     """)
#
#         # подготавливаем множественный запрос
#         sql = 'INSERT or IGNORE INTO products (product_name, product_price_original, ' \
#               'product_price, product_price_with_ozon_card, product_images,' \
#               'product_brand_name, product_brand_link, product_rating, ' \
#               'product_categories, product_color, product_article, product_sizes,' \
#               'product_all_articles) values(?,?,?,?,?,?,?,?,?,?,?,?,?)'
#         # указываем данные для запроса
#         data = [
#             (product_name,
#              product_price_original,
#              product_price,
#              product_price_with_ozon_card,
#              product_images,
#              product_brand_name,
#              product_brand_link,
#              product_rating,
#              product_categories,
#              product_color,
#              product_article,
#              product_sizes,
#              product_all_articles
#              )
#         ]
#
#         # добавляем с помощью множественного запроса все данные сразу
#         with con:
#             con.executemany(sql, data)
#
#         # выводим содержимое таблицы на экран
#         # with con:
#         #     data = con.execute("SELECT * FROM products")
#         #     for row in data:
#         #         print(row)
#
#     # """ Connect to the PostgreSQL database server """
#     # conn = None
#     # try:
#     #     # read connection parameters
#     #     params = config()
#     #
#     #     # connect to the PostgreSQL server
#     #     print('Connecting to the PostgreSQL database...')
#     #     conn = psycopg2.connect(**params)
#     #
#     #     # create a cursor
#     #     cur = conn.cursor()
#     #
#     #     # execute a statement
#     #     print('PostgreSQL database version:')
#     #     cur.execute('SELECT product_name FROM products')
#     #
#     #     rows = cur.fetchall()
#     #     for row in rows:
#     #         print("FIELD =", row)
#     #     # # display the PostgreSQL database server version
#     #     # db_version = cur.fetchone()
#     #     # print(db_version)
#     #
#     #     # close the communication with the PostgreSQL
#     #     cur.close()
#     # except (Exception, psycopg2.DatabaseError) as error:
#     #     print(error)
#     # finally:
#     #     if conn is not None:
#     #         conn.close()
#     #         print('Database connection closed.')