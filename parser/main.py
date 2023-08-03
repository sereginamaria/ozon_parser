from flask import Flask
from parser.get_product import get_product
from parser.get_products_from_page import get_products_from_page

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


@app.route('/get_products_from_page')
def get_page():
    get_products_from_page(
        "https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Летнее+платье")
    return 'Получаем ссылки на продукты со страниц'


@app.post('/get_product')
def get_ozon_product(message):
    print('123')
    print(message)
    get_product(message)
    return 'Получаем информацию о товаре'

    #
    # if request.method == 'POST':
    #     print('123')
    #     get_product("/product/plate-1040289631/")
    #     return 'Получаем информацию о товаре'
    # if request.method == 'POST':
    #     print('123')
    #     get_product("/product/plate-1040289631/")
    #     return 'Получаем информацию о товаре'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
