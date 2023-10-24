# import sqlite3 as sl
import bot_requests

# открываем файл с базой данных

import psycopg2 as pg

connection = pg.connect(
    host='195.133.32.87',
    database='masha',
    port=5433,
    user='masha',
    password='mashamasha01'
)

cursor = connection.cursor()


def verification():
    cursor.execute(
        "select product_id, product_images from public.ozon_products where (verification != true) limit 1")
    return cursor.fetchall()


def callback_verification(data):
    if data.split('|')[1] == "yes":
        cursor.execute("update public.ozon_products set verification = true where product_id =" + str(data.split('|')[2]))
    if data.split('|')[1] == "no":
        cursor.execute("delete from public.ozon_products where product_id  = " + str(data.split('|')[2]))
    connection.commit()


def create_post(date_of_publication, time_of_publication, publishing_platform, product_id):
    cursor.execute(
        "update public.ozon_products set date_of_publication = '%s', time_of_publication = '%s', publishing_platform = '%s' where product_id = '%s'" % (
            date_of_publication, time_of_publication, publishing_platform, product_id))
    connection.commit()


def create_card(publication_category):
    cursor.execute(
        "select product_id, product_name, product_article, product_sizes, product_price, "
        "product_price_with_ozon_card, product_images, publication_category, product_url from public.ozon_products where (publication_category = '%s' and "
        "date_of_publication is null and publishing_platform is null and few_photos = false and verification = "
        "true) limit 30" % publication_category)

    product_list = cursor.fetchall()
    bot_requests.create_card(product_list)
    return product_list


def get_post_from_db(publication_category, publication_platform, date_of_publication):
    cursor.execute(
        "select product_id, product_name, product_article, product_sizes, product_price, "
        "product_price_with_ozon_card, product_images, publication_category, product_url from public.ozon_products where (publication_category = '%s' and "
        "publishing_platform = '%s' and date_of_publication = '%s' and few_photos = false and verification = "
        "true) limit 30" % (publication_category, publication_platform, date_of_publication))

    product_list = cursor.fetchall()
    bot_requests.create_post(product_list)

def autoposting_date(now, time):
    cursor.execute(
        "select product_id, product_name, product_article, product_sizes, product_price, "
        "product_price_with_ozon_card, product_images, publication_category, product_url "
        "from public.ozon_products where (date_of_publication = '%s' and time_of_publication <= '%s' "
        "and few_photos = false and verification = "
        "true and is_published = false)" % (str(now), time))

    product_list = cursor.fetchall()
    bot_requests.create_post(product_list)

    for product in product_list:
        (product_id, product_name, product_article, product_sizes, product_price, product_price_with_ozon_card,
         product_images, publication_category, product_url) = product
        cursor.execute(
            "update public.ozon_products set is_published = true where product_id = '%s'" % (product_id))
        connection.commit()