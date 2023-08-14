import requests
from flask import render_template
from html2image import Html2Image
from jinja2 import Environment, FileSystemLoader, Template

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"

def card_creator(message):
    print(message)
    hti = Html2Image(
        output_path='card_creator',
        custom_flags=[
            '--no-sandbox'
            '--remote-allow-origins=*',
            '--hide-scrollbars'
        ],
    )

    jinja2_template_string = open("card_creator/card.html", 'rb').read()

    # Create Template Object
    template = Template(jinja2_template_string)

    # Render HTML Template String
    html_template_string = template.render(name="John")

    print(html_template_string)
    # environment = Environment(loader=FileSystemLoader("card_creator/templates/"))
    # template = environment.get_template("card.html")
    # template.render(name='eee')

    hti.screenshot(
        html_file='card_creator/card.html', css_file='card_creator/test.css',
        save_as='card.png', size=(1024, 1280)
    )

    files = {'photo': open("card_creator/card.png", "rb")}
    requests.post(
        url=telegram_url + '/sendPhoto',
        data={'chat_id': 6181726421}, files=files
    )