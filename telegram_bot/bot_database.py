# import sqlite3 as sl
import requests
telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"

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
        "select product_id, product_images, publication_category, sub_category, product_name from public.ozon_products  where (verification = false) order by product_id limit 1")
    return cursor.fetchall()


def callback_verification(data):
    global new_name
    if data.split('|')[1] == "yes":
        cursor.execute(
            "select product_name from public.ozon_products where product_id =" + str(data.split('|')[2]))

        product_name = cursor.fetchall()
        new_name = new_tt = ''.join(product_name[0])

        # requests.post(
        #     url=telegram_url + '/sendMessage',
        #     data={'chat_id': 6181726421, 'text': new_tt}
        # ).json()

        if len(new_tt) > 30:
            new_name = new_tt.partition(' ')[0]
            # requests.post(
            #     url=telegram_url + '/sendMessage',
            #     data={'chat_id': 6181726421, 'text': new_name}
            # ).json()

        cursor.execute("update public.ozon_products set verification = true, product_name = '%s' where product_id = '%s'" % (
            new_name, str(data.split('|')[2])))

    if data.split('|')[1] == "no":
        cursor.execute("update public.ozon_products set verification = null where product_id  = " + str(data.split('|')[2]))

    connection.commit()

def verification_change_name(data):
    cursor.execute(
        "select product_name from public.ozon_products where product_id =" + str(data.split('|')[2]))
    product_list = cursor.fetchall()
    return product_list

def verification_add_new_name(data, new_name):
    cursor.execute("update public.ozon_products set product_name = '%s' where product_id = '%s'" % (
        new_name, str(data.split('|')[2])))
    connection.commit()

def verification_delete_photo(data):
    cursor.execute(
        "select product_images from public.ozon_products where product_id =" + str(data.split('|')[2]))
    product_list = cursor.fetchall()
    return product_list, str(data.split('|')[3])

def post_verification_delete_photo(product_id, new_product_images_list):
    cursor.execute("update public.ozon_products set product_images = '%s' where product_id = '%s'" % (
        new_product_images_list, product_id))
    connection.commit()

def create_post(date_of_publication, time_of_publication, publishing_platform, product_id):

    cursor.execute(
        "update public.ozon_products set date_of_publication = '%s', time_of_publication = '%s', publishing_platform = '%s', post_type = '%s' where product_id = '%s'" % (
            date_of_publication, time_of_publication, publishing_platform, 'group', product_id))
    connection.commit()

def create_single_post(date_of_publication, time_of_publication, publishing_platform, product_id):
    cursor.execute(
        "update public.ozon_products set date_of_publication = '%s', time_of_publication = '%s', publishing_platform = '%s', post_type = '%s' where product_id = '%s'" % (
            date_of_publication, time_of_publication, publishing_platform, 'single', product_id))
    connection.commit()


def create_card(sub_category):
    cursor.execute(
        "select product_id, product_name, product_article, product_sizes, product_price, "
        "product_price_with_ozon_card, product_images, sub_category, product_url from public.ozon_products where (sub_category = '%s' and "
        "date_of_publication is null and publishing_platform is null and few_photos = false and verification = "
        "true) limit 14" % sub_category)

    product_list = cursor.fetchall()
    bot_requests.create_card(product_list)
    return product_list

def create_test_card(category):

    if (category == 'Платье' or category == 'Юбка'
            or category == 'Топ' or category == 'Футболка'
            or category == 'Костюм' or category == 'Нижнее Белье'
            or category == 'Рубашка' or category == 'Брюки' or category == 'Обувь'
            or category == 'Пиджак' or category == 'Джинсы' or category == 'Аксессуары'
            or category == 'Шорты' or category == 'Домашняя Одежда'
            or category == 'Спортивная Одежда' or category == 'Купальники'
            or category == 'Сумка' or category == 'Дом'
            or category == 'Косметика' or category == 'Детям'
            or category == 'Мужчинам' or category == 'Украшения' or category == '23 Февраля'
            or category == '8 Марта'):

        cursor.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, "
            "product_price_with_ozon_card, product_images, sub_category, product_url from public.ozon_products where (publication_category = '%s' and "
            "date_of_publication is null and publishing_platform is null and few_photos = false and verification = "
            "true) order by product_id limit 14" % category)
    else:
        cursor.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, "
            "product_price_with_ozon_card, product_images, sub_category, product_url from public.ozon_products where (sub_category = '%s' and "
            "date_of_publication is null and publishing_platform is null and few_photos = false and verification = "
            "true) order by product_id limit 14" % category)

    product_list = cursor.fetchall()


    bot_requests.create_test_card(product_list)
    return product_list

def create_verification_test_card(product_id):
    cursor.execute(
        "select product_id, product_name, product_article, product_sizes, product_price, "
        "product_price_with_ozon_card, product_images, publication_category, product_url from public.ozon_products where (product_id = '%s')" % product_id)
    product_list = cursor.fetchall()


    bot_requests.create_test_card(product_list)
    bot_requests.create_test_post(product_list)
    return product_list


def get_product_by_id(product_id):
    cursor.execute(
        "select product_id, product_name, product_article, product_images, publication_category, sub_category, product_url, few_photos from public.ozon_products where (product_id = '%s')" % product_id)
    product_list = cursor.fetchall()
    return product_list


def get_check_list(publication_category, date_of_publication, time_of_publication):
    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': publication_category}
    # ).json()
    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': date_of_publication}
    # ).json()
    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': time_of_publication}
    # ).json()
    cursor.execute(
        "select product_id, product_name, product_article, product_images, product_url, sub_category from public.ozon_products "
        "where (publication_category = '%s' and date_of_publication = '%s' and time_of_publication = '%s')"
        % (publication_category, date_of_publication, time_of_publication))

    product_list = cursor.fetchall()
    return product_list



def plane_to_db(product_id, date_of_publication, time_of_publication, publishing_platform, post_type):
    cursor.execute(
        "select product_name from public.ozon_products where (product_id = '%s')" % product_id)

    product_name = cursor.fetchall()
    new_name = new_tt = ''.join(product_name[0])

    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': new_tt}
    # ).json()

    if len(new_tt) > 30:
        new_name = new_tt.partition(' ')[0]
        # requests.post(
        #     url=telegram_url + '/sendMessage',
        #     data={'chat_id': 6181726421, 'text': new_name}
        # ).json()

    cursor.execute(
        "update public.ozon_products set verification = true, product_name = '%s', date_of_publication = '%s', "
        "time_of_publication = '%s', publishing_platform = '%s', post_type = '%s' where product_id = '%s'" % (
            new_name, date_of_publication, time_of_publication, publishing_platform, post_type, product_id))

    connection.commit()

def plane_if_few_photos(product_id):
    cursor.execute("update public.ozon_products set verification = true where product_id = '%s'" % product_id)

    connection.commit()

def create_single_card(publication_category):
    cursor.execute(
        "select product_id, product_name, product_article, product_sizes, product_price, "
        "product_price_with_ozon_card, product_images, publication_category, product_url from public.ozon_products where (publication_category = '%s' and "
        "date_of_publication is null and publishing_platform is null and few_photos = false and verification = "
        "true) limit 10" % publication_category)

    product_list = cursor.fetchall()
    bot_requests.create_card(product_list)
    return product_list

def get_post_from_db(publication_category, publication_platform, date_of_publication):
    if (publication_category == 'Платье' or publication_category == 'Юбка'
            or publication_category == 'Топ' or publication_category == 'Футболка'
            or publication_category == 'Костюм' or publication_category == 'Нижнее Белье'
            or publication_category == 'Рубашка'  or publication_category == 'Блузка'
            or publication_category == 'Брюки' or publication_category == 'Обувь'
            or publication_category == 'Пиджак' or publication_category == 'Джинсы' or publication_category == 'Аксессуары'
            or publication_category == 'Шорты' or publication_category == 'Домашняя Одежда'
            or publication_category == 'Спортивная Одежда' or publication_category == 'Купальники'
            or publication_category == 'Сумка' or publication_category == 'Дом'
            or publication_category == 'Косметика' or publication_category == 'Детям'
            or publication_category == 'Мужчинам' or publication_category == 'Украшения'
            or publication_category == '8 Марта'):

        cursor.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, "
            "product_price_with_ozon_card, product_images, publication_category, product_url from public.ozon_products where (publication_category = '%s' and "
            "publishing_platform = '%s' and date_of_publication = '%s' and few_photos = false and verification = "
            "true and post_type = 'group') order by product_id" % (publication_category, publication_platform, date_of_publication))
    else:
        cursor.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, "
            "product_price_with_ozon_card, product_images, publication_category, product_url from public.ozon_products where (sub_category = '%s' and "
            "publishing_platform = '%s' and date_of_publication = '%s' and few_photos = false and verification = "
            "true and post_type = 'group') order by product_id" % (publication_category, publication_platform, date_of_publication))

    product_list = cursor.fetchall()
    if len(product_list) != 0:
        bot_requests.create_test_post(product_list)
        # bot_requests.create_test_post_for_other_networks(product_list)

    if (publication_category == 'Платье' or publication_category == 'Юбка'
            or publication_category == 'Топ' or publication_category == 'Футболка'
            or publication_category == 'Костюм' or publication_category == 'Нижнее Белье'
            or publication_category == 'Рубашка' or publication_category == 'Блузка'
            or publication_category == 'Брюки' or publication_category == 'Обувь'
            or publication_category == 'Пиджак' or publication_category == 'Джинсы' or publication_category == 'Аксессуары'
            or publication_category == 'Шорты' or publication_category == 'Домашняя Одежда'
            or publication_category == 'Спортивная Одежда' or publication_category == 'Купальники'
            or publication_category == 'Сумка' or publication_category == 'Дом'
            or publication_category == 'Косметика' or publication_category == 'Детям'
            or publication_category == 'Мужчинам' or publication_category == 'Украшения'
            or publication_category == '8 Марта'    ):

        cursor.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, "
            "product_price_with_ozon_card, product_images, publication_category, product_url from public.ozon_products where (publication_category = '%s' and "
            "publishing_platform = '%s' and date_of_publication = '%s' and few_photos = false and verification = "
            "true and post_type = 'single') " % (publication_category, publication_platform, date_of_publication))
    else:
        cursor.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, "
            "product_price_with_ozon_card, product_images, publication_category, product_url from public.ozon_products where (sub_category = '%s' and "
            "publishing_platform = '%s' and date_of_publication = '%s' and few_photos = false and verification = "
            "true and post_type = 'single') " % (publication_category, publication_platform, date_of_publication))

    product_list = cursor.fetchall()

    if len(product_list) != 0:
        bot_requests.create_test_single_post(product_list)
        # bot_requests.create_test_post_for_other_networks(product_list)
    return True

def get_timesheet(date_of_publication, time_of_publication):
    cursor.execute(
        "select publication_category, sub_category from public.ozon_products where (date_of_publication = '%s' and "
        "time_of_publication = '%s') order by product_id" % (date_of_publication, time_of_publication))

    product_list = cursor.fetchall()
    return product_list

def get_all_day_posts_from_db(publication_platform, date_of_publication, time_of_publication):
    cursor.execute(
        "select product_id, product_name, product_article, product_sizes, product_price, "
        "product_price_with_ozon_card, product_images, publication_category, product_url from public.ozon_products where "
        "(publishing_platform = '%s' and date_of_publication = '%s' and few_photos = false and verification = "
        "true and post_type = 'group' and time_of_publication = '%s') order by product_id" % (publication_platform, date_of_publication, time_of_publication))

    product_list = cursor.fetchall()
    print(product_list)

    if len(product_list) != 0:
        bot_requests.create_test_post_for_other_networks(product_list)
    return product_list

def autoposting_date(now, time):
    print('autopost')

    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': now}
    # ).json()
    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': time}
    # ).json()

    cursor.execute(
        "select product_id, product_name, product_article, product_sizes, product_price, "
        "product_price_with_ozon_card, product_images, publication_category, product_url "
        "from public.ozon_products where (date_of_publication = '%s' and time_of_publication <= '%s' "
        "and few_photos = false and verification = "
        "true and is_published = false and post_type = 'group') order by product_id" % (str(now), time))

    product_list = cursor.fetchall()
    print('group')
    print(product_list)

    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': str(len(product_list))}
    # ).json()

    if len(product_list) == 6:
        # requests.post(
        #     url=telegram_url + '/sendMessage',
        #     data={'chat_id': 6181726421, 'text': '333333333333'}
        # ).json()
        bot_requests.create_post(product_list)
        for product in product_list:
            (product_id, product_name, product_article, product_sizes, product_price, product_price_with_ozon_card,
             product_images, publication_category, product_url) = product
            cursor.execute(
                "update public.ozon_products set is_published = true where product_id = '%s'" % (product_id))
            connection.commit()



    cursor.execute(
        "select product_id, product_name, product_article, product_sizes, product_price, "
        "product_price_with_ozon_card, product_images, publication_category, product_url "
        "from public.ozon_products where (date_of_publication = '%s' and time_of_publication <= '%s' "
        "and few_photos = false and verification = "
        "true and is_published = false and post_type = 'single')" % (str(now), time))

    product_list = cursor.fetchall()
    print('single')
    print(product_list)
    if len(product_list) != 0:
        bot_requests.create_single_post(product_list)
        for product in product_list:
            (product_id, product_name, product_article, product_sizes, product_price, product_price_with_ozon_card,
             product_images, publication_category, product_url) = product
            cursor.execute(
                "update public.ozon_products set is_published = true where product_id = '%s'" % (product_id))
            connection.commit()



def product_for_only_title_card(id):
    cursor.execute(
        "select product_name, product_images, publication_category from public.ozon_products where (product_id = '%s')" % id)
    product_list = cursor.fetchall()
    bot_requests.create_only_title_card(product_list)