import io
from urllib.request import urlopen

from flask import render_template
from html2image import Html2Image
from colorthief import ColorThief

from parser.schema import Product
import os


def create_titled_card(product: Product) -> bytes:
    def get_html(product_name, category, palette):
        if category == 'Верхняя Одежда' or category == 'Обувь' or category == 'Кофта' or category == 'Аксессуары':
            card_title = product_name.partition(' ')[0]
        else:
            card_title = category
        return render_template('title_card_single_photo.html', category=card_title,
                               color1=palette[0],
                               color2=palette[2])

    def get_css(product_images, palette):
        product_image = product_images.split(',')

        return render_template('title_card_single_photo.css', url_img=product_image[0], color=palette[2])

    images_urls = product.images.split(',')
    fd = urlopen(images_urls[0])
    f = io.BytesIO(fd.read())
    fd.close()
    color_thief = ColorThief(f)
    palette = color_thief.get_palette(color_count=2, quality=2)

    html = get_html(product.name, product.publication_category, palette)
    css = get_css(product.images, palette)
    return screenshot_html(html, css)


def create_triple_card(product: Product, front: bool) -> bytes:
    def get_html(product_name, product_article, product_sizes, product_price,
                 product_price_with_ozon_card, palette):
        product_size = product_sizes.split(' ,')

        if len(product_name) > 30:
            product_name = product_name.partition(' ')[0]

        del product_size[-1]

        string = ''
        for el in product_size:
            # Добавляем к строке элемент списка
            string += str(el)
            # Добавляем к строке разделитель — в данном случае пробел
            string += ', '
        new_string = string[:-1]

        return render_template('card.html', name=product_name, article=product_article,
                               size=new_string, price=product_price,
                               ozon_card_price=product_price_with_ozon_card,
                               color1=palette[0],
                               color2=palette[2])

    def get_css(product_images, palette, front):
        product_image = product_images.split(',')

        if front:
            return render_template('card.css', url_img1=product_image[1],
                                   url_img2=product_image[2],
                                   url_img3=product_image[3],
                                   color=palette[2])
        else:
            return render_template('card.css', url_img1=product_image[0],
                                   url_img2=product_image[1],
                                   url_img3=product_image[2],
                                   color=palette[2])

    images_urls = product.images.split(',')
    fd = urlopen(images_urls[0])
    f = io.BytesIO(fd.read())
    fd.close()
    color_thief = ColorThief(f)
    # dominant_color = color_thief.get_color(quality=1)
    palette = color_thief.get_palette(color_count=2, quality=2)
    html = get_html(product.name, product.article, product.sizes, product.price,
                    product.price_with_ozon_card, palette)
    css = get_css(product.images, palette, front)
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
    hti.load_file("card_creator/templates/logo1.png", "logo.png")
    path = hti.screenshot(
        html_str=html, css_str=css, size=(1024, 1280)
    )[0]

    image_b = open(path, 'rb').read()
    os.remove(path)
    return image_b
