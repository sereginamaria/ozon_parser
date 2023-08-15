import requests
from flask import render_template
from html2image import Html2Image
import json

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"


def card_creator(product_list):
    product_list = json.loads(product_list)
    print('lisy')
    print(product_list)
    print(type(product_list))


    # print(product_list)
    # print(type(product_list))
    # list = product_list.split(';')
    # print(list)
    # print(type(list))
    # print(list[0])
    # print(type(list[0]))

    if product_list:
        for product in product_list:
            product_id, product_images = product
            print(product)
            print(product_id)
            print(product_images)
    # if product_list:
    #     for product in product_list:
    #         product_id, product_name = product
    #         render_html = html_render(product_id, product_name)
    #         render_css = css_render()
    #         card(render_html, render_css)

            # print(product_id)
            # print(product_images)
            # print(type(product_id))
            # print(product_images.split(','))

            # product_image = str(product_image[0]).split(',')


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

    files = {'photo': open("card_creator/card.png", "rb")}
    requests.post(
        url=telegram_url + '/sendPhoto',
        data={'chat_id': 6181726421}, files=files
    )


def html_render(product_id, product_name):
    return render_template('card.html', name=product_name, article=product_id)


def css_render():
    return render_template('card.css', url_img1='https://cdn1.ozone.ru/s3/multimedia-a/6685787134.jpg',
                           url_img2='https://cdn1.ozone.ru/s3/multimedia-a/6685787134.jpg',
                           url_img3='https://cdn1.ozone.ru/s3/multimedia-a/6685787134.jpg')
