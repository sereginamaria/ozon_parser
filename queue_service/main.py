from flask import Flask
from get_product_json import get_product_json
from get_products_from_page import get_products_from_page

app = Flask(__name__)

@app.route('/queue')
def queue():
    return "queue!"


if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0", port=5010)