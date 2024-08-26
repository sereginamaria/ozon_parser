from parser_wb import get_products, schema
from web_server import logger
from db import db_wb
from flask import request, Blueprint
from cards_module import card_creator
from datetime import date
import datetime as datetime2
from main_config import TIMESHEET
from video_module import video_maker
from telegram.wb_bot import telegram_notifier, telegram_connector

wb = Blueprint('wb', __name__)

@wb.route('/wb')
def hello():
    get_products.parse_page('Футболка', 'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=футболка+женская')
    return 'wb'

@wb.route('/wb/get_verification_information', methods=['GET'])
def get_verification_information():
    logger.info('get_verification_information')
    return list(db_wb.get_verification_information())

@wb.route('/wb/save_product', methods=['POST'])
def save_product():
    logger.info('save_product')
    db_wb.save_product(request.json)
    return 'save_product'

@wb.route('/wb/delete_product', methods=['POST'])
def delete_product():
    logger.info('delete_product')
    db_wb.delete_product(request.json)
    return 'delete_product'

@wb.route('/wb/store_category', methods=['POST'])
def store_category():
    logger.info('store_category')
    db_wb.store_category(request.json)
    return 'store_category'

@wb.route('/wb/return_all_categories', methods=['POST'])
def return_all_categories():
    logger.info('return_all_categories')
    db_wb.return_all_categories()
    return 'return_all_categories'

@wb.route('/wb/send_post', methods=['POST'])
def send_post():
    logger.info('send_post')
    products_list = db_wb.get_products_for_post(request.json)
    cards_list = []
    print(products_list)
    if len(products_list) == 2:
        unique_sub_categories = list(set([schema.Product(*product).sub_category for product in products_list]))
        cards_list.append(card_creator.create_title_card(schema.Product(*products_list[0])))
        cards_list.append(card_creator.create_triple_card(schema.Product(*products_list[0]), True))
        for product in products_list[1:]:
            cards_list.append(card_creator.create_triple_card(schema.Product(*product), False))

        products_links = [schema.Product(*product).url for product in products_list]

        resp = telegram_connector.send_post(cards_list, request.json, products_links, unique_sub_categories)
        if resp:
            for product in products_list:
                db_wb.publish_product(schema.Product(*product).id)
    else:
        telegram_notifier.not_enough_products_in_db(request.json)
    return 'send_post'

@wb.route('/wb/get_timesheet', methods=['GET'])
def get_timesheet():
    list_with_timesheet = []
    count_of_products = db_wb.count_of_verified_products()
    count_of_products_list = []
    for count_of_product in count_of_products:
        count_of_products_list.append(list(count_of_product))

    def are_there_products_in_db_wb(category, time):
        for count_of_product_list in count_of_products_list:
            if category in count_of_product_list:
                if count_of_product_list[1] >= 6:
                    count_of_product_list[1] = count_of_product_list[1] - 6
                    return '\n' + time + ' ' + category + '  ✅️'
                else:
                    return ('\n' + time + ' ' + category + ' ❌ ' + 'Нужно еще '
                                       + str(6 - count_of_product_list[1]))

        return '\n' + time + ' ' + category + ' ❌ ' + 'Нужно еще 6'

    date_of_publication = date.today()
    i = 1
    while i <= 14:
        timesheet_text = str(date_of_publication)

        date_name = date_of_publication.strftime("%A")
        for category, time in TIMESHEET[date_name].items():

            resp = are_there_products_in_db_wb(category, time)
            timesheet_text += resp

        i += 1
        date_of_publication += datetime2.timedelta(days=1)
        list_with_timesheet.append(timesheet_text)

    return list_with_timesheet

@wb.route('/wb/count_of_verified_products', methods=['GET'])
def count_of_verified_products():
    return db_wb.count_of_verified_products()

@wb.route('/wb/count_of_not_verified_products', methods=['GET'])
def count_of_not_verified_products():
    return db_wb.count_of_not_verified_products()

@wb.route('/wb/create_videos', methods=['GET'])
def create_videos():
    categories = ["Украшения", "Верхняя Одежда", "Кофта", "Брюки", "Джинсы", "Платье", "Пиджак", "Сумка", "Костюм",
                 "Юбка", "Блузка", "Обувь", "Футболка", "Топ", "Домашняя Одежда", "Рубашка"]
    for category in categories:
        new_product = {
            "category": category,
        }
        products_list = db_wb.get_products_for_post(new_product)
        cards_list = []
        if len(products_list) == 6:
            cards_list.append(card_creator.create_title_card(schema.Product(*products_list[0])))
            cards_list.append(card_creator.create_triple_card(schema.Product(*products_list[0]), True))
            for product in products_list[1:]:
                cards_list.append(card_creator.create_triple_card(schema.Product(*product), False))

            video_b = video_maker.generate_video(cards_list)
            telegram_connector.send_video(video_b)
    return 'end'