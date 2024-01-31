import json
import random

import requests
from telebot import types

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"

mass_of_stikers = ['\U0001F531', '\U000026B1', '\U0001F9FF', '\U0001FAAC',
                   '\U0001F5FF', '\U0001FAA7', '\U0001F9EF', '\U0001FAE7', '\U0001F9EC',
                   '\U00002697', '\U0001F9EA', '\U0001F4F7', '\U0001F3A5', '\U0001F39E',
                   '\U0001F3AC', '\U0001F484', '\U0001F48D', '\U0001F48E', '\U0001F451', '\U0001F452', '\U0001F6CD',
                   '\U0001F97C', '\U0001F9BA', '\U0001F454', '\U0001F455', '\U0001F456', '\U0001F9E5', '\U0001F457',
                   '\U0001F458', '\U0001F97B', '\U0001FA73', '\U0001F45A', '\U0001FAAD', '\U0001F45B', '\U0001F45C',
                   '\U0001F9F6', '\U0001F5BC', '\U0001F3A8', '\U0001F9F8', '\U0001FAA9', '\U0001FA86', '\U0001F52E',
                   '\U0001F380', '\U0001F381', '\U00002728', '\U0001F388', '\U0001F383', '\U0001F384', '\U000026F1',
                   '\U000026A1', '\U00002744', '\U00002603', '\U000026C4', '\U0001F525', '\U00002B50', '\U0001F31F',
                   '\U00002600', '\U0001F315', '\U0001F319', '\U0001F9CA', '\U0001F964', '\U0001F9CB', '\U0001F9C3',
                   '\U00002615', '\U0001F366', '\U0001F367', '\U0001F368', '\U0001F369', '\U0001F36A', '\U0001F382',
                   '\U0001F370', '\U0001F9C1', '\U0001F967', '\U0001F36B', '\U0001F36C', '\U0001F36D', '\U0001F36E',
                   '\U0001F36F', '\U0001F980', '\U0001F99E', '\U0001F990', '\U0001F991', '\U0001F957', '\U0001F37F',
                   '\U0001F354', '\U0001F35F', '\U0001F355', '\U0001F32D', '\U0001F96A', '\U0001F32E', '\U0001F32F',
                   '\U0001F968', '\U0001F96F', '\U0001F95E', '\U0001F9C7', '\U0001F9C0', '\U0001F950', '\U0001F956',
                   '\U0001F955', '\U0001F33D', '\U0001F336', '\U0001FAD1', '\U0001F966', '\U0001F951', '\U0001F349',
                   '\U0001F34A', '\U0001F34B', '\U0001F34C', '\U0001F34D', '\U0001F96D', '\U0001F34E', '\U0001F34F',
                   '\U0001F350', '\U0001F351', '\U0001F352', '\U0001F353', '\U0001FAD0', '\U0001F95D', '\U0001F344',
                   '\U0001F347', '\U0001F490', '\U0001F338', '\U0001F3F5', '\U0001F339', '\U0001F940', '\U0001F33A',
                   '\U0001F33B', '\U0001F33C', '\U0001F337', '\U0001F331', '\U0001FAB4', '\U0001F332', '\U0001F333',
                   '\U0001F334', '\U0001F335', '\U0001F33E', '\U0001F33F', '\U00002618', '\U0001F340', '\U0001F341',
                   '\U0001F342', '\U0001F343', '\U0001F98B', '\U0001F438', '\U0001F40A', '\U0001F422', '\U0001F98E',
                   '\U0001F40D', '\U0001F432', '\U0001F409', '\U0001F995', '\U0001F996', '\U0001F433', '\U0001F40B',
                   '\U0001F42C', '\U0001F9AD', '\U0001F41F', '\U0001F420', '\U0001F421', '\U0001F988', '\U0001F419',
                   '\U0001F41A', '\U0001F99C', '\U0001F9A9', '\U0001F99A', '\U0001F986', '\U0001F9A2', '\U0001F423',
                   '\U0001F424', '\U0001F425', '\U0001F426', '\U0001F427', '\U0001F43E', '\U0001F43B', '\U0001F428',
                   '\U0001F43C', '\U0001F43F', '\U0001F994', '\U0001F42D', '\U0001F401', '\U0001F400', '\U0001F439',
                   '\U0001F430', '\U0001F407', '\U0001F999', '\U0001F984', '\U0001F434', '\U0001F98A', '\U0001F431',
                   '\U0001F408', '\U0001F981', '\U0001F42F', '\U0001F436', '\U0001F415', '\U0001F9AE', '\U0001F429',
                   '\U0001F478', '\U0001F4AB', '\U00002764', '\U0001F9E1', '\U0001F49B', '\U0001F49A', '\U0001F499',
                   '\U0001F49C', '\U0001F48C', '\U0001F498', '\U0001F49D', '\U0001F496', '\U0001F497', '\U0001F493',
                   '\U0001F49E', '\U0001F495', '\U0001F49F', '\U00002763']


def send_media_group(media_list, files):
    images_response = requests.post(
        url=telegram_url + '/sendMediaGroup', data={'chat_id': 6181726421, 'media': json.dumps(media_list)},
        files=files
    )
    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': str(images_response)}
    ).json()

    print(images_response)

    while images_response.status_code != 200:
        print('Фотографии не отправлены, response !== 200')
        images_response = requests.post(
            url=telegram_url + '/sendMediaGroup', data={'chat_id': 6181726421, 'media': json.dumps(media_list)},
            files=files
        )

    print('new resp')
    print(images_response)




def send_post(media_list, files, publication_category, names_list, urls_list):
    new_publication_category = ''.join(publication_category.split())
    i = 0
    str = ''

    keyboard = {
        "inline_keyboard": [
            [

            ],
            [

            ]
        ],
    }

    sub_category =''
    for name in names_list:
        str = str + "\n<a href=\'https://www.ozon.ru" + urls_list[i] + "\'>" + name + "</a>"

        if i == 0:
            sub_category = name.partition(' ')[0]

        inline = {
            "text": i+1,
            "url": "https://www.ozon.ru" + urls_list[i]
        }

        if i <3:
            keyboard["inline_keyboard"][0].append(inline)
        else:
            keyboard["inline_keyboard"][1].append(inline)
        i = i + 1
        # print(keyboard)



    #
    # new_caption = ("#" + new_publication_category + "\n<a href=\'https://www.ozon.ru" +
    #                urls_list[i] + "\'>" + name + "</a>")

    if (new_publication_category == 'ВерхняяОдежда' or new_publication_category == 'Кофта'
        or new_publication_category == 'Обувь' or new_publication_category == 'Аксессуары'):
        new_caption = ("#" + new_publication_category + ' #' + sub_category)
    else:
        new_caption = ("#" + new_publication_category)


    stikers = random.sample(mass_of_stikers, 4)
    text = ''

    for stiker in stikers:
        text += stiker

    text += 'ㅤ'

    for el in media_list:
        if 'caption' in el:
            el['caption'] = new_caption

    post_response = requests.post(
        url=telegram_url + '/sendMediaGroup', data={'chat_id': '6181726421',
                                                    'media': json.dumps(media_list)},
        files=files
    ).json()

    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': post_response}
    ).json()

    print(post_response)

    while post_response.status_code != 200:
        print('Фотографии не отправлены, response !== 200')
        post_response = requests.post(
            url=telegram_url + '/sendMediaGroup', data={'chat_id': 6181726421, 'media': json.dumps(media_list)},
            files=files
        )

    print('new resp')
    print(post_response)

    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': text, "reply_markup": json.dumps(keyboard),
              "resize_keyboard": True}
    ).json()




def send_single_post(media_list, files, publication_category, names_list, urls_list):
    new_publication_category = ''.join(publication_category.split())
    i = 0
    str = ''

    keyboard = {
        "inline_keyboard": [
            [

            ]
        ],
    }
    sub_category = ''
    for name in names_list:
        str = str + "\n<a href=\'https://www.ozon.ru" + urls_list[i] + "\'>" + name + "</a>"

        if i == 0:
            sub_category = name.partition(' ')[0]

        inline = {
            "text": i + 1,
            "url": "https://www.ozon.ru" + urls_list[i]
        }


        keyboard["inline_keyboard"][0].append(inline)

        i = i + 1

    #
    # new_caption = ("#" + new_publication_category + "\n<a href=\'https://www.ozon.ru" +
    #                urls_list[i] + "\'>" + name + "</a>")

    if (new_publication_category == 'ВерхняяОдежда' or new_publication_category == 'Кофта'
            or new_publication_category == 'Обувь' or new_publication_category == 'Аксессуары'):
        new_caption = ("#" + new_publication_category + ' #' + sub_category)
    else:
        new_caption = ("#" + new_publication_category)

    for el in media_list:
        if 'caption' in el:
            el['caption'] = new_caption

    requests.post(
        url=telegram_url + '/sendMediaGroup', data={'chat_id': '6181726421', 'media': json.dumps(media_list)},
        files=files
    )


    stikers = random.sample(mass_of_stikers, 4)
    text = ''

    for stiker in stikers:
        text += stiker

    text += 'ㅤ'
    # print('4215798099999999999')
    # print(text)
    # text = '\U0001F6CD' + description.partition('.')[0] + '.'
    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': text, "reply_markup": json.dumps(keyboard),
              "resize_keyboard": True}
    ).json()

def info(text):
    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': text}
    ).json()

    # @ozon_trend_plus
    # 6181726421
#    'Ссылка на товар:ㅤㅤㅤ'
