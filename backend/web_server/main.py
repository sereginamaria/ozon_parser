import flask

from web_server import logger, app
from db import db
from product_parser import schema, parsing_categories
from flask import request
from telegram import telegram_connector, telegram_notifier
from card_creator import card_creator

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/parse_page', methods=['GET'])
def parse_page():
    parsing_categories.parse_bag()

@app.route('/get_verification_information', methods=['GET'])
def get_verification_information():
    logger.info('get_verification_information')
    return list(db.get_verification_information())

@app.route('/save_product', methods=['POST'])
def save_product():
    logger.info('save_product')
    db.save_product(request.json)
    return 'save_product'

@app.route('/delete_product', methods=['POST'])
def delete_product():
    logger.info('delete_product')
    db.delete_product(request.json)
    return 'delete_product'

@app.route('/store_category', methods=['POST'])
def store_category():
    logger.info('store_category')
    db.store_category(request.json)
    return 'store_category'

@app.route('/return_all_categories', methods=['POST'])
def return_all_categories():
    logger.info('return_all_categories')
    db.return_all_categories()
    return 'return_all_categories'

@app.route('/send_post', methods=['POST'])
def send_post():
    logger.info('send_post')
    products_list = db.get_products_for_post(request.json)
    cards_list = []
    if len(products_list) == 6:
        cards_list.append(card_creator.create_title_card(schema.Product(*products_list[0])))
        cards_list.append(card_creator.create_triple_card(schema.Product(*products_list[0]), True))
        for product in products_list[1:]:
            cards_list.append(card_creator.create_triple_card(schema.Product(*product), False))

        products_links = [schema.Product(*product).url for product in products_list]

        telegram_connector.send_post(cards_list, request.json, products_links, schema.Product(*products_list[0]).sub_category)
    else:
        telegram_notifier.not_enough_products_in_db(request.json)
    return 'send_post'

@app.route('/get_count_of_categories', methods=['GET'])
def get_count_of_category():
    return db.count_of_categories()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
    # app.run(host="195.133.32.87", port=5001, debug=True)