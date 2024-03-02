import re
import json
from selenium.common import NoSuchElementException
from parser import driver, config
from parser import logger
from selenium.webdriver.common.by import By
from schema import Product


def clear_widgets(raw_widgets):
    clean_widgets = {}

    keys_to_save_lvl2 = ['breadcrumbs', 'aspects', 'id', 'name', 'link', 'characteristics', 'mainAdvantages', 'images',
                         'marks', 'textRs', 'priceTextRs', 'originalPrice', 'price', 'cardPrice', 'title', 'seller']

    keys_to_save_lvl3 = ['text', 'priceTextRs', 'content', 'description', 'name', 'alt', 'src', 'mainAdvantages',
                         'short',
                         'variants', 'name', 'link']

    for k1, v1 in raw_widgets.items():
        clean_widgets[k1] = {}
        for k2, v2 in v1.items():
            if k2 not in keys_to_save_lvl2:
                continue
            if type(v2) == list:
                clean_widgets[k1][k2] = []
                for object in v2:
                    if type(object) == dict:
                        for k3, v3 in object.items():
                            if k3 in keys_to_save_lvl3:
                                clean_widgets[k1][k2].append({k3: v3})

            else:
                clean_widgets[k1][k2] = v2
    return clean_widgets


def find_nonempty_widget(raw_widgets, widget):
    if re.search(f'{widget}[^":]*', raw_widgets) != None:
        return re.search(f'{widget}[^":]*', raw_widgets).group(0)
    else:
        return None


def try_parse_seo(parsed_json):
    seo_html = ''
    description = ''
    product_rating = ''
    product_article = ''
    try:
        seo_json = parsed_json["seo"]["script"]
        seo_html = json.loads(seo_json[0]['innerHTML'])
        description = seo_html['description']
        product_rating = seo_html['aggregateRating']['ratingValue']
        product_article = seo_html['sku']
    except KeyError as e:
        logger.warning(f'Не удалост найти поле {e} у товара')
    return seo_html, description, product_rating, product_article


def try_parse_product_name(web_product_heading, clean_widgets):
    try:
        if web_product_heading in clean_widgets:
            if 'title' in clean_widgets[web_product_heading]:
                product_name = clean_widgets[web_product_heading]['title'].replace("'", "")
                return product_name
    except KeyError:
        logger.warning('Cannot get product name')
    return ''


def try_parse_price(web_price, clean_widgets, seo_html):
    product_price_original = ''
    product_price = ''
    product_price_with_ozon_card = ''
    try:
        if web_price in clean_widgets:
            if 'originalPrice' in clean_widgets[web_price]:
                product_price_original = clean_widgets[web_price]['originalPrice']
            if 'price' in clean_widgets[web_price]:
                product_price = clean_widgets[web_price]['price']
            if 'cardPrice' in clean_widgets[web_price]:
                product_price_with_ozon_card = clean_widgets[web_price]['cardPrice']
            if product_price == '':
                product_price = seo_html['offers']['price'] + ' ₽'
    except KeyError:
        logger.warning("Cannot get product price")
    return product_price_original, product_price, product_price_with_ozon_card


def try_parse_images(web_gallery, clean_widgets):
    product_images = ''
    try:
        if web_gallery in clean_widgets:
            if 'images' in clean_widgets[web_gallery]:
                for object in clean_widgets[web_gallery]['images']:
                    for k, v in object.items():
                        if k == 'src':
                            product_images += v + ', '
    except KeyError:
        logger.warning("Cannot get product image")
    return product_images


def try_parse_product_brand(webSticky_products, clean_widgets):
    product_brand_name = ''
    product_brand_link = ''
    try:
        if webSticky_products in clean_widgets:
            if 'seller' in clean_widgets[webSticky_products]:
                if 'name' in clean_widgets[webSticky_products]['seller']:
                    product_brand_name = clean_widgets[webSticky_products]['seller']['name']

        if webSticky_products in clean_widgets:
            if 'seller' in clean_widgets[webSticky_products]:
                if 'link' in clean_widgets[webSticky_products]['seller']:
                    product_brand_link = clean_widgets[webSticky_products]['seller']['link']
    except KeyError as e:
        logger.warning(f'Cannot get product brand: {e}')
    return product_brand_name, product_brand_link


def try_parse_product_categories(breadcrumbs, clean_widgets):
    product_categories = ''
    try:
        if breadcrumbs in clean_widgets:
            if 'breadcrumbs' in clean_widgets[breadcrumbs]:
                for o in clean_widgets[breadcrumbs]['breadcrumbs']:
                    for k, v in o.items():
                        product_categories += v + ', '
    except KeyError:
        logger.warning('Cannot parse product categories')
    return product_categories


def validate_product(product: Product):
    if product.article == '':
        logger.warning('Отсутствует поле product_article')
        return
    if product.rating == '':
        logger.warning('Отсутствует поле product_rating')
        return
    if float(product.rating.replace(',', '.')) < config.PRODUCT_RATING_THRESHOLD:
        logger.warning(f'Рейтинг ниже порога {product.rating} < {config.PRODUCT_RATING_THRESHOLD}')
        return
    return product


def try_parse_web_aspects(web_aspects, clean_widgets, url):
    product_all_articles = ''
    product_color = ''
    product_sizes = ''

    try:
        if web_aspects in clean_widgets and web_aspects != '':
            if 'aspects' in clean_widgets[web_aspects]:
                if len(clean_widgets[web_aspects]['aspects']) >= 3:
                    for o in clean_widgets[web_aspects]['aspects'][1]['variants']:
                        for k, v in o.items():
                            if k == 'sku':
                                product_all_articles += str(v) + ', '
                            if k == 'link' and v.split('?')[0] == url:
                                for k1, v1 in o.items():
                                    if k1 == 'data':
                                        product_color = v1['searchableText']
                    for o in clean_widgets[web_aspects]['aspects'][2]['variants']:
                        for k, v in o.items():
                            if k == 'data':
                                product_sizes += v['searchableText'] + ', '
                if len(clean_widgets[web_aspects]['aspects']) == 2:
                    for o in clean_widgets[web_aspects]['aspects'][0]['variants']:
                        for k, v in o.items():
                            if k == 'sku':
                                product_all_articles += str(v) + ', '
                            if k == 'link' and v.split('?')[0] == url:
                                for k1, v1 in o.items():
                                    if k1 == 'data':
                                        product_color = v1['searchableText']
                    for o in clean_widgets[web_aspects]['aspects'][1]['variants']:
                        for k, v in o.items():
                            if k == 'data':
                                product_sizes += v['searchableText'] + ', '
                if len(clean_widgets[web_aspects]['aspects']) == 1:
                    for o in clean_widgets[web_aspects]['aspects'][0]['variants']:
                        for k, v in o.items():
                            if k == 'data':
                                product_sizes += v['searchableText'] + ', '
    except KeyError as e:
        logger.warning(f'Cannot parse webAspects(articles, sizes, color): {e}')
    return product_all_articles, product_color, product_sizes


def parse_product(url, publication_category):
    logger.info(f'Parsing product {url}')
    driver.get(config.PRODUCT_PAGE_ENTRYPOINT + url)

    try:
        content = driver.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
    except NoSuchElementException:
        logger.warning(f"Cannot get product data: {url}")
        return

    parsed_json = json.loads(content)
    parsed_widget_states = parsed_json["widgetStates"]
    raw_widget_states = json.dumps(parsed_widget_states)
    seo_html, description, product_rating, product_article = try_parse_seo(parsed_json)

    widgets_for_search = ['webGallery', 'webCharacteristics', 'webAspects', 'breadCrumbs', 'webPrice',
                        'webProductHeading', 'webStickyProducts']
    webGallery, webCharacteristics, webAspects, breadCrumbs, webPrice, webProductHeading, webStickyProducts = \
        [find_nonempty_widget(raw_widget_states, w) for w in widgets_for_search]

    keys_to_save_lvl1 = [webGallery, webAspects, webCharacteristics, breadCrumbs, webPrice, webProductHeading,
                         webStickyProducts]

    raw_widgets = {k: json.loads(v) for k, v in parsed_widget_states.items() if k in keys_to_save_lvl1}
    clean_widgets = clear_widgets(raw_widgets)

    product_name = try_parse_product_name(webProductHeading, clean_widgets)
    product_price_original, product_price, product_price_with_ozon_card = try_parse_price(webPrice, clean_widgets,
                                                                                          seo_html)

    if publication_category == 'Мужчинам':
        sub_category = 'Мужчинам'
    else:
        sub_category = product_name.partition(' ')[0]

    product_images = try_parse_images(webGallery, clean_widgets)

    few_photos = False if len(product_images.split(',')) <= 4 else True

    product_brand_name, product_brand_link = try_parse_product_brand(webStickyProducts, clean_widgets)

    product_categories = try_parse_product_categories(breadCrumbs, clean_widgets)

    product_all_articles, product_color, product_sizes = try_parse_web_aspects(webAspects, clean_widgets, url)

    product = validate_product(Product(
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
    ))
    if not product:
        logger.info(f'Product validation failed')
    else:
        logger.info(f'Done parsing product')
    return product
