import json
import requests

BASE_URL = 'http://195.133.46.183:5000'
# BASE_URL = 'http://127.0.0.1:5000'

def get_products_from_page(message, publication_category_page):
    page_url = message.text
    data = {"publication_category": publication_category_page, "page_url": page_url}
    requests.post(BASE_URL + "/get_products_from_page", json=data)


def get_product(message, publication_category_product):
    data = {"publication_category": publication_category_product, "page_url": message.text}
    requests.post(BASE_URL + "/get_product", json=data)


def create_card(product_list):
    requests.post(BASE_URL + "/create_card", json=json.dumps(product_list))

def create_post(product_list):
    requests.post(BASE_URL + "/create_post", json=json.dumps(product_list))

def create_single_post(product_list):
    requests.post(BASE_URL + "/create_single_post", json=json.dumps(product_list))


def create_test_card(product_list):
    requests.post(BASE_URL + "/create_test_card", json=json.dumps(product_list))


def create_test_post(product_list):
    requests.post(BASE_URL + "/create_test_post", json=json.dumps(product_list))

def create_test_post_for_other_networks(product_list):
    requests.post(BASE_URL + "/create_test_post_for_other_networks", json=json.dumps(product_list))

def create_test_single_post(product_list):
    requests.post(BASE_URL + "/create_test_single_post", json=json.dumps(product_list))


def create_video(text):
    requests.post(BASE_URL + "/create_video", json=json.dumps(text))


def create_only_title_card(product_list):
    requests.post(BASE_URL + "/create_only_title_card", json=json.dumps(product_list))