import json
import requests
telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"


def send_media_group(media_list, files):
    requests.post(
        url=telegram_url + '/sendMediaGroup', data={'chat_id': 6181726421, 'media': json.dumps(media_list)},
        files=files
    )

def send_post(media_list, files, publication_category, names_list, urls_list):
    new_publication_category = ''.join(publication_category.split( ))
    i = 0
    str = ''

    for name in names_list:
        str = str + "\n<a href=\'https://www.ozon.ru" + urls_list[i] + "\'>" + name + "</a>"
        i = i + 1
    #
    # new_caption = ("#" + new_publication_category + "\n<a href=\'https://www.ozon.ru" +
    #                urls_list[i] + "\'>" + name + "</a>")

    new_caption = ("#" + new_publication_category + str)

    for el in media_list:
        if 'caption' in el:
            el['caption'] = new_caption

    requests.post(
        url=telegram_url + '/sendMediaGroup', data={'chat_id': '@ozon_trend_plus', 'media': json.dumps(media_list)},
        files=files
    )

    # @ozon_trend_plus