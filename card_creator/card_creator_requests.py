import json
import requests
telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"


def send_media_group(media_list, files):
    requests.post(
        url=telegram_url + '/sendMediaGroup', data={'chat_id': 6181726421, 'media': json.dumps(media_list)},
        files=files
    )

def send_post(media_list, files, publication_category, product_name, product_url):
    print('122222222222222222')
    print(type(product_name))
    print(type(product_url))
    print(product_url)
    new_publication_category = ''.join(publication_category.split( ))

    new_caption = ("#" + new_publication_category + "\n<a href=\'https://www.ozon.ru" +
                   product_url + "\'>" + product_name + "</a>")
    print(new_caption)
    print(type(new_caption))
    for el in media_list:
        if 'caption' in el:
            el['caption'] = new_caption

    print(media_list)
    requests.post(
        url=telegram_url + '/sendMediaGroup', data={'chat_id': '6181726421', 'media': json.dumps(media_list)},
        files=files
    )

    # @ozon_trend_plus