from backend.web_server import logger, app
from backend.db import db
from backend.parser import get_products, schema
import json
from flask import request, send_file, Response
from backend.telegram import telegram_connector
from backend.card_creator import card_creator

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/parse_page', methods=['GET'])
def parse_page():
    get_products.parse_page('Категория',
                            'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=шорты+женские')
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

@app.route('/send_media_group', methods=['GET'])
def send_media_group():
    newProduct = schema.Product('f', 'f', 'f', 'f', 'https://cdn1.ozone.ru/s3/multimedia-1-3/7049856459.jpg, https://cdn1.ozone.ru/s3/multimedia-1-8/7049856464.jpg, https://cdn1.ozone.ru/s3/multimedia-1-i/7049856690.jpg, https://cdn1.ozone.ru/s3/multimedia-1-n/7049856623.jpg, https://cdn1.ozone.ru/s3/multimedia-1-e/7049856614.jpg', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f')
    a = card_creator.create_triple_card(newProduct, False)
    print(a)
    # telegram_connector.send_media_group()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)