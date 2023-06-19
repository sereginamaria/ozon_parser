from bs4 import BeautifulSoup
import itertools
import glob

def get_pages() -> list:
    return glob.glob('pages/*.html')

def get_html(page: str):
    with open(page, 'r', encoding='utf-8') as f:
        return f.read()

def parse_data(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    links = []

    # print(soup)
    products = soup.find('div')
    products2 = set([a.get('href') for a in list(itertools.chain(*[div.find_all('a') for div in products.find_all(attrs={'class', 'io6'})]))])
    # from pprint import pprint
    # print(len(products2))
    # print()
    # pprint(products2)
    products3 = products.find_all('a')
    # products3 = products2.find_all('a')
    # products3 = products.find_all('a')
    # print('products')
    # print(products3)
    # with open('soup.txt', 'w', encoding='utf-8') as f:
    #         f.write(soup)
    # for product in products:
    #     links.append(product.get('href').split('?')[0])
    #
    for product in products3:
        links.append(product.get('href'))

    # print(links)
    return set(links)

def main():
    pages = get_pages()

    all_links = []

    for page in pages:
        html = get_html(page)
        # print(html)
        links = parse_data(html)

        all_links = all_links + list(links)

    # print(all_links)
    # print(len(all_links))

    # with open('product_links.txt', 'w', encoding='utf-8') as f:
        # for link in all_links:
            # print(link)
            # print(type(link))
            # f.write(link)


if __name__ == '__main__':
    main()