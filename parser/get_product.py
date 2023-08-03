import undetected_chromedriver
from selenium.webdriver.common.by import By
import json
from parser.add_to_db import add_to_db
from datetime import date


def get_product(url):
    print('hello')
    print(type(url))
    print(url)

    driver = undetected_chromedriver.Chrome()
    driver.get("https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=" + url)
    # time.sleep(1)

    content = driver.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
    parsed_json = json.loads(content)
    parsed_data_json = parsed_json["widgetStates"]

    # pprint(parsed_data_json)
    keys_to_save1 = ['webCharacteristics-545750-default-1', 'webBrand-1033259-default-1',
                     'webAspects-418189-default-1',
                     'breadCrumbs-1619260-default-1', 'webGallery-1748356-default-1',
                     'webCurrentSeller-735663-default-1', 'webPrice-2111817-default-1',
                     'webProductHeading-943795-default-1']

    keys_to_save2 = ['breadcrumbs', 'aspects', 'id', 'name', 'link', 'characteristics', 'mainAdvantages', 'images',
                     'marks', 'textRs', 'priceTextRs', 'originalPrice', 'price', 'cardPrice', 'title']

    keys_to_save3 = ['text', 'priceTextRs', 'content', 'description', 'name', 'alt', 'src', 'mainAdvantages', 'short',
                     'variants']

    d1 = {k: json.loads(v) for k, v in parsed_data_json.items() if k in keys_to_save1}
    d2 = {}

    for k1, v1 in d1.items():
        d2[k1] = {}
        for k2, v2 in v1.items():
            if k2 not in keys_to_save2:
                continue
            if type(v2) == list:
                d2[k1][k2] = []
                for object in v2:
                    if type(object) == dict:
                        for k3, v3 in object.items():
                            if k3 in keys_to_save3:
                                d2[k1][k2].append({k3: v3})

            else:
                d2[k1][k2] = v2
    # pprint(d2['webProductHeading-943795-default-1']['title'])
    # pprint(d2)

    product_name = ''
    product_price_original = ''
    product_price = ''
    product_price_with_ozon_card = ''

    if 'webProductHeading-943795-default-1' in d2:
        if 'title' in d2['webProductHeading-943795-default-1']:
            product_name = d2['webProductHeading-943795-default-1']['title']

    if 'webPrice-2111817-default-1' in d2:
        if 'originalPrice' in d2['webPrice-2111817-default-1']:
            product_price_original = d2['webPrice-2111817-default-1']['originalPrice']
        if 'price' in d2['webPrice-2111817-default-1']:
            product_price = d2['webPrice-2111817-default-1']['price']
        if 'cardPrice' in d2['webPrice-2111817-default-1']:
            product_price_with_ozon_card = d2['webPrice-2111817-default-1']['cardPrice']

    product_images = ''
    if 'webGallery-1748356-default-1' in d2:
        if 'images' in d2['webGallery-1748356-default-1']:
            for object in d2['webGallery-1748356-default-1']['images']:
                for k, v in object.items():
                    if k == 'src':
                        product_images += v + ', '

    product_brand_name = ''
    product_brand_link = ''
    if 'webCurrentSeller-735663-default-1' in d2:
        if 'name' in d2['webCurrentSeller-735663-default-1']:
            product_brand_name = d2['webCurrentSeller-735663-default-1']['name']

    if 'webCurrentSeller-735663-default-1' in d2:
        if 'link' in d2['webCurrentSeller-735663-default-1']:
            product_brand_link = d2['webCurrentSeller-735663-default-1']['link']

    product_rating = ''
    if 'webCurrentSeller-735663-default-1' in d2:
        if 'mainAdvantages' in d2['webCurrentSeller-735663-default-1']:
            product_rating = d2['webCurrentSeller-735663-default-1']['mainAdvantages'][0]['content']['headRs'][0][
                'content']

    product_categories = ''
    if 'breadCrumbs-1619260-default-1' in d2:
        if 'breadcrumbs' in d2['breadCrumbs-1619260-default-1']:
            for object in d2['breadCrumbs-1619260-default-1']['breadcrumbs']:
                for k, v in object.items():
                    product_categories += v + ', '

    product_article = ''
    product_all_articles = ''
    product_color = ''
    product_sizes = ''
    if 'webAspects-418189-default-1' in d2:
        if 'aspects' in d2['webAspects-418189-default-1']:
            if len(d2['webAspects-418189-default-1']['aspects']) == 3:
                for object in d2['webAspects-418189-default-1']['aspects'][1]['variants']:
                    for k, v in object.items():
                        if k == 'sku':
                            product_all_articles += str(v) + ', '
                        if k == 'link' and v.split('?')[0] == url:
                            for k1, v1 in object.items():
                                if k1 == 'sku':
                                    product_article = v1
                                if k1 == 'data':
                                    product_color = v1['searchableText']
                for object in d2['webAspects-418189-default-1']['aspects'][2]['variants']:
                    for k, v in object.items():
                        if k == 'data':
                            product_sizes += v['searchableText'] + ', '
            if len(d2['webAspects-418189-default-1']['aspects']) == 2:
                for object in d2['webAspects-418189-default-1']['aspects'][0]['variants']:
                    for k, v in object.items():
                        if k == 'sku':
                            product_all_articles += str(v) + ', '
                        if k == 'link' and v.split('?')[0] == url:
                            for k1, v1 in object.items():
                                if k1 == 'sku':
                                    product_article = v1
                                if k1 == 'data':
                                    product_color = v1['searchableText']
                for object in d2['webAspects-418189-default-1']['aspects'][1]['variants']:
                    for k, v in object.items():
                        if k == 'data':
                            product_sizes += v['searchableText'] + ', '
            if len(d2['webAspects-418189-default-1']['aspects']) == 1:
                for object in d2['webAspects-418189-default-1']['aspects'][0]['variants']:
                    for k, v in object.items():
                        if k == 'data':
                            product_sizes += v['searchableText'] + ', '
                        if k == 'link' and v.split('?')[0] == url:
                            for k1, v1 in object.items():
                                if k1 == 'sku':
                                    product_article = v1

    # print(d2['webPrice-2136014-default-1']['originalPrice'])

    add_date = date.today()
    add_to_db(
        product_name,
        product_price_original,
        product_price,
        product_price_with_ozon_card,
        product_images,
        product_brand_name,
        product_brand_link,
        product_rating,
        product_categories,
        product_color,
        product_article,
        product_sizes,
        product_all_articles,
        add_date
    )

    with open('../parser/product_json.json', 'w', encoding="utf-8") as outfile:
        outfile.write(json.dumps(d2, indent=4, sort_keys=True, ensure_ascii=False, separators=(',', ': ')))
