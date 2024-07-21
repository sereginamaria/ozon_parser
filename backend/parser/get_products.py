import re
import json
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from backend.parser.schema import Product
from bs4 import BeautifulSoup
import itertools
from backend.parser import logger, driver, config
# from backend.parser.db import add_product

def parse_page(publication_category, url):
    logger.info('Start parse pages')
    logger.info('Downloading pages')
    pages = [get_html(url + '?page=' + str(i)) for i in range(1, config.MAX_PAGES + 1)]
    logger.info('Parsing product links from pages')
    print(pages)
    urls = list(itertools.chain(*[parse_urls(p) for p in pages]))
    logger.info('Starting products parsing')
    products = []
    for url in urls:
        product = parse_product(url, publication_category)
        if product is not None:
            products.append(product)

    # logger.info('Adding products to DB')
    # for p in products:
    #     if not config.DEBUG:
    #         add_product(p)
    #     else:
    #         logger.info("Not commiting to DB cuz of debug")
    # # telegram_notifier.send_execution_completed()
    # logger.info('Done get_products_from_page. Success!')


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
    if re.search(f'{widget}[^":]*', parsed_widget_states) != None:
        return re.search(f'{widget}[^":]*', parsed_widget_states).group(0)
    else:
        return None

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

    parsed_widget_states = json.dumps(parsed_json["widgetStates"])

    widgets_for_search = ['webGallery', 'webCharacteristics', 'webAspects', 'breadCrumbs', 'webPrice',
                          'webProductHeading', 'webStickyProducts']

    webGallery, webCharacteristics, webAspects, breadCrumbs, webPrice, webProductHeading, webStickyProducts = \
        [find_nonempty_widget(parsed_widget_states, widget) for widget in widgets_for_search]



    seo_json = parsed_json["seo"]["script"]

    d0 = json.loads(seo_json[0]['innerHTML'])

    description = d0['description']
    product_rating = d0['aggregateRating']['ratingValue']
    product_article = d0['sku']





    seo_html, description, product_rating, product_article = try_parse_seo(parsed_json)




    keys_to_save_lvl1 = [webGallery, webAspects, webCharacteristics, breadCrumbs, webPrice, webProductHeading,
                         webStickyProducts]

    raw_widgets = {k: json.loads(v) for k, v in parsed_widget_states.items() if k in keys_to_save_lvl1}
    clean_widgets = clear_widgets(raw_widgets)

    product_name = try_parse_product_name(webProductHeading, clean_widgets)
    product_price_original, product_price, product_price_with_ozon_card = try_parse_price(webPrice, clean_widgets,
                                                                                          seo_html)
