from flask import request, Blueprint
from my_parsers.parser_ozon import parsing_categories
ozon = Blueprint('ozon', __name__)

@ozon.route('/ozon/parser/parse_trousers', methods=['POST'])
def parse_trousers():
    parsing_categories.parse_trousers()
    return '/ozon/parser/parse_trousers'

@ozon.route('/ozon/parser/parse_home_clothes', methods=['POST'])
def parse_home_clothes():
    parsing_categories.parse_home_clothes()
    return '/ozon/parser/parse_home_clothes'

@ozon.route('/ozon/parser/parse_jewelry', methods=['POST'])
def parse_jewelry():
    parsing_categories.parse_jewelry()
    return '/ozon/parser/parse_jewelry'

@ozon.route('/ozon/parser/parse_bag', methods=['POST'])
def parse_bag():
    parsing_categories.parse_bag()
    return '/ozon/parser/parse_bag'

@ozon.route('/ozon/parser/parse_tshirts', methods=['POST'])
def parse_tshirts():
    parsing_categories.parse_tshirts()
    return '/ozon/parser/parse_tshirts'

@ozon.route('/ozon/parser/parse_shirts', methods=['POST'])
def parse_shirts():
    parsing_categories.parse_shirts()
    return '/ozon/parser/parse_shirts'

@ozon.route('/ozon/parser/parse_jeans', methods=['POST'])
def parse_jeans():
    parsing_categories.parse_jeans()
    return '/ozon/parser/parse_jeans'

@ozon.route('/ozon/parser/parse_jacket', methods=['POST'])
def parse_jacket():
    parsing_categories.parse_jacket()
    return '/ozon/parser/parse_jacket'

@ozon.route('/ozon/parser/parse_dress', methods=['POST'])
def parse_dress():
    parsing_categories.parse_dress()
    return '/ozon/parser/parse_dress'

@ozon.route('/ozon/parser/parse_shoes', methods=['POST'])
def parse_shoes():
    parsing_categories.parse_shoes()
    return '/ozon/parser/parse_shoes'

@ozon.route('/ozon/parser/parse_top', methods=['POST'])
def parse_top():
    parsing_categories.parse_top()
    return '/ozon/parser/parse_top'

@ozon.route('/ozon/parser/parse_skirt', methods=['POST'])
def parse_skirt():
    parsing_categories.parse_skirt()
    return '/ozon/parser/parse_skirt'

@ozon.route('/ozon/parser/parse_suit', methods=['POST'])
def parse_suit():
    parsing_categories.parse_suit()
    return '/ozon/parser/parse_suit'

@ozon.route('/ozon/parser/parse_accessories', methods=['POST'])
def parse_accessories():
    parsing_categories.parse_accessories()
    return '/ozon/parser/parse_accessories'

@ozon.route('/ozon/parser/parse_blouse', methods=['POST'])
def parse_blouse():
    parsing_categories.parse_blouse()
    return '/ozon/parser/parse_blouse'

@ozon.route('/ozon/parser/parse_kofta', methods=['POST'])
def parse_kofta():
    parsing_categories.parse_kofta()
    return '/ozon/parser/parse_kofta'


@ozon.route('/ozon/parser/parse_outer_wear', methods=['POST'])
def parse_outer_wear():
    parsing_categories.parse_outer_wear()
    return '/ozon/parser/parse_outer_wear'

@ozon.route('/ozon/parser/custom_request', methods=['POST'])
def custom_request():
    parsing_categories.custom_request(request.json['category'], request.json['request'])
    return '/ozon/parser/custom_request'
