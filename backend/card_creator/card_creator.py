import io
from urllib.request import urlopen

from flask import render_template
from html2image import Html2Image
from colorthief import ColorThief

from ozon_parser.schema import Product
from card_creator import logger
import os
from text_recognizer.main import recognize_text

def create_triple_card(product: Product, front: bool) -> bytes:
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

    print('create_card')
    print(images_urls[0])
    recognize_text(images_urls[0])
    palette = get_palette(images_urls)

    html = get_html(product.name, product.article, product.price, palette)
    css = get_css(images_urls, palette)
    logger.info('End create_triple_card')
    return screenshot_html(html, css)


def create_title_card(product: Product) -> bytes:
    def get_html(product_category, palette_colors):
        card_title = product_category
        return render_template('title_card.html', category=card_title,
                               color1=palette_colors[0],
                               color2=palette_colors[2])
    def get_css(images_urls, palette_colors):
        return render_template('title_card.css', url_img=images_urls[0], color=palette_colors[2])

    logger.info('Start create_title_card')
    images_urls = product.images.split(',')
    palette = get_palette(images_urls)

    html = get_html(product.publication_category, palette)
    css = get_css(images_urls, palette)
    logger.info('End create_title_card')
    return screenshot_html(html, css)

def screenshot_html(html, css) -> bytes:
    hti = Html2Image(
        custom_flags=[
            '--no-sandbox',
            '--disable-gpu',
            '--remote-allow-origins=*',
            '--hide-scrollbars'
        ],
    )

    hti.load_file('../card_creator/templates/logo.png', "logo.png")
    path = hti.screenshot(
        html_str=html, css_str=css, size=(1024, 1280)
    )[0]

    image_b = open(path, 'rb').read()
    os.remove(path)
    return image_b

def get_palette(images_urls):
    try:
        fd = urlopen(images_urls[0])
        f = io.BytesIO(fd.read())
        fd.close()
        color_thief = ColorThief(f)
        return color_thief.get_palette(color_count=2, quality=2)
    except KeyError:
        logger.warning("Can't get palette")
