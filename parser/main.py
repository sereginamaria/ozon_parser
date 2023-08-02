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


@app.route('/get_product')
def get_ozon_product():
    print('123')
    get_product("/product/dzhinsy-jelika-881711556/")
    return 'Получаем информацию о товаре'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
