from bs4 import BeautifulSoup
import itertools
from get_product import get_product
import telegram_notifier
from parser import logger, driver
import config


def get_products_from_page(publication_category, url):
    logger.info('Starting get_products_from_page')
    telegram_notifier.send_wait()
    urls = []
    logger.info('Starting parsing products urls')
    for i in range(1, config.MAX_PAGES+1):
        html = get_html(url + '?page=' + str(i))
        urls.extend(parse_urls(html))
    logger.info('Starting products parsing')
    for url in urls:
        get_product(url, publication_category)

    # parser_requests.send_execution_completed(message_type)
    # print('End get_products_from_page')


def get_html(url):
    logger.info(f'Downloading {url}')

    logger.info('Viewing page')
    driver.get(url)
    driver.execute_script("window.scrollTo(5,4000);")
    html = driver.page_source
    driver.close()
    driver.quit()
    return html


def parse_urls(html):
    logger.info('Parsing URLs')
    soup = BeautifulSoup(html, 'html.parser')
    product_links = set([a.get('href').split('?')[0] for a in list(
        itertools.chain(*[div.find_all('a') for div in soup.find('div').find_all(attrs={'class', 'wi3'})]))])
    return product_links
