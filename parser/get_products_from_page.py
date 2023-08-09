from typing import Any
import undetected_chromedriver
import time
from bs4 import BeautifulSoup
import itertools
from parser.get_product import get_product
import requests

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"

def get_products_from_page(url):
    # Ограничим парсинг первыми n страницами
    print('hello')
    MAX_PAGE = 1
    i = 1
    while i <= MAX_PAGE:
        if i == 1:
            get_html(url)
        else:
            url_param = url + '?page=' + str(i)
            get_html(url_param)
        i += 1


def get_html(url):
    print('get_html')
    driver = undetected_chromedriver.Chrome()
    driver.get(url)
    time.sleep(3)
    driver.execute_script("window.scrollTo(5,4000);")
    # time.sleep(5)
    html = driver.page_source
    get_urls(html)
    driver.close()
    driver.quit()


def parse_data(html: str) -> set[Any]:
    print('parse_data')
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    product_links = set([a.get('href').split('?')[0] for a in list(
        itertools.chain(*[div.find_all('a') for div in soup.find('div').find_all(attrs={'class', 'oi2'})]))])
    return product_links


def get_urls(html):
    print('get_urls')
    all_links = []
    links = parse_data(html)
    all_links = all_links + list(links)

    print(all_links)
    print(len(all_links))
    if len(all_links) == 36:
        for link in all_links:
            print('get_product')
            get_product(link)
    else:
        print('ERROR')
        requests.post(
            url=telegram_url + '/sendMessage',
            data={'chat_id': 6181726421, 'text': 'Ошибка! Со страницы определилось ' + str(len(all_links)) +
                      ' ссылок. Повторите попытку.'}
        ).json()