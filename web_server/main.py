from time import strftime

from parser.db import get_product as gp
from parser.get_product import parse_product
from parser.get_products_from_page import parse_page
from card_creator.card_creator import create_titled_card, create_triple_card

from card_creator.test_card_creator import post_creator as test_post_creator
from card_creator.test_card_creator import single_post_creator as test_single_post_creator
from card_creator.test_card_creator import card_creator as test_card_creator
from card_creator.test_card_creator import only_title_card_creator

from video_maker.video_maker import generate_video
from flask import request, send_file, Response
from web_server import logger, app

import json
import io


@app.before_request
def before_request():
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.info('%s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path)
    return


@app.route('/')
def hello():
    return "Hello!"


@app.route('/parse_page', methods=['GET'])
def get_page():
    request_data = request.json
    publication_category = request_data['publication_category']
    page_url = request_data['page_url']
    parse_page(publication_category, page_url)
    return 'Получаем ссылки на продукты со страниц'


@app.route('/parse_product', methods=['GET'])
def get_product():
    request_data = json.loads(request.data.decode('UTF-8'))
    publication_category = request_data.get('publication_category')
    page_url = request_data.get('page_url')
    parse_product(page_url, publication_category)
    return 'Парсим продукт'


@app.route('/get_titled_card', methods=['GET'])
def get_titled():
    payload = json.loads(request.json)
    product_id = payload['id']
    product = gp(product_id)
    card = create_titled_card(product)
    return send_file(
        io.BytesIO(card),
        download_name='card.png',
        mimetype='image/png'
    )


@app.route('/get_triple_card', methods=['GET'])
def get_triple():
    payload = json.loads(request.json)
    product_id = payload['id']
    if payload['type'] == 'front':
        is_front = True
    elif payload['type'] == 'back':
        is_front = False
    else:
        return Response(status=400)

    product = gp(product_id)
    card = create_triple_card(product, is_front)
    return send_file(
        io.BytesIO(card),
        download_name='card.png',
        mimetype='image/png'
    )


# @app.route('/create_video', methods=['GET', 'POST'])
# def create_video():
#     if request.method == 'POST':
#         generate_video(json.loads(request.json))
#         return 'Создаю тестовый одиночный пост (для бота)'
#     if request.method == 'GET':
#         generate_video('ghbdtn')
#         return 'Создаю одиночный пост'


if __name__ == "__main__":
    import requests
    logger.info("Starting debug")
    # url = '/product/nasos-dlya-perekachki-masla-topliva-i-drugih-tehnicheskih-zhidkostey-12v-100w-1-4l-min-984149846'
    # product = parse_product(url, 'somecategory')
    # with app.app_context():
    #     card = create_titled_card(product)
    # telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"
    # response = requests.post(
    #     url=telegram_url + '/sendMediaGroup', data={'chat_id': 6181726421,
    #                                                 'media': '''[{
    #                                                     "type": "photo",
    #                                                     "media": "attach://name1"
    #                                                 }]'''
    #                                                 },
    #     files={
    #         "name1": card
    #     }
    # )
    # print(response.status_code)
    app.run(host="0.0.0.0", port=5000, debug=True)
