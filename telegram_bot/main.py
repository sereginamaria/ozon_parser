import logging
import sys
from threading import Thread
import telebot
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import datetime
from datetime import date
import bot_database
import create_post
import get_post
import get_products_from_page
import get_product
import verification
import autoposting
import create_single_post
import get_all_day_posts
import time
import requests

bot = telebot.TeleBot('6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og')

th_1 = Thread(target=autoposting.autop)
th_1.start()

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "/get_products_from_page":
        get_products_from_page.init_bot(message, bot)
    elif message.text == "/get_product":
        get_product.init_bot(message, bot)
    elif message.text == "/verification":
        verification.init_bot(message, bot, 'verification')
    elif message.text == "/create_post":
        create_post.init_bot(message, bot)
    elif message.text == "/create_single_post":
        create_single_post.init_bot(message, bot)
    elif message.text == "/get_post":
        get_post.init_bot(message, bot)
    elif message.text == "/get_all_day_posts":
        get_all_day_posts.init_bot(message, bot)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Список команд:"
                                               "/get_products_from_page - распарсить страницу с товарами"
                                               "/get_product - распарсить товар"
                                               "/verification - проверифицирвоать товары"
                                               "/create_post - создать пост"
                                               "/create_single_post - создать одиночный пост"
                                               "/get_post - посмотреть пост"
                                               "/get_all_day_posts - посмотреть все посты на день"
                                               "/help - помощь")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

token = '6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og'
url = 'https://api.telegram.org/botf'

def get_updates(offset=0):
    # result = requests.get(f'{url}{token}/getUpdates?offset={offset}').json()
    # return result['result']
    requests.get(f'{url}{token}/getUpdates?offset={offset}').json()


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
def call(call):
    result, key, step = DetailedTelegramCalendar(calendar_id=1, locale='ru').process(call.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        create_post.get_date_of_publication(call.message, result)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2))
def call(call):
    result, key, step = DetailedTelegramCalendar(calendar_id=2, locale='ru').process(call.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        get_post.get_date_of_publication(call.message, result)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=3))
def call(call):
    result, key, step = DetailedTelegramCalendar(calendar_id=3, locale='ru').process(call.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        create_single_post.get_date_of_publication(call.message, result)

@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=4))
def call(call):
    result, key, step = DetailedTelegramCalendar(calendar_id=4, locale='ru').process(call.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        get_all_day_posts.get_date_of_publication(call.message, result)

@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'verification')
def callback_inline(call):
    if call.data.split('|')[1] == "yes" or call.data.split('|')[1] == "no":
        bot_database.callback_verification(call.data)
        verification.init_bot(call.message, bot, 'verification')
    else:
        verification.init_change_name(call.message, bot, call.data)


@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'create_post_platform')
def callback_inline(call):
    publication_platform = call.data.split('|')[1]
    create_post.get_publication_platform(call.message, publication_platform)

@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'create_single_post_platform')
def callback_inline(call):
    publication_platform = call.data.split('|')[1]
    create_single_post.get_publication_platform(call.message, publication_platform)

@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'choice')
def callback_inline(call):
    create_post.record_data(call.message, call.data.split('|')[1], call.data.split('|')[2])

@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'choice_single')
def callback_inline(call):
    create_single_post.record_data(call.message, call.data.split('|')[1], call.data.split('|')[2])


@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'get_post_platform')
def callback_inline(call):
    publication_platform = call.data.split('|')[1]
    get_post.get_publication_platform(call.message, publication_platform)

@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'get_all_day_posts_platform')
def callback_inline(call):
    publication_platform = call.data.split('|')[1]
    get_all_day_posts.get_publication_platform(call.message, publication_platform)


while True:
    try:
        bot.polling(none_stop=True)
    except:
        print('bolt')
        logging.error('error: {}'.format(sys.exc_info()[0]))
        time.sleep(5)

# bot.polling(none_stop=True, interval=0)
