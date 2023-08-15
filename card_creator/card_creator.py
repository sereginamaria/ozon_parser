import requests
from flask import render_template
from html2image import Html2Image

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"


def card_creator(message):
    print(message)

    render_html = render()
    # f = open('card_creator/render_html.html', 'w', encoding='UTF-8')  # открытие в режиме записи
    # f.write(render_html)

    card(render_html)


def card(html):
    hti = Html2Image(
        output_path='card_creator/',
        custom_flags=[
            '--no-sandbox'
            '--remote-allow-origins=*',
            '--hide-scrollbars'
        ],
    )

    hti.screenshot(
        html_str=html,
        save_as='card.png', size=(1024, 1280)
    )

    files = {'photo': open("card_creator/card.png", "rb")}
    requests.post(
        url=telegram_url + '/sendPhoto',
        data={'chat_id': 6181726421}, files=files
    )


def render():
    return render_template('cardtest.html', name='eee')


if __name__ == '__main__':
    from parser.main import app

    with app.app_context():
        card_creator("dsfsdf")
