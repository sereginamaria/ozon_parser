import io
from urllib.request import urlopen

from flask import render_template
from html2image import Html2Image
from colorthief import ColorThief

from parser_ozon.schema import Product
from cards_module import logger
import os

def create_triple_card(product: Product, front: bool, card_type: str) -> bytes:
    def get_html(product_name, product_article, product_price, palette_colors):
        return render_template('triple_card.html', name=product_name, article=product_article,
                               price=product_price,
                               color1=palette_colors[0],
                               color2=palette_colors[2])
    def get_css(images_urls, palette_colors):
        if front:
            return render_template('triple_card.css', url_img1=images_urls[1],
                               url_img2=images_urls[2],
                               url_img3=images_urls[3],
                               color=palette_colors[2])
        else:
            return render_template('triple_card.css', url_img1=images_urls[0],
                               url_img2=images_urls[1],
                               url_img3=images_urls[2],
                               color=palette_colors[2])

    logger.info('Start create_triple_card')
    images_urls = product.images.split(',')
    palette = get_palette(images_urls[0])

    html = get_html(product.name, product.article, product.price, palette)
    css = get_css(images_urls, palette)
    logger.info('End create_triple_card')
    return screenshot_html(html, css, card_type)

def create_duo_card(products: [], front: bool, card_type: str) -> bytes:
    def get_html(names, articles, prices, palette_colors1, palette_colors2):
        return render_template('duo_card.html',
                               name1=names[0], name2=names[1],
                               article1=articles[0], article2=articles[1],
                               price1=prices[0], price2=prices[1],
                               color10=palette_colors1[0], color12=palette_colors1[2],
                               color20=palette_colors2[0], color22=palette_colors2[2], type=card_type
                               )
    def get_css(images, palette_colors2):
            return render_template('duo_card.css', url_img1=images_urls[0],
                                   url_img2=images[1],
                                   color1=palette_colors2[2], color2=palette_colors2[2])

    logger.info('Start create_triple_card')
    print(products)
    images_urls = [product.images.split(',')[0] for product in products]

    # if front:
    #     images_urls = []
    #     images_urls.append(products[0].images.split(',')[1])
    #     images_urls.append(products[1].images.split(',')[0])
    # else:
    #     images_urls = [product.images.split(',')[0] for product in products]

    products_names = [product.sub_category for product in products]
    products_articles = [product.article for product in products]
    products_prices = [product.price for product in products]

    # images_urls = product.images.split(',')
    palette1 = get_palette(images_urls[0])
    palette2 = get_palette(images_urls[1])

    html = get_html(products_names, products_articles, products_prices, palette1, palette2)
    css = get_css(images_urls, palette2)
    logger.info('End create_triple_card')
    return screenshot_html(html, css, card_type)

def create_title_card(product: Product, card_type: str) -> bytes:
    def get_html(product_category, palette_colors, bp):
        card_title = product_category
        return render_template('title_card.html', category=card_title,
                               color1=palette_colors[0],
                               color2=palette_colors[2], card_type=card_type, background_position=bp)
    def get_css(images_urls, palette_colors):
        return render_template('title_card.css',
                               url_img=images_urls[0], color=palette_colors[2])

    logger.info('Start create_title_card')
    images_urls = product.images.split(',')
    palette = get_palette(images_urls[0])

    background_position = 'center'
    if (product.publication_category == 'Обувь' or product.publication_category == 'Брюки' or
        product.publication_category == 'Джинсы'):
        background_position = 'bottom'

    html = get_html(product.publication_category, palette, background_position)
    css = get_css(images_urls, palette)
    logger.info('End create_title_card')
    return screenshot_html(html, css, card_type)

def create_stiled_card(products, card_type: str) -> bytes:
    def get_html(names, articles, prices):
        return render_template('stile_card.html',
                               name1=names[0], name2=names[1],
                               name3=names[2], name4=names[3],
                               article1=articles[0], article2=articles[1],
                               article3=articles[2], article4=articles[3],
                               price1=prices[0], price2=prices[1],
                               price3=prices[2], price4=prices[3], type=card_type
                               )

    def get_css(images):
        return render_template('stile_card.css', url_img1=images[0],
                               url_img2=images[1],
                               url_img3=images[2],
                               url_img4=images[3])

    logger.info('Start create_stile_card')
    images_urls = [product.images.split(',')[0] for product in products]
    products_names = [product.sub_category for product in products]
    products_articles = [product.article for product in products]
    products_prices = [product.price for product in products]

    print(images_urls)

    html = get_html(products_names, products_articles, products_prices)
    css = get_css(images_urls)
    logger.info('End create_stile_card')
    return screenshot_html(html, css, card_type)


def screenshot_html(html, css, card_type) -> bytes:
    hti = Html2Image(
        custom_flags=[
            '--no-sandbox',
            '--disable-gpu',
            '--remote-allow-origins=*',
            '--hide-scrollbars'
        ],
    )

    logger.info('screen')
    import os
    print(os.getcwd())
    logger.info(os.getcwd())
    path = ''
    if card_type == 'ozon':
        hti.load_file('./cards_module/templates/logo_ozon.png', "logo.png")
        path = hti.screenshot(
            html_str=html, css_str=css, size=(1024, 1280), save_as='ozon.png'
        )[0]

    if card_type == 'wb':
        print('wb')
        hti.browser.flags = ["--no-sandbox", "--disable-gpu"]
        hti.load_file('./cards_module/templates/logo_wb.png', "logo.png")
        path = hti.screenshot(
            html_str=html, css_str=css, size=(1024, 1280), save_as='wb.png'
        )[0]

    print(path)

    image_b = open(path, 'rb').read()
    os.remove(path)

    return image_b

def get_palette(images_urls):
    try:
        fd = urlopen(images_urls)
        f = io.BytesIO(fd.read())
        fd.close()
        color_thief = ColorThief(f)
        return color_thief.get_palette(color_count=2, quality=2)
    except KeyError:
        logger.warning("Can't get palette")
