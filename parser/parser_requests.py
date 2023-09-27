import requests

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"
def execution_completed(message_type):
    if message_type:
        requests.post(
            url=telegram_url + '/sendMessage',
            data={'chat_id': 6181726421, 'text': 'Выполнение завершено!'}
        ).json()

def error(text):
    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': text}
    ).json()

def wait():
    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': 'Ожидайте...'}
    ).json()
