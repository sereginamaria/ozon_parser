from flask import Flask
from parser.get_product import get_product
from parser.get_products_from_page import get_products_from_page
from card_creator.card_creator import card_creator
from card_creator.card_creator import post_creator
from flask import request

app = Flask(__name__, template_folder='../card_creator/templates')

import json
@app.route('/')
def hello():
    return "Hello!"


@app.route('/get_products_from_page', methods=['GET', 'POST'])
def get_page():
    if request.method == 'POST':
        request_data = json.loads(request.data.decode('UTF-8'))
        publication_category = request_data.get('publication_category')
        page_url = request_data.get('page_url')
        get_products_from_page(publication_category, page_url)
        return 'Получаем ссылки на продукты со страниц'
    if request.method == 'GET':
        return 'Получаем ссылки на продукты со страниц'

    # get_products_from_page(
    #     "https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Летнее+платье")



@app.route('/get_product', methods=['GET', 'POST'])
def get_ozon_product():
    if request.method == 'POST':
        request_data = json.loads(request.data.decode('UTF-8'))
        publication_category = request_data.get('publication_category')
        page_url = request_data.get('page_url')
        message_type = True
        get_product(page_url, publication_category, message_type)
        return 'Получаем информацию о товаре'
    if request.method == 'GET':
        return 'Получаем информацию о товаре'

@app.route('/create_card', methods=['GET', 'POST'])
def create_card():
    if request.method == 'POST':
        print(request)
        print(request.json)
        print(type(json.loads(request.json)))

        card_creator(json.loads(request.json))
        return 'Создаю карточку'
    if request.method == 'GET':
        card_creator('ghbdtn')
        return 'Создаю карточку'

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        print(request)
        print(request.json)
        print(type(json.loads(request.json)))

        post_creator(json.loads(request.json))
        return 'Создаю пост'
    if request.method == 'GET':
        card_creator('ghbdtn')
        return 'Создаю пост'

if __name__ == "__main__":
    app.run(host="194.87.232.115", port=5001, debug=True)
