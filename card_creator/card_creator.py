from flask import render_template
from html2image import Html2Image
from card_creator import card_creator_requests

def card_creator(product_list):
    print('create_card')
    rerq = create_card(product_list, 'without_title')
    print(rerq)

    print('media_list')
    print(rerq[0])
    print(rerq[1])

    card_creator_requests.send_media_group(rerq[0], rerq[1])


def post_creator(product_list):
    print('create_post')
    rerq = create_card(product_list, 'with_title')
    print(rerq)


    card_creator_requests.send_post(rerq[0], rerq[1], rerq[2], rerq[3], rerq[4])
def create_card(product_list, mess):
    global nomer, files, media_list, urls_list, publication_category
    nomer = 1
    make_title = False
    print('lisy')
    print(product_list)
    print(type(product_list))
    print(len(product_list))
    files = {}
    media_list = []

    publication_category = ''

    names_list = []
    urls_list = []
    if product_list:
        for product in product_list:
            print(product)
            if nomer == 11 or nomer == 21:
                card_creator_requests.send_media_group(media_list, files)
                files = {}
                media_list = []

            (product_id, product_name, product_article, product_sizes, product_price,
             product_price_with_ozon_card, product_images, publication_category, product_url) = product

            if mess == 'with_title' and make_title == False:
                name = f'photo{nomer}'
                print('with_title')
                render_title_html = title_html_render(publication_category)
                render_title_css = title_css_render(product_images)
                card(render_title_html, render_title_css)
                make_title = True
                files.update({name: open("card_creator/cards/card" + str(nomer) + ".png", "rb")})
                media_list.append(dict(type='photo', caption='', parse_mode='HTML', media=f'attach://{name}'))
                nomer += 1

            name = f'photo{nomer}'
            render_html = html_render(product_name, product_article, product_sizes, product_price,
                                      product_price_with_ozon_card)

            render_css = css_render(product_images)
            card(render_html, render_css)


            urls_list.append(product_url)
            names_list.append(product_name)
            files.update({name: open("card_creator/cards/card" + str(nomer) + ".png", "rb")})

            if nomer == 1:
                media_list.append(dict(type='photo', caption='', parse_mode = 'HTML', media=f'attach://{name}'))
            else:
                media_list.append(dict(type='photo', media=f'attach://{name}'))

            nomer += 1

    return media_list, files, publication_category, names_list, urls_list

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


def title_html_render(category):
    return render_template('title_card.html', category=category)


def title_css_render(product_images):

    product_image = product_images.split(',')

    return render_template('title_card.css', url_img=product_image[0])
