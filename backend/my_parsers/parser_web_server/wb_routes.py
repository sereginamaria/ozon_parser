from flask import request, Blueprint
from my_parsers.parser_wb import parsing_categories
wb = Blueprint('wb', __name__)

@wb.route('/wb/parser/parse_trousers', methods=['POST'])
def parse_trousers():
    parsing_categories.parse_trousers()
    return '/wb/parser/parse_trousers'

@wb.route('/wb/parser/parse_home_clothes', methods=['POST'])
def parse_home_clothes():
    parsing_categories.parse_home_clothes()
    return '/wb/parser/parse_home_clothes'

@wb.route('/wb/parser/parse_jewelry', methods=['POST'])
def parse_jewelry():
    parsing_categories.parse_jewelry()
    return '/wb/parser/parse_jewelry'

@wb.route('/wb/parser/parse_bag', methods=['POST'])
def parse_bag():
    parsing_categories.parse_bag()
    return '/wb/parser/parse_bag'

@wb.route('/wb/parser/parse_tshirts', methods=['POST'])
def parse_tshirts():
    parsing_categories.parse_tshirts()
    return '/wb/parser/parse_tshirts'

@wb.route('/wb/parser/parse_shirts', methods=['POST'])
def parse_shirts():
    parsing_categories.parse_shirts()
    return '/wb/parser/parse_shirts'

@wb.route('/wb/parser/parse_jeans', methods=['POST'])
def parse_jeans():
    parsing_categories.parse_jeans()
    return '/wb/parser/parse_jeans'

@wb.route('/wb/parser/parse_jacket', methods=['POST'])
def parse_jacket():
    parsing_categories.parse_jacket()
    return '/wb/parser/parse_jacket'

@wb.route('/wb/parser/parse_dress', methods=['POST'])
def parse_dress():
    parsing_categories.parse_dress()
    return '/wb/parser/parse_dress'

@wb.route('/wb/parser/parse_shoes', methods=['POST'])
def parse_shoes():
    parsing_categories.parse_shoes()
    return '/wb/parser/parse_shoes'

@wb.route('/wb/parser/parse_top', methods=['POST'])
def parse_top():
    parsing_categories.parse_top()
    return '/wb/parser/parse_top'

@wb.route('/wb/parser/parse_skirt', methods=['POST'])
def parse_skirt():
    parsing_categories.parse_skirt()
    return '/wb/parser/parse_skirt'

@wb.route('/wb/parser/parse_suit', methods=['POST'])
def parse_suit():
    parsing_categories.parse_suit()
    return '/wb/parser/parse_suit'

@wb.route('/wb/parser/parse_accessories', methods=['POST'])
def parse_accessories():
    parsing_categories.parse_accessories()
    return '/wb/parser/parse_accessories'

@wb.route('/wb/parser/parse_blouse', methods=['POST'])
def parse_blouse():
    parsing_categories.parse_blouse()
    return '/wb/parser/parse_blouse'

@wb.route('/wb/parser/parse_kofta', methods=['POST'])
def parse_kofta():
    parsing_categories.parse_kofta()
    return '/wb/parser/parse_kofta'


@wb.route('/wb/parser/parse_outer_wear', methods=['POST'])
def parse_outer_wear():
    parsing_categories.parse_outer_wear()
    return '/wb/parser/parse_outer_wear'

@wb.route('/wb/parser/custom_request', methods=['POST'])
def custom_request():
    parsing_categories.custom_request(request.json['category'], request.json['request'])
    return '/wb/parser/custom_request'
