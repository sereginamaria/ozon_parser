from bs4 import BeautifulSoup
import itertools
from get_product import parse_product
import telegram_notifier
from parser import logger, driver
import config
from db import add_product


def get_products_from_page(publication_category, url):
    logger.info('Starting get_products_from_page')
    if not config.DEBUG:
        telegram_notifier.send_wait()
    logger.info('Downloading pages')
    pages = [get_html(url + '?page=' + str(i)) for i in range(1, config.MAX_PAGES+1)]
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
    telegram_notifier.send_execution_completed()
    logger.info('Done get_products_from_page. Success!')


def get_html(url):
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
        itertools.chain(*[div.find_all('a') for div in soup.find('div').find_all(attrs={'class', 'iv4'})]))])
    if not product_links:
        logger.warning("Empty links parsed from HTML, probably got stuck on CloudFlare:" + html)
    return product_links
