import flask
from flask import Blueprint

from web_server import logger
from parser_wb import get_products

wb = Blueprint('wb', __name__)
@wb.route('/wb')
def hello():
    get_products.parse_page('Футболка', 'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=футболка+женская')
    print('wb')