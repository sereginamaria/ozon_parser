import re
import json
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from backend.parser.schema import Product
from bs4 import BeautifulSoup
import itertools
from backend.parser import logger, driver, config
from backend.db.db import add_product

def parse_page(publication_category, url):
    logger.info('Start parse pages')
    logger.info('Downloading pages')
    pages = [get_html(url + '?page=' + str(i)) for i in range(1, config.MAX_PAGES + 1)]
    logger.info('Parsing product links from pages')
    urls = list(itertools.chain(*[parse_urls(p) for p in pages]))
    logger.info('Starting products parsing')
    products = []
    for url in urls:
        product = parse_product(url, publication_category)
        if product is not None:
            products.append(product)

    logger.info('Adding products to DB')
    for p in products:
        if not config.DEBUG:
            add_product(p)
        else:
            logger.info("Not commiting to DB cuz of debug")
    # telegram_notifier.send_execution_completed()
    logger.info('Done get_products_from_page. Success!')


def get_html(url):
    logger.info('Start get_html')
    logger.info(f'Viewing {url}')
    driver.get(url)
    driver.execute_script("window.scrollTo(5,4000);")
    import time
    time.sleep(5)
    html = driver.page_source
    return html

def parse_urls(html):
    logger.info('Parsing URLs')
    soup = BeautifulSoup(html, 'html.parser')
    product_links = set([a.get('href').split('?')[0] for a in list(
        itertools.chain(*[div.find_all('a') for div in soup.find('div').find_all(attrs={'class', 'j0j_23'})]))])
    return product_links


def find_nonempty_widget(parsed_widget_states, widget):
    if re.search(f'{widget}-[^":]*', parsed_widget_states) != None:
        return re.search(f'{widget}-[^":]*', parsed_widget_states).group(0)
    else:
        return None

def try_parse_seo(parsed_json):
    product_name = ''
    product_rating = ''
    product_article = ''
    description = ''
    try:
        seo_html = json.loads(parsed_json["seo"]["script"][0]['innerHTML'])
        product_name = seo_html['name'].replace("'", "")
        product_rating = seo_html['aggregateRating']['ratingValue']
        product_article = seo_html['sku']
        description = seo_html['description']
    except KeyError as e:
        logger.warning(f'Не удалост найти поле {e} у товара')
    return product_name, product_rating, product_article, description

def try_parse_price(webPrice, parsed_json):
    product_price_original = ''
    product_price = ''
    product_price_with_ozon_card = ''

    try:
        parsed_widget_states = parsed_json["widgetStates"]
        if webPrice in parsed_widget_states:
            if 'originalPrice' in json.loads(parsed_widget_states[webPrice]):
                product_price_original = json.loads(parsed_widget_states[webPrice])['originalPrice']
            if 'price' in json.loads(parsed_widget_states[webPrice]):
                product_price = json.loads(parsed_widget_states[webPrice])['price']
            if 'cardPrice' in json.loads(parsed_widget_states[webPrice]):
                product_price_with_ozon_card = json.loads(parsed_widget_states[webPrice])['originalPrice']

            if product_price == '':
                seo_html = json.loads(parsed_json["seo"]["script"][0]['innerHTML'])
                product_price = seo_html['offers']['price'] + ' ₽'
    except KeyError:
        logger.warning("Cannot get product price")
    return product_price_original, product_price, product_price_with_ozon_card


def try_parse_images(webGallery, parsed_widget_states):
    product_images = ''

    try:
        if webGallery in parsed_widget_states:
            if 'images' in json.loads(parsed_widget_states[webGallery]):
                for item in json.loads(parsed_widget_states[webGallery])['images']:
                    for k, v in item.items():
                        if k == 'src':
                            product_images += v + ', '
    except KeyError:
        logger.warning("Cannot get product images")
    return product_images

def try_parse_brand(webStickyProducts, parsed_widget_states):
    product_brand_name = ''
    product_brand_link = ''

    try:
        if webStickyProducts in parsed_widget_states:
            if 'seller' in json.loads(parsed_widget_states[webStickyProducts]):
                if 'name' in json.loads(parsed_widget_states[webStickyProducts])['seller']:
                    product_brand_name = json.loads(parsed_widget_states[webStickyProducts])['seller']['name']
                if 'link' in json.loads(parsed_widget_states[webStickyProducts])['seller']:
                    product_brand_link = json.loads(parsed_widget_states[webStickyProducts])['seller']['link']
    except KeyError:
        logger.warning("Cannot get product brand")
    return product_brand_name, product_brand_link

def try_parse_categories(breadCrumbs, parsed_widget_states):
    product_categories = ''

    try:
        if breadCrumbs in parsed_widget_states:
            if 'breadcrumbs' in json.loads(parsed_widget_states[breadCrumbs]):
                for item in json.loads(parsed_widget_states[breadCrumbs])['breadcrumbs']:
                    for k, v in item.items():
                        if k == 'text':
                            product_categories += v + ', '
    except KeyError:
        logger.warning("Cannot get product categories")
    return product_categories

def try_parse_web_aspects(webAspects, parsed_widget_states, product_article):
    product_all_articles = ''
    product_color = ''
    product_sizes = ''

    try:
        if webAspects in parsed_widget_states:
            if 'aspects' in json.loads(parsed_widget_states[webAspects]):
                if len(json.loads(parsed_widget_states[webAspects])['aspects']) >= 3:
                    for item in json.loads(parsed_widget_states[webAspects])['aspects'][0]['variants']:
                        for k, v in item.items():
                            if k == 'sku':
                                if str(v) == product_article:
                                    for k1, v1 in item.items():
                                        if k1 == 'data':
                                            product_color = v1['searchableText']
                    for item in json.loads(parsed_widget_states[webAspects])['aspects'][1]['variants']:
                        for k, v in item.items():
                            if k == 'sku':
                                product_all_articles += str(v) + ', '
                    for item in json.loads(parsed_widget_states[webAspects])['aspects'][2]['variants']:
                        for k, v in item.items():
                            if k == 'data':
                                product_sizes += v['searchableText'] + ', '
                if len(json.loads(parsed_widget_states[webAspects])['aspects']) == 2:
                    for item in json.loads(parsed_widget_states[webAspects])['aspects'][0]['variants']:
                        for k, v in item.items():
                            if k == 'sku':
                                product_all_articles += str(v) + ', '
                                if str(v) == product_article:
                                    for k1, v1 in item.items():
                                        if k1 == 'data':
                                            product_color = v1['searchableText']
                    for item in json.loads(parsed_widget_states[webAspects])['aspects'][1]['variants']:
                        for k, v in item.items():
                            if k == 'data':
                                product_sizes += v['searchableText'] + ', '
                if len(json.loads(parsed_widget_states[webAspects])['aspects']) == 1:
                    for item in json.loads(parsed_widget_states[webAspects])['aspects'][0]['variants']:
                        for k, v in item.items():
                            if k == 'data':
                                product_sizes += v['searchableText'] + ', '
    except KeyError:
        logger.warning("Cannot get product web aspects")
    return product_all_articles, product_color, product_sizes

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
    if float(product.rating.replace(',', '.')) < config.PRODUCT_RATING_THRESHOLD:
        logger.warning(f'Рейтинг ниже порога {product.rating} < {config.PRODUCT_RATING_THRESHOLD}')
        return
    return product

def parse_product(url, publication_category):
    logger.info(f'Parsing url: {url}')
    driver.get(config.PRODUCT_PAGE_ENTRYPOINT + url)
    time.sleep(5)  # TODO
    try:
        content = driver.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
    except NoSuchElementException:
        logger.warning(f"Cannot get product data: {url}")
        return

    parsed_json = json.loads(content)

    logger.info('Parse seo')
    product_name, product_rating, product_article, description = try_parse_seo(parsed_json)

    logger.info('Parse widgets')
    parsed_widget_states = parsed_json["widgetStates"]
    raw_widget_states = json.dumps(parsed_widget_states)

    widgets_for_search = ['webGallery', 'webAspects', 'breadCrumbs', 'webPrice',
                          'webProductHeading', 'webStickyProducts']

    webGallery, webAspects, breadCrumbs, webPrice, webProductHeading, webStickyProducts = \
        [find_nonempty_widget(raw_widget_states, widget) for widget in widgets_for_search]

    product_price_original, product_price, product_price_with_ozon_card = try_parse_price(webPrice, parsed_json)

    product_images = try_parse_images(webGallery, parsed_widget_states)

    product_brand_name, product_brand_link = try_parse_brand(webStickyProducts, parsed_widget_states)

    product_categories = try_parse_categories(breadCrumbs, parsed_widget_states)

    product_all_articles, product_color, product_sizes = try_parse_web_aspects(webAspects, parsed_widget_states, product_article)

    print(product_name, product_rating, product_article, description, product_price_original, product_price, product_price_with_ozon_card,
          product_images, product_brand_name, product_brand_link, product_categories, product_all_articles, product_color, product_sizes)

    sub_category = product_name.partition(' ')[0]

    product = validate_product(Product(
        product_name,
        product_price_original,
        product_price,
        product_price_with_ozon_card,
        product_images,
        product_brand_name,
        product_brand_link,
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
    return product
