import time
import random

import undetected_chromedriver as uc
from undetected_chromedriver import ChromeOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import re
import json
from parser_local.add_to_db_local import add_to_db

# from parser import parser_requests

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"


def get_product(url, publication_category, message_type):
    global content
    print('Start get_product')

    options1 = uc.ChromeOptions()
    options1.headless = False
    # options1.add_argument('--headless')
    # options1.add_argument('--headless=new')
    options1.add_argument('--no-sandbox')
    options1.add_argument('--disable-dev-shm-usage')

    options1.add_argument("--disable-extensions")
    options1.add_argument('--disable-application-cache')
    options1.add_argument("--disable-setuid-sandbox")
    options1.add_argument("--disable-gpu")
    options1.add_argument("--remote-allow-origins=*")
    # options1.add_argument("--log-path=/home/masha/chromelogs")
    options1.add_argument("--disable-dev-shm-usage")
    options1._session = None

    # options1.binary_location = '/home/masha/ozon_parser/chromedriver/chrome-linux64/chrome'
    # options1.binary_location = '/home/masha/ozon_parser/chromedriver/chrome117/chrome-linux64/chrome'
    # options1.binary_location = '/home/masha/ozon_parser/chromedriver/chrome-headless-shell-linux64/chrome-headless-shell'
    print('before Chrome')

    driver1 = uc.Chrome(
        # driver_executable_path='/home/masha/ozon_parser/chromedriver/chromedriver-linux64/chromedriver',
        patcher_force_close=True, no_sandbox=True, suppress_welcome=True, use_subprocess=False,
        options=options1,
        log_level=10, headless=False)

    print('get')
    print(url)
    driver1.get("https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=" + url)
    time.sleep(5)
    print('get ok')

    html = driver1.page_source
    # print(html)

    # WebDriverWait(driver1, 20).until(EC.frame_to_be_available_and_switch_to_it(
    #     (By.CSS_SELECTOR, "iframe[title='Widget containing a Cloudflare security challenge']")))
    # WebDriverWait(driver1, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.ctp-checkbox-label"))).click()

    # time.sleep(30)

    # print('new html')
    # html = driver1.page_source
    # print(html)

    # print(driver1.current_url)

    # driver1.save_screenshot('5.png')

    try:
        print('try start')
        # driver1.save_screenshot('6.png')
        content = driver1.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')

        print('content')
        # print(content)
        print("Content is not empty")
    except:
        try:
            print('Content is empty')
            driver1.save_screenshot('7.png')
            driver1.refresh()
            # time.sleep(10)
            driver1.save_screenshot('8.png')
            content = driver1.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
        except:
            print(
                'В процессе парсинга произошла ошибка, не удалось получить tag_name pre. Запустите парсер заново.')

    driver1.close()
    driver1.quit()

    # options1 = Options()
    # options1.add_argument('--no-sandbox')
    # options1.add_argument('--disable-dev-shm-usage')
    # # options1.add_argument("start-maximized")
    # options1.add_argument("--headless=new")
    # options1.add_argument("--disable-blink-features=AutomationControlled")
    # # options1.add_experimental_option("excludeSwitches", ["enable-automation"])
    # # options1.add_experimental_option('useAutomationExtension', False)
    # # options1.headless = True

    # driver1 = uc.Chrome(options=options1, version_main=117)

    # driver1.get("https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=" + url)
    # time.sleep(10)

    # content = driver1.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
    # # content = driver1.find_element(By.TAG_NAME, 'body')
    # print(content)
    # driver1.close()
    # driver1.quit()

    parsed_json = json.loads(content)

    parsed_data_json = parsed_json["widgetStates"]
    seo_json = ''
    if 'script' in parsed_json["seo"]:
        seo_json = parsed_json["seo"]["script"]


    print(seo_json)
    print(seo_json[0])
    print(type(seo_json[0]))
    d0 = ''
    if seo_json != '':
        d0 = json.loads(seo_json[0]["innerHTML"])

    description = ''
    product_rating = ''
    product_article = ''
    if d0 != '':
        description = d0['description']

        product_rating = ''
        if 'aggregateRating' in d0:
            product_rating = d0['aggregateRating']['ratingValue']
        product_article = d0['sku']


    # OLD, does not exist
    # 'webBrand-1033259-default-1'
    # webCurrentSeller-735663-default-1'

    webGallery = ''
    webCharacteristics = ''
    webAspects = ''
    breadCrumbs = ''
    webPrice = ''
    webProductHeading = ''
    webStickyProducts = ''


    if re.search('webGallery[^":]*', json.dumps(parsed_data_json)) != None:
        webGallery = re.search('webGallery[^":]*', json.dumps(parsed_data_json)).group(0)

    if re.search('webCharacteristics[^":]*', json.dumps(parsed_data_json)) != None:
        webCharacteristics = re.search('webCharacteristics[^":]*', json.dumps(parsed_data_json)).group(0)

    if re.search('webAspects[^":]*', json.dumps(parsed_data_json)) != None:
        webAspects = re.search('webAspects[^":]*', json.dumps(parsed_data_json)).group(0)

    if re.search('breadCrumbs[^":]*', json.dumps(parsed_data_json)) != None:
        breadCrumbs = re.search('breadCrumbs[^":]*', json.dumps(parsed_data_json)).group(0)

    if re.search('webPrice[^":]*', json.dumps(parsed_data_json)) != None:
        webPrice = re.search('webPrice[^":]*', json.dumps(parsed_data_json)).group(0)

    if re.search('webProductHeading[^":]*', json.dumps(parsed_data_json)) != None:
        webProductHeading = re.search('webProductHeading[^":]*', json.dumps(parsed_data_json)).group(0)

    if re.search('webStickyProducts[^":]*', json.dumps(parsed_data_json)) != None:
        webStickyProducts = re.search('webStickyProducts[^":]*', json.dumps(parsed_data_json)).group(0)



    # print(webAspects)
    # print(re.search('webAspects[^":]*', json.dumps(parsed_data_json)) != None)
    # print('webaspects')
    # print(seo_json)

    keys_to_save1 = [webGallery, webAspects, webCharacteristics, breadCrumbs, webPrice, webProductHeading,
                     webStickyProducts]

    keys_to_save2 = ['breadcrumbs', 'aspects', 'id', 'name', 'link', 'characteristics', 'mainAdvantages', 'images',
                     'marks', 'textRs', 'priceTextRs', 'originalPrice', 'price', 'cardPrice', 'title', 'seller']

    keys_to_save3 = ['text', 'priceTextRs', 'content', 'description', 'name', 'alt', 'src', 'mainAdvantages', 'short',
                     'variants', 'name', 'link', ]

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

    # print('d2')
    # print(d2)

    # print(bool(d2))

    product_name = ''
    product_price_original = ''
    product_price = ''
    product_price_with_ozon_card = ''

    if webProductHeading in d2:
        if 'title' in d2[webProductHeading]:
            product_name = d2[webProductHeading]['title']

    rem_char = "'"
    product_name.replace(rem_char, "")

    if webPrice in d2:
        if 'originalPrice' in d2[webPrice]:
            product_price_original = d2[webPrice]['originalPrice']
        if 'price' in d2[webPrice]:
            product_price = d2[webPrice]['price']
        if 'cardPrice' in d2[webPrice]:
            product_price_with_ozon_card = d2[webPrice]['cardPrice']

    if product_price == '':
        product_price = d0['offers']['price'] + ' ₽'

    if publication_category == 'Мужчинам':
        sub_category = 'Мужчинам'
    else:
        sub_category = product_name.partition(' ')[0]

    if sub_category == 'Толстовка':
        sub_category = 'Худи'

    product_images = ''
    if webGallery in d2:
        if 'images' in d2[webGallery]:
            for object in d2[webGallery]['images']:
                for k, v in object.items():
                    if k == 'src':
                        product_images += v + ', '

    few_photos = False
    if len(product_images.split(',')) <= 2:
        few_photos = True

    product_brand_name = ''
    product_brand_link = ''
    if webStickyProducts in d2:
        # print(d2[webStickyProducts])
        # print(d2[webStickyProducts]['seller'])
        if 'seller' in d2[webStickyProducts]:
            if 'name' in d2[webStickyProducts]['seller']:
                product_brand_name = d2[webStickyProducts]['seller']['name']

    if webStickyProducts in d2:
        # print(d2[webStickyProducts])
        # print(d2[webStickyProducts]['seller'])

        if 'seller' in d2[webStickyProducts]:
            if 'link' in d2[webStickyProducts]['seller']:
                product_brand_link = d2[webStickyProducts]['seller']['link']

    product_categories = ''
    if breadCrumbs in d2:
        if 'breadcrumbs' in d2[breadCrumbs]:
            for object in d2[breadCrumbs]['breadcrumbs']:
                for k, v in object.items():
                    product_categories += v + ', '


    product_all_articles = ''
    product_color = ''
    product_sizes = ''

    if webAspects in d2 and webAspects != '':
        if 'aspects' in d2[webAspects]:
            if len(d2[webAspects]['aspects']) >= 3:
                for object in d2[webAspects]['aspects'][1]['variants']:
                    for k, v in object.items():
                        if k == 'sku':
                            product_all_articles += str(v) + ', '
                        if k == 'link' and v.split('?')[0] == url:
                            for k1, v1 in object.items():
                                if k1 == 'data':
                                    product_color = v1['searchableText']
                for object in d2[webAspects]['aspects'][2]['variants']:
                    for k, v in object.items():
                        if k == 'data':
                            product_sizes += v['searchableText'] + ', '
            if len(d2[webAspects]['aspects']) == 2:
                for object in d2[webAspects]['aspects'][0]['variants']:
                    for k, v in object.items():
                        if k == 'sku':
                            product_all_articles += str(v) + ', '
                        if k == 'link' and v.split('?')[0] == url:
                            for k1, v1 in object.items():
                                if k1 == 'data':
                                    product_color = v1['searchableText']
                for object in d2[webAspects]['aspects'][1]['variants']:
                    for k, v in object.items():
                        if k == 'data':
                            product_sizes += v['searchableText'] + ', '
            if len(d2[webAspects]['aspects']) == 1:
                for object in d2[webAspects]['aspects'][0]['variants']:
                    for k, v in object.items():
                        if k == 'data':
                            product_sizes += v['searchableText'] + ', '

    print('product_rating')
    print(product_rating)

    if product_rating != '' and product_article != '':
        if float(product_rating.replace(',', '.')) >= float('4.4'):
            print('Go to add_to_db')
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
                publication_category,
                few_photos,
                url,
                description,
                sub_category
            )

    else:
        if product_article == '':
            print('Отсутствует поле product_article')
        if product_rating == '':
            print('Отсутствует поле product_rating')

    # with open('parser/product_json.json', 'w', encoding="utf-8") as outfile:
    #     outfile.write(json.dumps(d2, indent=4, sort_keys=True, ensure_ascii=False, separators=(',', ': ')))

    print('End get_product')


if __name__ == '__main__':




    get_product('/product/kanistra-bar-1292523882/', '23 Февраля', False)


