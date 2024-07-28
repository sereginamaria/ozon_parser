from backend.web_server import logger, app, parsing_categories
from backend.db import db
from backend.parser import get_products, schema
import json
from flask import request, send_file, Response
from backend.telegram import telegram_connector, telegram_notifier
from backend.card_creator import card_creator

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/parse_page', methods=['GET'])
def parse_page():
    # get_products.parse_page('Категория',
    #                         'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=шорты+женские')
    parsing_categories.parse_trousers()
    return 'parse_page'

@app.route('/get_verification_information', methods=['GET'])
def get_verification_information():
    logger.info('Получаем информацию о товаре для верификации')
    return list(db.get_verification_information())

@app.route('/save_product', methods=['POST'])
def save_product():
    db.save_product(request.json)
    return 'save'

@app.route('/delete_product', methods=['POST'])
def delete_product():
    db.delete_product(request.json)
    return 'delete'

@app.route('/store_category', methods=['POST'])
def store_category():
    db.store_category(request.json)
    return 'store_category'

@app.route('/return_all_categories', methods=['GET'])
def return_all_categories():
    db.return_all_categories()
    return 'return_all_categories'

# Передаем параметры category и sub_category
@app.route('/send_post', methods=['POST'])
def send_post():
    products_list = db.get_products_for_post(request.json)
    cards_list = []
    if len(products_list) == 6:
        cards_list.append(card_creator.create_title_card(schema.Product(*products_list[0])))
        cards_list.append(card_creator.create_triple_card(schema.Product(*products_list[0]), True))
        for product in products_list[1:]:
            cards_list.append(card_creator.create_triple_card(schema.Product(*product), False))
    else:
        telegram_notifier.not_enough_products_in_db(request.json)

    products_links = [schema.Product(*product).url for product in products_list]

    telegram_connector.send_post(cards_list, request.json, products_links)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)