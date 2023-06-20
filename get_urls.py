from bs4 import BeautifulSoup
import itertools
import glob
from get_product_json import get_product_json

def get_pages() -> list:
    return glob.glob('pages/*.html')

def get_html(page: str):
    with open(page, 'r', encoding='utf-8') as f:
        return f.read()

def parse_data(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    product_links = set([a.get('href').split('?')[0] for a in list(itertools.chain(*[div.find_all('a') for div in soup.find('div').find_all(attrs={'class', 'io6'})]))])

    from pprint import pprint
    # print(len(product_links))
    # print()
    # pprint(product_links)


    # print(links)
    return product_links

def get_urls():
    pages = get_pages()

    all_links = []

    for page in pages:
        html = get_html(page)
        # print(html)
        links = parse_data(html)

        all_links = all_links + list(links)

    # print(all_links)
    # print(len(all_links))

    with open('product_links.txt', 'w', encoding='utf-8') as f:
        for link in all_links:
            # print(link)
            # print(type(link))
            get_product_json(link)
            # f.write(link + '\n')
        # print('1234')

