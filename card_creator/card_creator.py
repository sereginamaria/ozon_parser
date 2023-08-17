import requests
from flask import render_template
from html2image import Html2Image
import json

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"


def card_creator(product_list):
    print('lisy')
    print(product_list)
    print(type(product_list))

    if product_list:
        for product in product_list:
            product_name, product_article, product_sizes, product_price, product_price_with_ozon_card, product_images = product
            render_html = html_render(product_name, product_article, product_sizes, product_price, product_price_with_ozon_card)
            render_css = css_render(product_images)
            card(render_html, render_css)



    # render_html = html_render()
    # render_css = css_render()
    # card(render_html, render_css)


def card(html, css):
    hti = Html2Image(
        output_path='card_creator/',
        custom_flags=[
            '--no-sandbox'
            '--remote-allow-origins=*',
            '--hide-scrollbars'
        ],
    )

    hti.screenshot(
        html_str=html, css_str=css,
        save_as='card.png', size=(1024, 1280)
    )
    #
    # from telebot.types import InputMediaPhoto
    # pic2 = open("card_creator/card.png", "rb")
    # media = []
    # media += InputMediaPhoto(pic2)
    files = []
    files += {'photo': open("card_creator/card.png", "rb")}
    requests.post(
        url=telegram_url + '/sendMediaGroup',
        data={'chat_id': 6181726421}, files=files
    )


def html_render(product_name, product_article, product_sizes, product_price, product_price_with_ozon_card):
    return render_template('card.html', name=product_name, article=product_article, size=product_sizes, price=product_price,
                           ozon_card_price=product_price_with_ozon_card)


def css_render(product_images):
    print(product_images.split(','))

    product_image = str(product_images[0]).split(',')
    print(product_image)
    return render_template('card.css', url_img1=str(product_images[0]).split(','),
                           url_img2=str(product_images[1]).split(','),
                           url_img3=str(product_images[2]).split(','))
