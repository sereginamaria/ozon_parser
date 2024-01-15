import io
from urllib.request import urlopen

from flask import render_template
from html2image import Html2Image
from card_creator import card_creator_requests
from colorthief import ColorThief

def card_creator(product_list):
    print('Start create_card')
    rerq = create_card(product_list, 'without_title')
    card_creator_requests.send_media_group(rerq[0], rerq[1])
    # return rerq


def post_creator(product_list):
    print('Start create_post')
    rerq = create_card(product_list, 'with_title')
    card_creator_requests.send_post(rerq[0], rerq[1], rerq[2], rerq[3], rerq[4])



def create_card(product_list, mess):
    global nomer, files, media_list, urls_list, publication_category
    nomer = 1
    make_title = False
    files = {}
    media_list = []

    publication_category = ''

    names_list = []
    urls_list = []
    if product_list:
        for product in product_list:
            if nomer == 11 or nomer == 21:
                card_creator_requests.send_media_group(media_list, files)
                files = {}
                media_list = []
                names_list = []
                urls_list = []

            (product_id, product_name, product_article, product_sizes, product_price,
             product_price_with_ozon_card, product_images, publication_category, product_url) = product


            product_image = product_images.split(',')
            fd = urlopen(product_image[0])
            f = io.BytesIO(fd.read())
            fd.close()
            color_thief = ColorThief(f)
            # dominant_color = color_thief.get_color(quality=1)
            palette = color_thief.get_palette(color_count=2, quality=2)

            if mess == 'with_title' and make_title == False:
                name = f'photo{nomer}'

                # product_image = product_images.split(',')
                # fd = urlopen(product_image[0])
                # f = io.BytesIO(fd.read())
                # fd.close()
                # color_thief = ColorThief(f)
                # # get the dominant color
                # # dominant_color = color_thief.get_color(quality=2)
                # # build a color palette
                # dominant_color = color_thief.get_palette(color_count=2, quality=2)
                # print('palette1')


                render_title_html = title_html_render(product_name, publication_category, palette)
                render_title_css = title_css_render(product_images, palette)
                card(render_title_html, render_title_css)
                make_title = True
                files.update({name: open("card_creator/cards/card" + str(nomer) + ".png", "rb")})
                media_list.append(dict(type='photo', caption='', parse_mode='HTML', media=f'attach://{name}'))
                nomer += 1

            name = f'photo{nomer}'

            # product_image = product_images.split(',')
            # fd = urlopen(product_image[0])
            # f = io.BytesIO(fd.read())
            # fd.close()
            # color_thief = ColorThief(f)
            # # get the dominant color
            # dominant_color = color_thief.get_color(quality=1)
            # # build a color palette
            # # palette = color_thief.get_palette(color_count=3)
            # print('palette')
            # print(dominant_color)

            render_html = html_render(product_name, product_article, product_sizes, product_price,
                                      product_price_with_ozon_card, palette)
            render_css = css_render(product_images, palette)
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
    hti.load_file("card_creator/templates/logo1.png", "logo.png")
    hti.screenshot(
        html_str=html, css_str=css,
        save_as='card' + str(nomer) + '.png', size=(1024, 1280)
    )



def html_render(product_name, product_article, product_sizes, product_price,
                product_price_with_ozon_card, palette):
    product_size = product_sizes.split(' ,')

    del product_size[-1]

    string = ''
    for el in product_size:
        # Добавляем к строке элемент списка
        string += str(el)
        # Добавляем к строке разделитель — в данном случае пробел
        string += ', '
    new_string = string[:-1]
    print(new_string)

    return render_template('card.html', name=product_name, article=product_article,
                           size=new_string, price=product_price,
                           ozon_card_price=product_price_with_ozon_card,
                           color1=palette[0],
                           color2=palette[2])


def css_render(product_images, palette):

    product_image = product_images.split(',')

    return render_template('card.css', url_img1=product_image[1],
                           url_img2=product_image[2],
                           url_img3=product_image[3],
                           color=palette[2])


def title_html_render(product_name, category, palette):
    card_title = product_name.partition(' ')[0]
    return render_template('title_card_single_photo.html', category=card_title,
                           color1=palette[0],
                           color2=palette[2])


def title_css_render(product_images, palette):

    product_image = product_images.split(',')

    return render_template('title_card_single_photo.css', url_img=product_image[0], color=palette[2])


def single_post_creator(product_list):
    print('Start create_single_post')
    rerq = create_single_card(product_list, 'with_title')
    card_creator_requests.send_single_post(rerq[0], rerq[1], rerq[2], rerq[3], rerq[4], rerq[5])

def create_single_card(product_list, mess):
    global single_nomer, single_files, single_media_list, single_urls_list, single_publication_category
    single_nomer = 1
    make_title = False
    single_files = {}
    single_media_list = []

    single_publication_category = ''

    names_list = []
    single_urls_list = []
    if product_list:
        for product in product_list:
            (product_id, product_name, product_article, product_sizes, product_price,
             product_price_with_ozon_card, product_images, single_publication_category, product_url,
             description) = product

            product_image = product_images.split(',')
            fd = urlopen(product_image[0])
            f = io.BytesIO(fd.read())
            fd.close()
            color_thief = ColorThief(f)
            # dominant_color = color_thief.get_color(quality=1)
            palette = color_thief.get_palette(color_count=2, quality=2)

            if mess == 'with_title' and make_title == False:
                name = f'photo{single_nomer}'
                print(name)

                # product_image = product_images.split(',')
                # fd = urlopen(product_image[0])
                # f = io.BytesIO(fd.read())
                # fd.close()
                # color_thief = ColorThief(f)
                # get the dominant color
                # dominant_color = color_thief.get_color(quality=1)
                # # build a color palette
                # palette = color_thief.get_palette(color_count=2, quality=2)
                # print('palette')
                # print(palette)


                render_title_html = single_title_html_render(single_publication_category, palette, product_name, product_image)

                render_title_css = single_title_css_render(product_images, palette)
                single_card(render_title_html, render_title_css)
                make_title = True
                single_files.update({name: open("card_creator/cards/card" + str(single_nomer) + ".png", "rb")})
                single_media_list.append(dict(type='photo', caption='', parse_mode='HTML', media=f'attach://{name}'))
                single_nomer += 1

            name = f'photo{single_nomer}'

            # product_image = product_images.split(',')
            # fd = urlopen(product_image[0])
            # f = io.BytesIO(fd.read())
            # fd.close()
            # color_thief = ColorThief(f)
            # # get the dominant color
            # dominant_color = color_thief.get_color(quality=1)
            # # build a color palette
            # # palette = color_thief.get_palette(color_count=3)
            # print('palette')
            # print(dominant_color)

            render_html = single_html_render(product_name, product_article, product_sizes, product_price,
                                      product_price_with_ozon_card, palette, product_image)



            render_css = single_css_render(product_images)
            single_card(render_html, render_css)


            single_urls_list.append(product_url)
            names_list.append(product_name)
            single_files.update({name: open("card_creator/cards/card" + str(single_nomer) + ".png", "rb")})

            if single_nomer == 1:
                single_media_list.append(dict(type='photo', caption='', parse_mode = 'HTML', media=f'attach://{name}'))
            else:
                single_media_list.append(dict(type='photo', media=f'attach://{name}'))

            single_nomer += 1

    return single_media_list, single_files, single_publication_category, names_list, single_urls_list, description

def single_html_render(product_name, product_article, product_sizes, product_price,
                       product_price_with_ozon_card, palette, product_image):
    print(type(product_sizes))
    print(product_sizes)
    product_size = product_sizes.split(' ,')
    print(product_size)
    print(type(product_size))

    del product_size[-1]

    string = ''
    for el in product_size:
        # Добавляем к строке элемент списка
        string += str(el)
        # Добавляем к строке разделитель — в данном случае пробел
        string += ', '
    print(string)
    print(type(string))

    Remove_last = string[:len(string) - 2]
    print(Remove_last)

    return render_template('single_card_single_photo.html', name=product_name, article=product_article,
                           size=Remove_last, price=product_price,
                           ozon_card_price=product_price_with_ozon_card,  color=palette[2],

                           )


def single_css_render(product_images):

    product_image = product_images.split(',')

    return render_template('single_card_single_photo.css',  url_img1=product_image[1],
                           url_img2=product_image[2],
                           url_img3=product_image[3],
                           url_img=product_image[1],)


def single_title_html_render(category, palette, product_name, product_image):
    return render_template('single_title_card_single_photo.html', category=category,
                           color=palette[0],  name=product_name,

                           )


def single_title_css_render(product_images, palette):
    product_image = product_images.split(',')

    return render_template('single_title_card_single_photo.css', url_img=product_image[0],
                           color1=palette[0],
                           color2=palette[1],
                           color3=palette[2])

def single_card(html, css):
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
        save_as='card' + str(single_nomer) + '.png', size=(1024, 1280)
    )
