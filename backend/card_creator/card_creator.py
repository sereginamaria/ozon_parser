import io
from urllib.request import urlopen

from flask import render_template
from html2image import Html2Image
from colorthief import ColorThief

from backend.parser.schema import Product
import os

def create_triple_card(product: Product, front: bool) -> bytes:
    def get_html(product_name, product_article, product_price, palette):
        return render_template('triple_card.html', name=product_name, article=product_article,
                               price=product_price,
                               color1=palette[0],
                               color2=palette[2])
    def get_css(images_urls, palette):
        if front:
            return render_template('triple_card.css', url_img1=images_urls[1],
                               url_img2=images_urls[2],
                               url_img3=images_urls[3],
                               color=palette[2])
        else:
            return render_template('triple_card.css', url_img1=images_urls[0],
                               url_img2=images_urls[1],
                               url_img3=images_urls[2],
                               color=palette[2])

    print(product)
    print(product.images)
    images_urls = product.images.split(',')
    print(images_urls)
    print(images_urls[0])
    palette = get_palette(images_urls)
    print(palette)

    html = get_html(product.name, product.article, product.price, palette)
    css = get_css(images_urls, palette)
    return screenshot_html(html, css)


def create_title_card(product: Product) -> bytes:
    def get_html(product_name, product_category, palette):
        if product_category == 'Верхняя Одежда' or product_category == 'Кофта':
            card_title = product_name.partition(' ')[0]
        else:
            card_title = product_category
        return render_template('title_card.html', category=card_title,
                               color1=palette[0],
                               color2=palette[2])
    def get_css(images_urls, palette):
        return render_template('title_card_.css', url_img=images_urls[0], color=palette[2])


    images_urls = product.images.split(',')
    palette = get_palette(images_urls)

    html = get_html(product.name, product.article, palette)
    css = get_css(images_urls, palette)
    return screenshot_html(html, css)

def screenshot_html(html, css) -> bytes:
    hti = Html2Image(
        output_path='card_creator/cards',
        custom_flags=[
            '--no-sandbox',
            '--disable-gpu',
            '--remote-allow-origins=*',
            '--hide-scrollbars'
        ],
    )
    # hti.load_file("card_creator/templates/logo1.png", "logo.png")
    path = hti.screenshot(
        html_str=html, css_str=css, size=(1024, 1280)
    )[0]

    image_b = open(path, 'rb').read()
    os.remove(path)
    return image_b

def get_palette(images_urls):
    fd = urlopen(images_urls[0])
    f = io.BytesIO(fd.read())
    fd.close()
    color_thief = ColorThief(f)
    return color_thief.get_palette(color_count=2, quality=2)