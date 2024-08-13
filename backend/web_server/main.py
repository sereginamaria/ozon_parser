import flask

from web_server import logger, app
from db import db
from ozon_parser import schema, parsing_categories
from flask import request
from telegram import telegram_connector, telegram_notifier
from card_creator import card_creator
from text_recognizer.main import recognize_text

@app.route('/')
def hello():
    img_urls = 'https://cdn1.ozone.ru/s3/multimedia-1-2/7067465246.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-5/7001510045.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-9/7001510049.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-6/7001510046.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-d/7001510053.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-k/7001566076.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-4/7001510044.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-q/7001510030.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-b/7001510051.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-s/7001510032.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-c/7001510052.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-m/7001510062.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-l/7001510061.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-c/7060435032.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-y/7060435054.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-l/7060435041.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-p/7001510029.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-u/7060435050.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-9/7060435065.jpg,  https://cdn1.ozone.ru/s3/multimedia-1-h/7060435037.jpg'
    product_images = ', '.join([recognize_text(image_url) for image_url in img_urls.split(',')
                                if recognize_text(image_url) != None])

    print('priduct_images')
    print(product_images)

    return 'Hello!'

@app.route('/parse_page', methods=['GET'])
def parse_page():
    parsing_categories.parse_trousers()

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
    app.run(host="127.0.0.1", port=5000, debug=True)
    # app.run(host="195.133.32.87", port=5001, debug=True)