from web_server import logger
from db import db_ozon
from parser_ozon import schema, parsing_categories
from flask import request, Blueprint
from cards_module import card_creator
from datetime import date
import datetime as datetime2
from main_config import TIMESHEET
from video_module import video_maker

from telegram.ozon_bot import telegram_notifier, telegram_connector

import datetime
import random

ozon = Blueprint('ozon', __name__)

@ozon.route('/')
def hello():
    return 'Hello!'

@ozon.route('/parse_page', methods=['GET'])
def parse_page():
    parsing_categories.parse_kofta()

@ozon.route('/get_verification_information', methods=['GET'])
def get_verification_information():
    logger.info('get_verification_information')
    return list(db_ozon.get_verification_information())

@ozon.route('/save_product', methods=['POST'])
def save_product():
    logger.info('save_product')
    current_date = datetime.date.today()
    db_ozon.save_product(request.json, current_date)
    return 'save_product'

@ozon.route('/delete_product', methods=['POST'])
def delete_product():
    logger.info('delete_product')
    db_ozon.delete_product(request.json)
    return 'delete_product'

@ozon.route('/delete_product_from_db', methods=['POST'])
def delete_product_from_db():
    logger.info('delete_product_from_db')
    db_ozon.delete_product_from_db(request.json)
    return 'delete_product_from_db'

@ozon.route('/store_category', methods=['POST'])
def store_category():
    logger.info('store_category')
    db_ozon.store_category(request.json)
    return 'store_category'

@ozon.route('/return_all_categories', methods=['POST'])
def return_all_categories():
    logger.info('return_all_categories')
    db_ozon.return_all_categories()
    return 'return_all_categories'

@ozon.route('/send_post', methods=['POST'])
def send_post():
    logger.info('send_post')
    products_list = db_ozon.get_products_for_post(request.json)
    logger.info(products_list)
    cards_list = []

    # if len(products_list != 6):
    #     products_list = db_ozon.get_products_for_post(request.json)
    #     logger.info(products_list)


    if len(products_list) == 6:
        unique_sub_categories = list(set([schema.Product(*product).sub_category for product in products_list]))
        cards_list.append(card_creator.create_title_card(schema.Product(*products_list[0]), 'ozon'))
        cards_list.append(card_creator.create_triple_card(schema.Product(*products_list[0]), True, 'ozon'))
        for product in products_list[1:]:
            cards_list.append(card_creator.create_triple_card(schema.Product(*product), False, 'ozon'))

        products_links = [schema.Product(*product).url for product in products_list]

        resp = telegram_connector.send_post(cards_list, request.json, products_links, unique_sub_categories)
        if resp:
            for product in products_list:
                db_ozon.publish_product(schema.Product(*product).id)
    else:
        telegram_notifier.not_enough_products_in_db(request.json)
    return 'send_post'

@ozon.route('/get_timesheet', methods=['GET'])
def get_timesheet():
    list_with_timesheet = []
    count_of_products = db_ozon.count_of_verified_products()
    count_of_products_list = []
    for count_of_product in count_of_products:
        count_of_products_list.append(list(count_of_product))

    def are_there_products_in_db_ozon(category, time):
        for count_of_product_list in count_of_products_list:
            if category in count_of_product_list:
                if count_of_product_list[1] >= 6 and count_of_product_list[1] != 0:
                    count_of_product_list[1] = count_of_product_list[1] - 6
                    return '\n' + time + ' ' + category + '  ✅️'
                else:
                    text = ('\n' + time + ' ' + category + ' ❌ ' + 'Нужно еще ' + str(6 - count_of_product_list[1]))
                    count_of_product_list[1] = 0
                    return text

        return '\n' + time + ' ' + category + ' ❌ ' + 'Нужно еще 6'

    date_of_publication = date.today()
    date_of_publication += datetime2.timedelta(days=1)
    i = 1
    while i <= 14:
        timesheet_text = str(date_of_publication)

        date_name = date_of_publication.strftime("%A")
        for category, time in TIMESHEET[date_name].items():

            resp = are_there_products_in_db_ozon(category, time)
            timesheet_text += resp

        i += 1
        date_of_publication += datetime2.timedelta(days=1)
        list_with_timesheet.append(timesheet_text)

    return list_with_timesheet
@ozon.route('/count_of_verified_products', methods=['GET'])
def count_of_verified_products():
    list_with_count_of_verified_products = []
    count_of_products = db_ozon.count_of_verified_products()
    count_of_products_list = []
    for count_of_product in count_of_products:
        count_of_products_list.append(list(count_of_product))


    for count_of_product_list in count_of_products_list:
        if count_of_product_list[0] == 'Верхняя Одежда' or count_of_product_list[0] == 'Кофта':
            if count_of_product_list[1] >= 60:
                list_with_count_of_verified_products.append('\n' + count_of_product_list[0] + ' ' + str(count_of_product_list[1]) + '  ✅️')
            else:
                list_with_count_of_verified_products.append('\n' + count_of_product_list[0] + ' ' + str(count_of_product_list[1]) +
                                           ' ❌ ' + 'Нужно еще ' + str(60 - count_of_product_list[1]))

        if count_of_product_list[0] == 'Платье' or count_of_product_list[0] == 'Юбка' \
                or count_of_product_list[0] == 'Футболка' or count_of_product_list[0] == 'Костюм'\
                or count_of_product_list[0] == 'Джинсы' or count_of_product_list[0] == 'Аксессуары':
            if count_of_product_list[1] >= 36:
                list_with_count_of_verified_products.append('\n' + count_of_product_list[0] + ' ' + str(count_of_product_list[1]) + '  ✅️')
            else:
                list_with_count_of_verified_products.append('\n' + count_of_product_list[0] + ' ' + str(count_of_product_list[1]) +
                                           ' ❌ ' + 'Нужно еще ' + str(36 - count_of_product_list[1]))

        if count_of_product_list[0] == 'Брюки' or count_of_product_list[0] == 'Пиджак' \
                or count_of_product_list[0] == 'Обувь' or count_of_product_list[0] == 'Сумка'\
                or count_of_product_list[0] == 'Украшения':
            if count_of_product_list[1] >= 48:
                list_with_count_of_verified_products.append('\n' + count_of_product_list[0] + ' ' + str(count_of_product_list[1]) + '  ✅️')
            else:
                list_with_count_of_verified_products.append('\n' + count_of_product_list[0] + ' ' + str(count_of_product_list[1]) +
                                           ' ❌ ' + 'Нужно еще ' + str(48 - count_of_product_list[1]))

        if count_of_product_list[0] == 'Топ' or count_of_product_list[0] == 'Рубашка' \
                or count_of_product_list[0] == 'Блузка':
            if count_of_product_list[1] >= 24:
                list_with_count_of_verified_products.append('\n' + count_of_product_list[0] + ' ' + str(count_of_product_list[1]) + '  ✅️')
            else:
                list_with_count_of_verified_products.append('\n' + count_of_product_list[0] + ' ' + str(count_of_product_list[1]) +
                                           ' ❌ ' + 'Нужно еще ' + str(24 - count_of_product_list[1]))

        if count_of_product_list[0] == 'Домашняя Одежда' or count_of_product_list[0] == 'Шорты' \
                or count_of_product_list[0] == 'Корсет':
            if count_of_product_list[1] >= 12:
                list_with_count_of_verified_products.append(
                    '\n' + count_of_product_list[0] + ' ' + str(count_of_product_list[1]) + '  ✅️')
            else:
                list_with_count_of_verified_products.append('\n' + count_of_product_list[0] + ' ' + str(count_of_product_list[1]) +
                                           ' ❌ ' + 'Нужно еще ' + str(12 - count_of_product_list[1]))
    return list_with_count_of_verified_products

@ozon.route('/count_of_not_verified_products', methods=['GET'])
def count_of_not_verified_products():
    return db_ozon.count_of_not_verified_products()

@ozon.route('/create_videos', methods=['GET'])
def create_videos():
    categories = ["Украшения", "Верхняя Одежда", "Кофта", "Брюки", "Джинсы", "Платье", "Пиджак", "Сумка", "Костюм",
                 "Юбка", "Блузка", "Обувь", "Футболка", "Топ", "Домашняя Одежда", "Рубашка"]
    for category in categories:
        new_product = {
            "category": category,
        }
        products_list = db_ozon.get_products_for_post(new_product)
        cards_list = []
        if len(products_list) == 6:
            cards_list.append(card_creator.create_title_card(schema.Product(*products_list[0]), 'ozon'))
            cards_list.append(card_creator.create_triple_card(schema.Product(*products_list[0]), True, 'ozon'))
            for product in products_list[1:]:
                cards_list.append(card_creator.create_triple_card(schema.Product(*product), False, 'ozon'))

            video_b = video_maker.generate_video(cards_list)
            telegram_connector.send_video(video_b)
    return 'end'

@ozon.route('/get_stylist_card_information', methods=['GET'])
def get_stylist_card_information():
    products_for_card1 = ['Верхняя Одежда', 'Сумка', 'Аксессуары']
    products_for_card2 = ['Кофта', 'Топ', 'Корсет', 'Футболка', 'Рубашка', 'Блузка', 'Пиджак']
    products_for_card3 = ['Платье', 'Юбка', 'Брюки', 'Джинсы']

    product1 = random.choice(products_for_card1)
    product2 = random.choice(products_for_card2)
    product3 = random.choice(products_for_card3)
    product4 = 'Обувь'

    if product3 == 'Платье' and product1 != 'Сумка':
        product2 = 'Сумка'
    if product3 == 'Платье' and product1 == 'Сумка':
        product2 = 'Украшения'

    print(product1, product2, product3, product4)

    from datetime import timedelta
    current_date = datetime.date.today() - timedelta(14)
    print(current_date)

    products = [schema.Product(*product)
                    for product in db_ozon.get_products_for_stile_card(product1, product2, product3, product4, current_date)]

    for product in products:
        print(product.name)

    # stile_card = card_creator.create_stiled_card(products, 'ozon')

    # stylist_bot_telegram_connector.send_post(stile_card)

    return products
