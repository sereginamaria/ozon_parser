import json
import requests
telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"


def send_media_group(media_list, files):
    requests.post(
        url=telegram_url + '/sendMediaGroup', data={'chat_id': 6181726421, 'media': json.dumps(media_list)},
        files=files
    )

def send_post(media_list, files):
    print('122222222222222222')
    requests.post(
        url=telegram_url + '/sendMediaGroup', data={'chat_id': 6181726421, 'caption': 'hkhbkhgjr', 'media': json.dumps(media_list)},
        files=files
    )