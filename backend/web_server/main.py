from backend.web_server import logger, app
from backend.db import db
from backend.parser import get_products
import json
from flask import request, send_file, Response

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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)