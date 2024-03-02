from parser.get_product import parse_product
from parser.get_products_from_page import get_products_from_page
from card_creator.card_creator import card_creator
from card_creator.card_creator import post_creator
from card_creator.card_creator import single_post_creator

from card_creator.test_card_creator import post_creator as test_post_creator
from card_creator.test_card_creator import single_post_creator as test_single_post_creator
from card_creator.test_card_creator import card_creator as test_card_creator

from card_creator.test_card_creator import only_title_card_creator

from video_maker.video_maker import generate_video
from flask import request
from parser import logger, app

import json


@app.route('/')
def hello():
    return "Hello!"


@app.route('/get_products_from_page', methods=['GET'])
def get_page():
    logger.info("Got request on /get_products_from_page")
    request_data = request.json
    publication_category = request_data['publication_category']
    page_url = request_data['page_url']
    get_products_from_page(publication_category, page_url)
    return 'Получаем ссылки на продукты со страниц'


@app.route('/get_product', methods=['GET', 'POST'])
def get_ozon_product():
    if request.method == 'POST':
        request_data = json.loads(request.data.decode('UTF-8'))
        publication_category = request_data.get('publication_category')
        page_url = request_data.get('page_url')
        message_type = True
        parse_product(page_url, publication_category, message_type)
        return 'Получаем информацию о товаре'
    if request.method == 'GET':
        return 'Получаем информацию о товаре'


@app.route('/create_card', methods=['GET', 'POST'])
def create_card():
    if request.method == 'POST':
        card_creator(json.loads(request.json))
        return 'Создаю карточку'
    if request.method == 'GET':
        rerq = card_creator([[140, 'Куртка Jan Steen', '1129369892', '42 RU, 48 RU, 50 RU, ', '6 441 ₽', '6 248 ₽',
                              'https://cdn1.ozone.ru/s3/multimedia-7/6725982931.jpg, https://cdn1.ozone.ru/s3/multimedia-m/6725987338.jpg, https://cdn1.ozone.ru/s3/multimedia-9/6725982933.jpg, https://cdn1.ozone.ru/s3/multimedia-4/6725982928.jpg, https://cdn1.ozone.ru/s3/multimedia-5/6725982929.jpg, https://cdn1.ozone.ru/s3/multimedia-8/6725982932.jpg, https://cdn1.ozone.ru/s3/multimedia-a/6725982934.jpg, https://cdn1.ozone.ru/s3/multimedia-6/6725982930.jpg, https://cdn1.ozone.ru/s3/multimedia-7/6740495611.jpg, ',
                              'Куртка', '/product/kurtka-jan-steen-1129369892/']])
        return rerq or "DONE"


@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        post_creator(json.loads(request.json))
        return 'Создаю пост'
    if request.method == 'GET':
        post_creator('ghbdtn')
        return 'Создаю пост'


@app.route('/create_single_post', methods=['GET', 'POST'])
def create_single_post():
    if request.method == 'POST':
        single_post_creator(json.loads(request.json))
        return 'Создаю одиночный пост'
    if request.method == 'GET':
        single_post_creator('ghbdtn')
        return 'Создаю одиночный пост'


@app.route('/create_test_card', methods=['GET', 'POST'])
def create_test_card():
    if request.method == 'POST':
        test_card_creator(json.loads(request.json))
        return 'Создаю карточку'
    if request.method == 'GET':
        rerq = test_card_creator([[140, 'Куртка Jan Steen', '1129369892', '42 RU, 48 RU, 50 RU, ', '6 441 ₽', '6 248 ₽',
                                   'https://cdn1.ozone.ru/s3/multimedia-7/6725982931.jpg, https://cdn1.ozone.ru/s3/multimedia-m/6725987338.jpg, https://cdn1.ozone.ru/s3/multimedia-9/6725982933.jpg, https://cdn1.ozone.ru/s3/multimedia-4/6725982928.jpg, https://cdn1.ozone.ru/s3/multimedia-5/6725982929.jpg, https://cdn1.ozone.ru/s3/multimedia-8/6725982932.jpg, https://cdn1.ozone.ru/s3/multimedia-a/6725982934.jpg, https://cdn1.ozone.ru/s3/multimedia-6/6725982930.jpg, https://cdn1.ozone.ru/s3/multimedia-7/6740495611.jpg, ',
                                   'Куртка', '/product/kurtka-jan-steen-1129369892/']])
        return rerq or "DONE"


@app.route('/create_test_post', methods=['GET', 'POST'])
def create_test_post():
    if request.method == 'POST':
        test_post_creator(json.loads(request.json))
        return 'Создаю тестовый пост (для бота)'
    if request.method == 'GET':
        test_post_creator('ghbdtn')
        return 'Создаю пост'


@app.route('/create_test_single_post', methods=['GET', 'POST'])
def create_test_single_post():
    if request.method == 'POST':
        test_single_post_creator(json.loads(request.json))
        return 'Создаю тестовый одиночный пост (для бота)'
    if request.method == 'GET':
        test_single_post_creator('ghbdtn')
        return 'Создаю одиночный пост'


@app.route('/create_video', methods=['GET', 'POST'])
def create_video():
    if request.method == 'POST':
        generate_video(json.loads(request.json))
        return 'Создаю тестовый одиночный пост (для бота)'
    if request.method == 'GET':
        generate_video('ghbdtn')
        return 'Создаю одиночный пост'


@app.route('/create_only_title_card', methods=['GET', 'POST'])
def create_only_title_card():

    if request.method == 'POST':
        only_title_card_creator(json.loads(request.json))
        return 'Создаю тестовый одиночный пост (для бота)'
    if request.method == 'GET':
        only_title_card_creator('ghbdtn')
        return 'Создаю одиночный пост'


if __name__ == "__main__":
    logger.info("Starting debug")
    app.run(host="0.0.0.0", port=5000, debug=True)
