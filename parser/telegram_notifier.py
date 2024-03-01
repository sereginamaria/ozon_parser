import requests

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"


def send_execution_completed():
    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': 'Выполнение завершено!'}
    ).json()


def send_wait():
    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': 'Ожидайте...'}
    ).json()


def send_message(text):
    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': text}
    ).json()
