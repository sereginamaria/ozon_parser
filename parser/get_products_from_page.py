from bs4 import BeautifulSoup
import itertools
from get_product import get_product
import telegram_notifier
from parser import logger, driver
import config


def get_products_from_page(publication_category, url):
    logger.info('Starting get_products_from_page')
    # telegram_notifier.send_wait()
    logger.info('Downloading pages')
    pages = [get_html(url + '?page=' + str(i)) for i in range(1, config.MAX_PAGES+1)]
    logger.info('Parsing product links from pages')
    urls = list(itertools.chain(*[parse_urls(p) for p in pages]))
    logger.info('Starting products parsing')
    for url in urls:
        get_product(url, publication_category)

    # parser_requests.send_execution_completed(message_type)
    # print('End get_products_from_page')


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
        itertools.chain(*[div.find_all('a') for div in soup.find('div').find_all(attrs={'class', 'wi3'})]))])
    return product_links
