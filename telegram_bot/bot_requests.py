import json
import requests


def get_products_from_page(message, publication_category_page):
    page_url = message.text
    data = {"publication_category": publication_category_page, "page_url": page_url}
    requests.post("http://127.0.0.1:5000/get_products_from_page", json=data)


def get_product(message, publication_category_product):
    data = {"publication_category": publication_category_product, "page_url": message.text}
    requests.post("http://127.0.0.1:5000/get_product", json=data)


def create_card(product_list):
    requests.post("http://127.0.0.1:5000/create_card", json=json.dumps(product_list))

def create_post(product_list):
    requests.post("http://127.0.0.1:5000/create_post", json=json.dumps(product_list))