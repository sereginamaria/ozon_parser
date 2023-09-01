from flask import render_template
from html2image import Html2Image
from card_creator import card_creator_requests

def card_creator(product_list):
    global nomer, files, media_list
    nomer = 1

    print('lisy')
    print(product_list)
    print(type(product_list))
    print(len(product_list))

    if product_list:
        files = {}
        media_list = []
        for product in product_list:
            if nomer == 11 or nomer == 21:
                card_creator_requests.send_media_group(media_list, files)
                files = {}
                media_list = []

            product_id, product_name, product_article, product_sizes, product_price, product_price_with_ozon_card, product_images = product

            render_html = html_render(product_name, product_article, product_sizes, product_price, product_price_with_ozon_card)
            render_css = css_render(product_images)
            card(render_html, render_css)

            name = f'photo{nomer}'

            files.update({name: open("card_creator/cards/card" + str(nomer) + ".png", "rb")})

            media_list.append(dict(type='photo', media=f'attach://{name}'))

            nomer+=1

        card_creator_requests.send_media_group(media_list, files)

def card(html, css):
    hti = Html2Image(
        output_path='card_creator/cards',
        custom_flags=[
            '--no-sandbox'
            '--remote-allow-origins=*',
            '--hide-scrollbars'
        ],
    )

    hti.screenshot(
        html_str=html, css_str=css,
        save_as='card' + str(nomer) + '.png', size=(1024, 1280)
    )



def html_render(product_name, product_article, product_sizes, product_price, product_price_with_ozon_card):
    return render_template('card.html', name=product_name, article=product_article, size=product_sizes, price=product_price,
                           ozon_card_price=product_price_with_ozon_card)


def css_render(product_images):

    product_image = product_images.split(',')

    return render_template('card.css', url_img1=product_image[0],
                           url_img2=product_image[1],
                           url_img3=product_image[2])
