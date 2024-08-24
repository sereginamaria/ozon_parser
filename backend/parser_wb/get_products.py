import re
from parser_wb.schema import Product
from bs4 import BeautifulSoup
import itertools
from parser_wb import logger, config
from db.db_wb import add_product
from text_recognizer.main import recognize_text
import requests
from chrome_driver import driver

def parse_page(publication_category, url):
    logger.info('Start parse_page')
    logger.info('Downloading pages')
    pages = [get_html(url.split('?')[0] + '?page=' + str(i) + '&' + url.split('?')[1].split('&', 1)[1]) for i in range(config.START_PAGE, config.MAX_PAGES + 1)]
    logger.info('Parsing product links from pages')
    urls = list(itertools.chain(*[parse_urls(p) for p in pages]))
    logger.info('Starting products parsing')
    if len(urls) == 0:
        logger.warning('Со страницы не распарсилось ни одной ссылки!')
    else:
        for url in urls:
            if urls.index(url) > config.MAX_PARSED_PRODUCTS:
                break
            else:
                product = parse_product(url, publication_category)
                if product is not None:
                    logger.info('Adding product to DB')
                    if not config.DEBUG:
                        add_product(product)
                    else:
                        logger.info("Not commiting to DB cuz of debug")

        logger.info('Done get_products_from_page. Success!')
    return 'End'


def get_html(url):
    logger.info('Start get_html')
    logger.info(f'Viewing {url}')
    driver.get(url)
    driver.execute_script("window.scrollTo(5,4000);")
    import time
    time.sleep(5)
    html = driver.page_source
    logger.info('End get_html')
    return html

def parse_urls(html):
    logger.info('Start parse_urls')
    soup = BeautifulSoup(html, 'html.parser')
    product_links = set([a.get('href').split('?')[0] for a in list(
        itertools.chain(*[div.find_all('a') for div in soup.find('div').find_all(attrs={'class', 'product-card__wrapper'})]))])
    print(product_links)
    logger.info('End parse_urls')
    return product_links

def get_basket(product_article):
    _short_id = int(product_article) // 100000
    if 0 <= _short_id <= 143:
        return '01'
    elif 144 <= _short_id <= 287:
        return '02'
    elif 288 <= _short_id <= 431:
        return '03'
    elif 432 <= _short_id <= 719:
        return '04'
    elif 720 <= _short_id <= 1007:
        return '05'
    elif 1008 <= _short_id <= 1061:
        return '06'
    elif 1062 <= _short_id <= 1115:
        return '07'
    elif 1116 <= _short_id <= 1169:
        return '08'
    elif 1170 <= _short_id <= 1313:
        return '09'
    elif 1314 <= _short_id <= 1601:
        return '10'
    elif 1602 <= _short_id <= 1655:
        return '11'
    elif 1656 <= _short_id <= 1919:
        return '12'
    elif 1920 <= _short_id <= 2045:
        return '13'
    elif 2046 <= _short_id <= 2189:
        return '14'
    elif 2190 <= _short_id <= 2405:
        return '15'
    else:
        return '16'

def try_get_article(url):
    logger.info('Start try_get_article')
    try:
        article = re.search(r'(\d+)', url)[0]
        logger.info('End try_get_article')
        return article
    except Exception as e:
        logger.warning(f'Ошибка! {e}')
    return
def try_get_jsons(article):
    logger.info('Start try_get_jsons')
    json_product = json_card = {}
    try:
        basket = get_basket(article)

        response_product = requests.get(
            url=f'https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1255987&spp=30&ab_testid=reranking_1&nm={article}')

        json_product = response_product.json().get('data')['products'][0]
        response_card = requests.get(
            url=f"https://basket-{basket}.wbbasket.ru/vol{int(article) // 100000}/part{int(article) // 1000}/{article}/info/ru/card.json")

        json_card = response_card.json()
        logger.info('End try_get_jsons')
        return json_product, json_card
    except Exception as e:
        logger.warning(f'Ошибка! {e}')
    return json_product, json_card

def try_parse_product_info(json_product, json_card):
    product_name = ''
    product_price_original = ''
    product_price = ''
    product_brand_name = ''
    product_rating = ''
    product_categories = ''
    product_sizes = ''
    product_color = ''
    product_article = ''
    product_all_articles = ''
    description = ''
    count_of_images = ''

    try:
        product_article = json_product["id"]

        product_brand_name = json_product["brand"]

        product_color = json_product["colors"][0]["name"]

        product_name = json_product["name"]

        product_rating = json_product["reviewRating"]

        for size in json_product["sizes"]:
            product_sizes += size['name'] + ', '

        for size in json_product["sizes"]:
            if 'price' in size:
                product_price_original = str(size['price']['basic'] // 100) + ' ₽'
                product_price = str(size['price']['product'] // 100) + ' ₽'
                break

        count_of_images = json_product['pics']

        description = json_card['description']

        for article in json_card['full_colors']:
            product_all_articles += str(article['nm_id']) + ', '

        product_categories = json_card['subj_name'] + ' ' + json_card['subj_root_name']

        return product_article, product_brand_name, product_color, product_name, product_rating, product_sizes, \
                product_price_original, product_price, count_of_images, description, product_all_articles, product_categories

    except KeyError as e:
        logger.warning(f'Не удалост найти поле {e} у товара')

    return product_article, product_brand_name, product_color, product_name, product_rating, product_sizes, \
                product_price_original, product_price, count_of_images, description, product_all_articles, product_categories



def try_parse_images(product_article, count_of_images):
    product_images = ''
    basket = get_basket(product_article)
    try:
        product_images = ", ".join([
            f"https://basket-{basket}.wbbasket.ru/vol{int(product_article) // 100000}/part{int(product_article) // 1000}/{product_article}/images/big/{i}.webp"
            for i in range(1, count_of_images + 1)])
        return product_images
    except KeyError as e:
        logger.warning(f'Не удалост найти поле {e} у товара')
    return product_images


def validate_product(product: Product):
    if product.name == '':
        logger.warning('Отсутствует поле product_name')
        return
    if product.price == '':
        logger.warning('Отсутствует поле product_price')
        return
    if product.images == '':
        logger.warning('Отсутствует поле product_images')
        return
    if product.article == '':
        logger.warning('Отсутствует поле product_article')
        return
    if product.rating == '':
        logger.warning('Отсутствует поле product_rating')
        return
    if float(product.rating) < config.PRODUCT_RATING_THRESHOLD:
        logger.warning(f'Рейтинг ниже порога {product.rating} < {config.PRODUCT_RATING_THRESHOLD}')
        return
    if len(product.images.split(', ')) < 3:
        logger.warning('Изображений меньше 3 штук')
        return
    return product

def parse_product(url, publication_category):
    logger.info('Start parse_product')
    logger.info(f'Parsing product with url: {url}')

    article = try_get_article(url)

    if article is not None:
        json_product, json_card = try_get_jsons(article)

        if json_product != {} and json_card != {}:
            product_article, product_brand_name, product_color, product_name, product_rating, product_sizes, \
                product_price_original, product_price, count_of_images, description, product_all_articles, \
                product_categories = try_parse_product_info(json_product, json_card)

            sub_category = product_name.partition(' ')[0]

            product_images = try_parse_images(article, count_of_images)
            product_images = ', '.join([recognize_text(image_url) for image_url in product_images.split(',')
                                        if recognize_text(image_url) != None])

            print(f'product_name: {product_name}, \n'
                  f'product_rating: {product_rating}, \n'
                  f'product_article: {product_article}, \n'
                  f'description: {description}, \n'
                  f'product_price_original: {product_price_original}, \n'
                  f'product_price: {product_price}, \n'
                  f'product_images: {product_images}, \n'
                  f'product_brand_name: {product_brand_name}, \n'
                  f'product_categories: {product_categories}, \n'
                  f'product_all_articles: {product_all_articles}, \n'
                  f'product_color: {product_color}, \n'
                  f'product_sizes: {product_sizes}, \n')

            product = validate_product(Product(
                0,
                product_name,
                product_price_original,
                product_price,
                product_images,
                product_brand_name,
                product_rating,
                product_categories,
                product_sizes,
                product_color,
                product_article,
                product_all_articles,
                url,
                publication_category,
                description,
                sub_category
            ))

            if not product:
                logger.info(f'Product validation failed')
            else:
                logger.info(f'Done parsing product')
            logger.info('End parse_product')
            return product
