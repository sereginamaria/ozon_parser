import undetected_chromedriver
from selenium.webdriver.common.by import By
import time
import json
from pprint import pprint


def get_product_json(url):
    driver = undetected_chromedriver.Chrome()
    driver.get("https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=" + url)
    # time.sleep(1)

    content = driver.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
    parsed_json = json.loads(content)
    parsed_data_json = parsed_json["widgetStates"]

    keys_to_save1 = ['webCharacteristics-545750-default-1', 'webBrand-1033259-default-1',
                         'webAspects-418189-default-1',
                         'breadCrumbs-1619260-default-1',
                         'webOzonAccountPrice-2136009-default-1', 'webGallery-1748356-default-1',
                         'webCurrentSeller-735663-default-1', 'webPrice-2136014-default-1',
                         'webProductHeading-943795-default-1']

    keys_to_save2 = ['breadcrumbs', 'aspects', 'id', 'name', 'link', 'characteristics', 'mainAdvantages', 'images',
                     'marks', 'textRs', 'priceTextRs', 'originalPrice', 'price', 'title']

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
    # pprint(d2)

    with open('product_json.json', 'w', encoding="utf-8") as outfile:
        outfile.write(json.dumps(d2, indent=4, sort_keys=True, ensure_ascii=False, separators=(',', ': ')))

