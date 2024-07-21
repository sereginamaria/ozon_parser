from backend.parser import logger, config, driver
import re
import json
import time

from backend.parser.schema import Product
from bs4 import BeautifulSoup
import itertools
# from parser.db import add_product

def parse_page(publication_category, url):
    logger.info('Start parse pages')
    logger.info('Downloading pages')
    pages = [get_html(url + '?page=' + str(i)) for i in range(1, config.MAX_PAGES + 1)]
    logger.info('Parsing product links from pages')
    print(pages)
    urls = list(itertools.chain(*[parse_urls(p) for p in pages]))
    logger.info('Starting products parsing')


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